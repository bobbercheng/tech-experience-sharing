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