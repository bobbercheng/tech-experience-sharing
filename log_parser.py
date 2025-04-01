import os
import glob
from datetime import datetime
import json
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

def parse_timestamp(timestamp_str):
    """Convert timestamp string to datetime object."""
    return datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S.%f')

def calculate_duration(start_time, end_time):
    """Calculate duration between start and end time in seconds."""
    return (parse_timestamp(end_time) - parse_timestamp(start_time)).total_seconds()

def process_single_file(log_file: str, result: dict, result_lock: Lock):
    # Extract hostname from filename (YYYY-MM-DD-HOSTNAME.log)
    hostname = os.path.basename(log_file).split('.')[0].split('-', 3)[3]
    
    host_result = {}
    # Track call states
    active_calls = {}
    try:
        with open(log_file, 'r') as f:
            for line in f:
                # Parse log line
                timestamp, call_id, event = line.strip().split('|')
                
                if event == 'Start':
                    active_calls[call_id] = timestamp
                elif event == 'End' and call_id in active_calls:
                    start_time = active_calls.pop(call_id)
                    
                    # Initialize call_id data structure if not exists
                    if call_id not in host_result:
                        host_result[call_id] = {
                            'average': 0,
                            'details': []
                        }
                    
                    # Add details for this call duration
                    host_result[call_id]['details'].append({
                        'start': start_time,
                        'end': timestamp,
                        'duration': calculate_duration(start_time, timestamp)
                    })
    except Exception as e:
        print(f"Error processing {log_file}: {e}")
    
    # Update global result dict thread-safely
    with result_lock:
        result[hostname] = host_result


def process_log_files(logs_dir):
    """Process all log files in the specified directory."""
    result = {}
    
    # Find all log files in the logs directory
    log_files = glob.glob(os.path.join(logs_dir, '*.log'))
        
    result_lock = Lock()
    
    
    # Process files in parallel using thread pool
    with ThreadPoolExecutor(max_workers=os.cpu_count() * 2) as executor:
        executor.map(process_single_file, log_files, [result], [result_lock])
    
    # Calculate averages for each call_id
    for hostname in result:
        sum_duration = 0
        for call_id in result[hostname]:
            details = result[hostname][call_id]['details']
            if details:
                total_duration = sum(
                    detail['duration']
                    for detail in details
                )
                result[hostname][call_id]['average'] = total_duration / len(details)
                sum_duration += result[hostname][call_id]['average']
        if len(result[hostname]) > 0:
            average_duration = sum_duration / len(result[hostname])
            result[hostname]['average'] = average_duration
    
    return result

def main():
    # Specify the logs directory (assuming it's in the same directory as the script)
    logs_dir = 'logs'
    
    # Create logs directory if it doesn't exist
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    
    # Process log files and get results
    results = process_log_files(logs_dir)
    
    # Print results in JSON format
    print(json.dumps(results, indent=4))

if __name__ == '__main__':
    main() 