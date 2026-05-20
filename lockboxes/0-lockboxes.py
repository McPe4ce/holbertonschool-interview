#!/usr/bin/python3

def canUnlockAll(boxes):
    unlocked = set([0])
    keys = list(boxes[0])
    length = len(boxes)

    while keys:
        key = keys.pop()
        if 0 <= key <= length and key not in unlocked:
            unlocked.add(key)
            keys.extend(boxes[key])

    return len(unlocked) == length
