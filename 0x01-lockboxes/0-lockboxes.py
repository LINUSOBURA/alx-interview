#!/usr/bin/env python3


def canUnlockAll(boxes):
    """Return True if all boxes can be unlocked, else return False
	Args:
		boxes (list): list of boxes"""

    opened_boxes = {0}
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)
                stack.append(key)

    return len(opened_boxes) == len(boxes)
