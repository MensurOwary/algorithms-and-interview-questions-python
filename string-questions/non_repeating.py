"""
The first non-repeating character
"""


# version 1
def non_repeating(string):
    # chars and their counts so far
    seen = {}
    # chars and their indices
    # we save the indices of chars we've seen for the first time
    # so the first occurrence is saved
    indices = {}
    # go through each char in string
    for i, ch in enumerate(string):
        # add to seen dictionary if not seen
        if ch not in seen:
            # count is 1
            seen[ch] = 1
            # save the index
            indices[ch] = i
        else:
            # otherwise increment its count
            seen[ch] += 1
    # save the char and its corresponding index where the value is 1
    mins = {k: indices[k] for k, v in seen.items() if v == 1}
    # return the char with minimum index
    return min(mins, key=mins.get)


# version 2
def non_repeating_v2(string):
    # chars we've seen so far and their indices
    seen = {}
    # go through the string
    for ch in string:
        # add to the dictionary if not seen
        if ch not in seen:
            # count is 1
            seen[ch] = 1
        else:
            # otherwise, increment
            seen[ch] += 1
    # go through the string again
    for ch in string:
        # if count is 1, return
        # basically the first char we will see that has 1 occurrence
        # is the answer we're looking for
        if seen[ch] == 1:
            return ch
    # otherwise, there's none
    # return none
    return None

