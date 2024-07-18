#!/usr/bin/python3
"""
Log Persing
"""

import re
import sys

pattern = re.compile(
    r'^([0-9]+(\.[0-9]+)+) - \[[^\]]*\] "(?:[^"]|"")*" [0-9]+ [0-9]+$',
    re.IGNORECASE)

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
                print(f"File size: {size}")
                for code, count in status_code_count.items():
                    if count > 0:
                        print(f"{code}: {count}")

                total_codes = 0
                status_code_count = {key: 0 for key in status_code_count}

except KeyboardInterrupt:
    print(f"File size: {size}")
    for code, count in status_code_count.items():
        if count > 0:
            print(f"{code}: {count}")

    sys.exit()
