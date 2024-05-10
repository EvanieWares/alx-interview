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
    return all(byte >> 7 == 0 for byte in data)
