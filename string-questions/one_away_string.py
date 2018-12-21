"""
One away string
It means if two strings are 1 edit away
1 edit - add, delete, change letter to other letter (even itself)
"""


def one_away_string(st1, st2):
    if abs(len(st1) - len(st2)) > 1:
        return False
    if st1 == st2:
        return True
    if len(st1) < len(st2):
        st1, st2 = st2, st1
    dictionary = {}
    for ch in st1:
        if ch not in dictionary:
            dictionary[ch] = 1
        else:
            dictionary[ch] += 1

    for ch in st2:
        if ch in dictionary:
            dictionary[ch] -= 1

    one_count = 0
    for k, v in dictionary.items():
        if v == 1:
            one_count += 1
    return one_count == 1


def one_away_string_v2(st1, st2):
    if abs(len(st1) - len(st2)) > 1:
        return False
    if st1 == st2:
        return True
    if len(st1) == len(st2):
        pass_for_once = 0
        for i in range(len(st1)):
            if st1[i] != st2[i]:
                pass_for_once += 1
        if pass_for_once == 1:
            return True
        else:
            return False
    if len(st1) < len(st2):
        st1, st2 = st2, st1
    j = 0
    pass_for_once = 0
    for ch in st1:
        if ch != st2[j]:
            pass_for_once += 1
            if pass_for_once > 1:
                return False
            continue
        j += 1
    if pass_for_once == 1:
        return True
    else:
        return False
