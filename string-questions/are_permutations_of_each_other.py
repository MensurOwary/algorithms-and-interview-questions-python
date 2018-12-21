"""
Check if strings are permutations of each other
"""


def are_permutations(str1, str2):
    """
    Algorithm:
    1. Loop over the first string's chars
    2. Register each of them in a dictionary and count
    3. Loop over the other string's chars
    4. If any char doesn't exist return False, cuz it cannot be permutation then
       Otherwise, decrement the value of the corresponding key
    5. Loop over the dictionary and check if all the values are 0
        If any of them is non-zero, stop and return False
        If finish loop, return True
    :param str1: string to check
    :param str2: other string to check
    :return: if they are permutations of each other
    """
    if len(str1) != len(str2):
        return False
    seen = {}
    for ch in str1:
        if ch not in seen:
            seen[ch] = 1
        else:
            seen[ch] += 1
    for ch in str2:
        if ch not in seen:
            return False
        else:
            seen[ch] -= 1
    for k, v in seen.items():
        if v != 0:
            return False
    return True

