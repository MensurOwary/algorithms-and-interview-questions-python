"""
Print duplicate characters from String
"""


def print_duplicate(string):
    dictionary = {}
    for ch in string:
        if ch not in dictionary:
            dictionary[ch] = 1
        else:
            dictionary[ch] = dictionary[ch] + 1
    return [k for k, v in dictionary.items() if v > 1]

