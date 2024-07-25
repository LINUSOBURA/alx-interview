#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Utf-8 validation function
    """
    num_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        bin_rep = bin(byte).replace('0b', '').rjust(8, '0')

        if num_bytes == 0:
            for i in range(8):
                if (byte & (1 << (7 - i))) == 0:
                    break
                num_bytes += 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1
    return num_bytes == 0
