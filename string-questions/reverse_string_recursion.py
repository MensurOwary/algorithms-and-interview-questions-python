"""
Reverse the string using recursion
"""


def reverse_recurse(string, st, end):
    if st > end:
        return ''.join(string)
    else:
        tmp_char = string[st]
        string[st] = string[end]
        string[end] = tmp_char
        return reverse_recurse(string, st+1, end-1)


def reverse(string):
    return reverse_recurse(list(string), 0, len(string)-1)