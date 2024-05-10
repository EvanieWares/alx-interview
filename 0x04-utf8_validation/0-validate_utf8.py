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
    def countLeadingOnes(byte):
        count = 0
        mask = 1 << 7
        while byte & mask:
            count += 1
            mask >>= 1
        return count

    i = 0
    while i < len(data):
        leading_ones = countLeadingOnes(data[i])
        if leading_ones == 0:
            i += 1
            continue
        if leading_ones == 1 or leading_ones > 4:
            return False
        for j in range(1, leading_ones):
            if i + j >= len(data) or (data[i + j] >> 6) != 0b10:
                return False
        i += leading_ones
    return True
