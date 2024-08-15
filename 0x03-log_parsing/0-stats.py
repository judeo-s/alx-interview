#!/usr/bin/env python3
"""
A script that reads stdin line by line and computes metrics
"""

import sys
import signal


status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
total_size = 0
counter = 0


def log_parser():
    """
    Analyze logs and print stats
    """
    global counter
    global total_size
    global status_codes

    for line in sys.stdin:
        try:
            line = line.strip()
            analysis = line.split(" ")

            size = int(analysis[-1])
            total_size += size

            code = int(analysis[-2])
            status_codes[code] += 1
            counter += 1
            if not counter % 10:
                print_codes(status_codes, total_size)
        except ValueError as e:
            pass


def print_codes(signal, frame):
    """
    Print stats
    """
    global status_codes
    global total_size

    print(f"File size: {total_size}")
    for key in status_codes.keys():
        if status_codes[key]:
            print(f"{key}: {status_codes[key]}")


signal.signal(signal.SIGINT, print_codes)
log_parser()
