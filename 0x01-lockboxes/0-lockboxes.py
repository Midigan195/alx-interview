#!/usr/bin/python3
"""
This module contains a function for going through lockboxes
"""


def canUnlockAll(boxes):
    """
    This function checks that every item in the list can be visited.
    """
    visited = set()

    def depth_search(box_index):
        visited.add(box_index)
        for key in boxes[box_index]:
            if key not in visited:
                depth_search(key)

    depth_search(0)

    return len(visited) == len(boxes)
