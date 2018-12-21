"""
First non-repeating character
"""


def first_non_repeating(string):
    # construct a dictionary
    dictionary = {}
    # go through the letters
    for i, ch in enumerate(string):
        # if not add to the dictionary and initialize it with 1
        if ch not in dictionary:
            dictionary[ch] = 1
        # else, increment it by 1
        else:
            dictionary[ch] = dictionary[ch] + 1
    # letter and their positions pairs
    keys = {k: string.find(k) for k, v in dictionary.items() if v == 1}
    # return the one with minimum position
    return min(keys, key=keys.get)


def first_non_repeating_v2(string):
    # initialize an empty set to keep track of the seen characters
    seen = set()
    # go through each letter
    for i, ch in enumerate(string):
        # if there's no occurrence of the character afterwards
        # and if it has been seen for the first time
        # return it
        if string.find(ch, i + 1) == -1 and ch not in seen:
            return ch
        # otherwise, add it to the seen
        else:
            seen.add(ch)
    # after all, if not found, return empty
    return ''
