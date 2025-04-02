"""
The target is to write a python code to read all log files in logs folder, each log file has filename as YYYY-MM-DD-HOSTNAME.log. Each log file
contain a call event with callID and event in each line like:
```
2023-10-26 10:00:00.123|CallID-123|Start
2023-10-26 10:00:05.456|CallID-124|Start
2023-10-26 10:00:10.789|CallID-123|Process data
2023-10-26 10:01:00.123|CallID-123|End
2023-10-26 10:01:00.789|CallID-124|End
2023-10-26 10:02:00.123|CallID-123|Start
2023-10-26 10:03:00.123|CallID-123|End
```
You need to parse all log files and read each CallID start time, end time in each host, calculate an average time for each call id like:
```
{
    "HOSTNAME": {
        "CallID-123": {
            "average": xxxx,
            "details":
            [
                {
                    'start': '2023-10-26 10:00:00.123',
                    'end': '023-10-26 10:01:00.123'
                },
                {
                    'start': '2023-10-26 10:02:00.123',
                    'end': '023-10-26 10:03:00.123'
                }
            ]
        },
        "CallID-124": {
            "average": xxxx,
            "details":
            [
                {
                    'start': '2023-10-26 10:00:05.456',
                    'end': '2023-10-26 10:01:00.789'
                }
            ]
        }
    }
    "HOSTNAME1": {
        ...
    }
}
```
"""

import os
import glob
from datetime import datetime
import json
from threading import Lock

def parse_timestamp(timestamp_str: str) -> datetime:
    """Convert timestamp string to datetime object."""
    return datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S.%f')

def parse_hostname(log_file: str) -> str:
    # Extract hostname from filename (YYYY-MM-DD-HOSTNAME.log)
    hostname = os.path.basename(log_file).split('.')[0].split('-', 3)[3]
    return hostname

def parse_log_line(line: str) -> tuple[str, str, str]:
    timestamp, call_id, event = line.strip().split('|')
    return timestamp, call_id, event

def calculate_duration(start_time: str, end_time: str) -> float:
    """Calculate duration between start and end time in seconds."""
    return (parse_timestamp(end_time) - parse_timestamp(start_time)).total_seconds()



def process_single_file(log_file: str, result: dict, result_lock: Lock) -> None:
    """Process a single log file and update the result dictionary."""
    hostname = parse_hostname(log_file)
    host_result = {}
    # Track call states
    active_calls = {}
    try:
        with open(log_file, 'r') as f:
            for line in f:
                # Parse log line
                timestamp, call_id, event = parse_log_line(line)
                
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
                    duration = calculate_duration(start_time, timestamp)
                    host_result[call_id]['details'].append({
                        'start': start_time,
                        'end': timestamp,
                        'duration': duration
                    })

                    # Update average duration for this call_id
                    if len(host_result[call_id]['details']) > 0:
                        with result_lock:
                            previous_average = host_result[call_id]['average']
                            count = len(host_result[call_id]['details'])
                            new_average = (previous_average  + duration) / count
                            host_result[call_id]['average'] = new_average


    except Exception as e:
        # print error callstack
        print(f"Error processing {log_file}: {e}")
        e.traceback.print_exc()
    
    # Update global result dict thread-safely
    with result_lock:
        result[hostname] = host_result


def process_log_files(logs_dir: str) -> dict:
    """Process all log files in the specified directory."""
    result = {}
    
    # Find all log files in the logs directory
    log_files = glob.glob(os.path.join(logs_dir, '*.log'))
        
    result_lock = Lock()
    
    
    for log_file in log_files:
        process_single_file(log_file, result, result_lock)


def main() -> None:
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