#!/usr/bin/python3
import sys

def print_stats(file_size, status_codes):
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def main():
    file_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            if len(data) >= 7:
                file_size += int(data[-1])
                status_code = data[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1
            if count == 10:
                print_stats(file_size, status_codes)
                count = 0
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise

if __name__ == "__main__":
    main()
