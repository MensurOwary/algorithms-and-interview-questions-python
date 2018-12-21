"""
Check if the string is the permutation of palindrome
"""


def is_palindrome_permutation(str):
    seen = {}
    for ch in str:
        if ch not in seen:
            seen[ch] = 1
        else:
            seen[ch] += 1
    only_one_odd = 0
    all_even = True
    for k, v in seen.items():
        if v % 2 != 0:
            only_one_odd += 1
            all_even = False
    if only_one_odd == 1 or all_even:
        return True
    return False
