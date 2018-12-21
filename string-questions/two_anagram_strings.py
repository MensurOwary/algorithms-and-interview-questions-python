"""
Check if two Strings are anagrams of each other?
"""


def are_anagrams(first, second):
    # dictionary to keep the count of letters
    dictionary = {}
    # go through the first string
    for ch in first:
        # if letter isn't in dictionary, initialize it with value of 1
        if ch not in dictionary:
            dictionary[ch] = 1
        # else increment it by 1
        else:
            dictionary[ch] = dictionary[ch] + 1

    # go through the next string
    for ch in second:
        # if letter isn't in the dictionary, then return False
        # because if it is not common then they aren't anagrams
        if ch not in dictionary:
            return False
        # otherwise, proceed
        # decrease the value corresponding to the letter by 1
        else:
            dictionary[ch] = dictionary[ch] - 1
    # if the list of elements with values more than 0 is empty return True
    # otherwise false
    return len([k for k, v in dictionary.items() if v > 0]) == 0

