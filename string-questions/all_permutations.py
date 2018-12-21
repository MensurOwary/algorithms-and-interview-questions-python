"""
Find all permutations of String?

version 1 : https://i.stack.imgur.com/KkDTf.png
version 2 : https://i.stack.imgur.com/yrTFw.gif

"""
import time

seen = set()
seen_v2 = set()
seen_v3 = set()


# version 1
def permutation(string, st, end):
    # if reached end, finish
    if st > end:
        return
    # so the logic is to swap characters while keeping the ones
    # before 'st' index untouched
    for i in range(st, end):
        # new copy of string
        copy = string.copy()
        # swap st and i index characters
        copy[st], copy[i] = copy[i], copy[st]
        # add the string to the 'seen' set
        seen.add(''.join(copy))
        # proceed
        permutation(copy, st+1, end)


# version 1, wrapper
def permute(string):
    # to measure the timing
    st = time.time()
    # permutation call
    permutation(list(string), 0, len(string))
    # end time
    end = time.time()
    # print the set
    print(seen)
    # print the total time
    print('Total_v1 :', str(end - st))


# version 2 permutation
def permutation_v2(string, st, end):
    # if string length is equal to total number of characters
    if st == end:
        # add it to the set
        seen_v2.add(''.join(string))
    # otherwise
    else:
        # idea is as follows, keep the elements
        # indices less then 'st' untouched
        for i in range(st, end):
            # swap 'st' and 'i' indexed characters
            string[st], string[i] = string[i], string[st]
            # permute
            permutation_v2(string, st+1, end)
            # swap 'st' and 'i' indexed characters
            string[st], string[i] = string[i], string[st]


# wrapper of version 2
def permute_v2(string):
    st = time.time()
    permutation_v2(list(string), 0, len(string))
    end = time.time()
    print(seen_v2)
    print('Total_v2 :', str(end-st))


# version 3 of permutations
def permutation_v3(unchosen, chosen, already_seen):
    # if empty left, then add the chosen one to the set
    if len(unchosen) == 0:
        already_seen.add(''.join(chosen))
    # otherwise
    else:
        # go through all the letters
        for i, ch in enumerate(unchosen):
            # choose the letter and add it to the chosen list
            chosen.append(ch)
            # remove it from unchosen
            unchosen.pop(i)
            # permute the rest with new chosen and unchosen pair
            permutation_v3(unchosen.copy(), chosen.copy(), already_seen)
            # un-choose what we did previously
            # add it to wherever it belongs
            unchosen.insert(i, ch)
            # remove it from chosen
            chosen.pop()


# wrapper of version 3
def permute_v3(string):
    st = time.time()
    permutation_v3(list(string), [], seen_v3)
    end = time.time()
    print(seen_v3)
    print('Total_v2 :', str(end-st))