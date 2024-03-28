#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics
"""
import sys

def print_stats(file_size, status_codes):
    """
    Print the statistics
    """
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        print("{}: {}".format(key, value))

def main():
    """
    Main function
    """
    file_size = 0
    status_codes = {}
    count = 0
    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            file_size += int(data[-1])
            status_code = data[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1
            if count == 10:
                print_stats(file_size, status_codes)
                count = 0
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise


if __name__ == "__main__":
    main()
