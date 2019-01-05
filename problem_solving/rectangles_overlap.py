"""
Check if 2 rectangles overlap
Assumption: sides are parallel to both axes
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, up_left, bot_right):
        self.up_left = up_left
        self.bot_right = bot_right


def do_overlap(rect_one, rect_two):
    """
    Basic idea:
    if one rectangle is above other, return False
    if one rectangle is to the left of the another, return False
    :param rect_one: First rectangle
    :param rect_two: Second rectangle
    :return: do they overlap
    """
    if rect_one.up_left.x > rect_two.bot_right.x or rect_one.bot_right.x < rect_two.up_left.x:
        return False
    if rect_one.bot_right.y > rect_two.up_left.y or rect_one.up_left.y < rect_two.bot_right.y:
        return False
    return True

