"""
Reverse words in a given sentence without using any library method?
"""
# regular expression
import re
# deque
from collections import deque

# alphabetical pattern
pattern = re.compile('[a-zA-Z]')


def reverse_words(sentence):
    # reverse the sentence character-wise
    sentence_reversed = reverse(list(sentence), 0, len(sentence)-1)
    # initialize the deque
    stack = deque()
    # empty dummy-temp string
    st = ''
    # go through each character
    for ch in sentence_reversed:
        # if it is space character
        # then save the string so far
        if ch == ' ':
            # to tackle multiple spaces
            if len(st) != 0:
                # add the string to the stack
                stack.appendleft(st)
                # empty the string
                st = ''
        # otherwise, if it is a letter
        elif pattern.match(ch):
            # append it to the string so far
            st = st + ch
    # append the last string to the stack
    if len(st) != 0:
        # add the string to the stack
        stack.appendleft(st)
    # return the sentence in joined form
    return ' '.join(stack)


def reverse(string, st, end):
    if st > end:
        return ''.join(string)
    else:
        tmp_char = string[st]
        string[st] = string[end]
        string[end] = tmp_char
        return reverse(string, st+1, end-1)