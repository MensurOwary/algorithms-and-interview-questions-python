"""
Numbers in a set that add up to target
"""


def number_of_sets(array, target, st):
    if target == 0:
        return 1
    elif st == len(array) and target != 0:
        return 0
    else:
        tmp1 = number_of_sets(array, target-array[st], st+1)
        tmp2 = number_of_sets(array, target, st+1)
        return tmp1+tmp2


def actual_of_sets(array, target, st, answer):
    if target == 0:
        return set()
    elif st == len(array) and target != 0:
        return None
    else:
        new_answer = answer.copy().add(array[st])
        tmp1 = actual_of_sets(array, target-array[st], st+1, new_answer)
        tmp2 = actual_of_sets(array, target, st+1, answer.copy())
        return set(tmp1, tmp2)