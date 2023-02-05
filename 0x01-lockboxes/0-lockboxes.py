#!/usr/bin/python3
""" oppening boxes"""

def getKeys(boxes):
    """get all keys"""
    checked = []
    size = len(boxes)
    for row in range(size):
        for col in range(len(boxes[row])):
            k = boxes[row][col]
            if (k < size and k != row):
                if k not in checked:
                    checked.append(k)
    checked.sort()
    return checked


def canUnlockAll(boxes):
    """determines if all the boxes can be opened"""
    opened = getKeys(boxes)
    if 0 in opened:
        opened.remove(0)
    return len(opened) == len(boxes) - 1
