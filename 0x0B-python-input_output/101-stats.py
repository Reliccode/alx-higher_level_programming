#!/usr/bin/python3
"""Module that prints the status code"""
import sys

lines_processed = 0
total_file_size = 0
status_code_counts = {}

try:
    for line in sys.stdin:
        lines_processed += 1

        # Extract relevant information from the line
        parts = line.split()
        if len(parts) >= 7:
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Update the total file size
            total_file_size += file_size

            # Update the status code count
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            else:
                status_code_counts[status_code] = 1

        # Print statistics every 10 lines
        if lines_processed % 10 == 0:
            print("File size:", total_file_size)
            for code in sorted(status_code_counts):
                count = status_code_counts[code]
                print(code + ":", count)

except KeyboardInterrupt:
    # Print statistics when a keyboard interruption occurs
    print("File size:", total_file_size)
    for code in sorted(status_code_counts):
        count = status_code_counts[code]
        print(code + ":", count)
