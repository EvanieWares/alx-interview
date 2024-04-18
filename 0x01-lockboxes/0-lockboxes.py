#!/usr/bin/python3
"""A module that determine if all the given boxes can be opened"""
from typing import List, Set


def getVisitedBoxes(boxes: List[List], keys: List, visited: Set) -> Set:
    """
    Gets the boxes opened

    Args:
        boxes (List[List]): List of lists to check
        keys (List): A list of keys to open the boxes with
        visited (Set): The boxes opened

    Returns:
        Set: The boxes opened
    """
    for key in keys:
        if key not in visited and key < len(boxes):
            visited.add(key)
            visited = getVisitedBoxes(boxes, boxes[key], visited)
    return visited


def canUnlockAll(boxes: List[List]) -> bool:
    """
    Determines if all boxes can be opened

    Args:
        boxes (list[list]): List of lists to check

    Returns:
        bool: Whether all boxes can be opened
    """
    visitedBoxes: Set[int] = {0}
    visitedBoxes = getVisitedBoxes(boxes, boxes[0], visitedBoxes)
    if len(visitedBoxes) == len(boxes):
        return True
    return False
