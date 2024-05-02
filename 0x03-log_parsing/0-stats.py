#!/usr/bin/python3
"""
Module 0-stats

Implements a function that reads stdin line by line and computes metrics
"""


def print_metrics(size, status_codes, found_codes):
    """
    Prints the computed metrics to stdout

    Parameters:
    - size (int): size of all metrics
    - status_codes (list): list of all status codes
    - found_codes (list): list of all status codes read
    """
    print("File size: {:d}".format(size))
    for code in status_codes:
        if found_codes.count(code) != 0:
            print("{} {}".format(code, found_codes.count(code)))


def read_metrics():
    """
    Reads stdin line by line and computes metrics
    """
    import sys
    try:
        size = 0
        num = 0
        status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
        found_codes = []
        for line in sys.stdin:
            num = num + 1
            line = line.strip()
            splitted = line.split()
            found_codes.append(splitted[7])
            size += int(splitted[8])
            if num == 10:
                num = 0
                print_metrics(size, status_codes, found_codes)

    except KeyboardInterrupt:
        print_metrics(size, status_codes, found_codes)


if __name__ == "__main__":
    read_metrics()