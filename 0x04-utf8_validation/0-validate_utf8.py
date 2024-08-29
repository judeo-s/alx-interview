#!/usr/bin/python3
"""
A module that determines if a given data set represents a valid UTF-8
encoding
"""


def validUTF8(data) -> bool:
    """
    Method that determines if a given data set represents a valid UTF-8
    encoding.

    Args:
        - data: list of integers

    Returns:
        bool: True if data is a valid UTF-8 encoding, else return False
    """
    bytes = 0
    for byte in data:
        byte = byte & 255
        if bytes:
            if byte >> 6 != 2:
                return False
            bytes -= 1
        else:
            if byte >> 7 == 0:
                continue
            elif byte >> 5 == 6:
                bytes = 1
            elif byte >> 4 == 14:
                bytes = 2
            elif byte >> 3 == 30:
                bytes = 3
            else:
                return False
    return bytes == 0
