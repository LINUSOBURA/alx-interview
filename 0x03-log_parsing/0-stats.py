#!/usr/bin/python3
"""
Log Persing
"""

import re
import sys

pattern = re.compile(
    r'^\d{1,3}(\.\d{1,3}){3} - \[[^\]]+\] "GET /projects/260 HTTP/1\.1" \d{3} \d+$'  # nopep8
)

size = 0
total_codes = 0
status_code_count = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}


def print_statistics():
    """Print the collected statistics"""
    print(f"File size: {size}")
    for code in sorted(status_code_count.keys()):
        count = status_code_count[code]
        if count > 0:
            print(f"{code}: {count}")


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            line = line.strip()
            if pattern.match(line):
                parts = line.split(" ")
                size += int(parts[-1])
                code = parts[-2]

                if code in status_code_count:
                    status_code_count[code] += 1
                    total_codes += 1

                if total_codes == 10:
                    print_statistics()

                    total_codes = 0
                    # status_code_count = {key: 0 for key in status_code_count}

    finally:
        print_statistics()
