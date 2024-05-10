#!/usr/bin/python3
"""
Module for validating UTF-8 sequences.

This module contains a single function `validUTF8` that checks if a given
list of bytes represents a valid UTF-8 sequence.
"""


def validUTF8(data):
    """
    Check if the given data is a valid UTF-8 sequence.

    Parameters:
        data (list): A list of bytes representing a UTF-8 sequence.

    Returns:
        bool: True if the data is a valid UTF-8 sequence, False otherwise.
    """
    byte_count = 0
    for byte in data:
        mask = 0x80
        if not byte_count:
            while byte & mask:
                byte_count += 1
                mask >>= 1
            if byte_count == 0:
                continue
            if byte_count > 4 or (byte_count == 1 and byte >= 0xC0):
                return False
        else:
            if byte >> 6 != 0b10:
                return False
        byte_count -= (byte >> 5 == 0b10) and 1
    return byte_count == 0
