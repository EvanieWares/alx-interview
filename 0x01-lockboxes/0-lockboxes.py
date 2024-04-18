#!/usr/bin/python3
"""
This module contains a method to determine if all the lockboxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determine if all the lockboxes can be opened.

    Args:
        boxes (list of list): A list of lists representing the lockboxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    # Initialize a set to keep track of opened boxes
    opened_boxes = set()
    # Add the first box (box 0) to the opened set
    opened_boxes.add(0)

    # Initialize a set to keep track of keys
    keys = set(boxes[0])

    # Loop through the keys set until there are no new keys
    while keys:
        # Get a key from the keys set
        key = keys.pop()

        # If the key opens a new box and the box is not opened yet
        if key < len(boxes) and key not in opened_boxes:
            # Add the box to the opened set
            opened_boxes.add(key)
            # Add the keys from the newly opened box to the keys set
            keys.update(boxes[key])

    # If the number of opened boxes is equal to the total number of boxes
    return len(opened_boxes) == len(boxes)
