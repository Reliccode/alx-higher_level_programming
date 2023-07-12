#!/usr/bin/python3
import sys

metrics = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

total_file_size = 0
lines_read = 0

try:
    for line in sys.stdin:
        lines_read += 1
        split_line = line.split()
        if len(split_line) >= 3:
            try:
                file_size = int(split_line[-1])
                total_file_size += file_size
            except ValueError:
                pass

        if len(split_line) >= 4:
            status_code = split_line[-2]
            if status_code in metrics:
                metrics[status_code] += 1

        if lines_read % 10 == 0:
            print(f"File size: {total_file_size}")
            for status_code in sorted(metrics.keys()):
                if metrics[status_code] > 0:
                    print(f"{status_code}: {metrics[status_code]}")

except KeyboardInterrupt:
    pass

print(f"File size: {total_file_size}")
for status_code in sorted(metrics.keys()):
    if metrics[status_code] > 0:
        print(f"{status_code}: {metrics[status_code]}")
