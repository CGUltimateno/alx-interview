#!/usr/bin/python3
"""You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and each box
may contain keys to the other boxes.
Design a method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    if len(boxes) == 0:
        return False
    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)
    if len(keys) == len(boxes):
        return True
    return False
