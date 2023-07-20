#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    sorted_status_codes = sorted(status_codes.keys())
    for code in sorted_status_codes:
        if code.isdigit():
            print("{}: {}".format(code, status_codes[code]))

def main():
    total_size = 0
    status_codes = {}

    try:
        for line_number, line in enumerate(sys.stdin, 1):
            parts = line.split()
            if len(parts) < 9:
                continue

            ip, date, method, path, protocol, status_code, file_size = parts[:7]

            if not ip.replace('.', '').isdigit() or not status_code.isdigit() or not file_size.isdigit():
                continue

            status_code = int(status_code)
            file_size = int(file_size)
            total_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

            if line_number % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
