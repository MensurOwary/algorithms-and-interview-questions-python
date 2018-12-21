"""
Check if all chars are unique
No additional data structure is allowed
"""


def is_unique(str):
    """
    Algorithm:
    Say, the string is [abcd]
    We loop through the string and take each char and check
    if it exists in the next portion
    So, check if [a] exist in [bcd]
    If yes, return False
    If no, check others, if not found, return True

    :param str: string to check if contains unique chars
    :return: if chars are unique
    """
    for i, ch in enumerate(str):
        for k in str[i+1:]:
            if ch == k:
                return False
    return True


def is_unique_map_allowed(str):
    """
    Algorithm:
    Loop through chars
    Add to the dictionary if not seen
    If seen stop and return False
    If finished loop and not returned, return True
    :param str: string to check if contains unique chars
    :return: if chars are unique
    """
    seen = {}
    for ch in str:
        if ch in seen:
            return False
        seen[ch] = 1
    return True
