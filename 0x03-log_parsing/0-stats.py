#!/usr/bin/python3
"""
Module 0-stats

Implements a function that reads stdin line by line and computes metrics
"""
import sys


def print_stats(stats: dict, file_size: int) -> None:
    """
    Prints the stats to stdout

    Parameters:
    - file_size (int): size of all metrics
    - stats (dict): The dictionary containing status codes
    """
    print("File size: {:d}".format(filesize))
    for k, v in sorted(stats.items()):
        if v:
            print("{}: {}".format(k, v))


if __name__ == '__main__':

    filesize, count = 0, 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in status_codes}

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                filesize += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats(stats, filesize)
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise
