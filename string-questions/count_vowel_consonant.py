"""
Count a number of vowels and consonants in a given String?
"""
import re


def vowel_consonant(string):
    # vowel pattern
    vowel_p = re.compile('[aeuio]')
    # alphabet pattern, lowercase
    alpha_p = re.compile('[a-z]')
    # being lowercase or uppercase doesn't change vowel and consonant count
    # so make everything lowercase
    string = string.lower()
    # total counts
    vowel = consonant = 0
    # for each char in the string
    for ch in string:
        # if it is a vowel, increment vowel by 1
        if vowel_p.match(ch):
            vowel = vowel + 1
        # else if it is in the alphabet
        # increase consonant
        # because there's no way, something else will get here
        # apart from a consonant
        elif alpha_p.match(ch):
            consonant = consonant + 1
    # return them
    return vowel, consonant
