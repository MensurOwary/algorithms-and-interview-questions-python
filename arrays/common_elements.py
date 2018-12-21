def common_elements(one, two):
    # one is longer
    # make the one longer
    # two smaller
    if len(one) < len (two):
        one, two = two, one
    # pointer for the smaller array
    j = 0
    # final result
    result = []
    # traverse the longer list
    for i in one:
        # if pointer of two exceeds its limits
        # stop the loop
        if j >= len(two):
            break
        # if numbers are equal add it, increment the pointer
        if i == two[j]:
            result.append(i)
            j += 1
        # if number in one is bigger
        elif i > two[j]:
            # increment j until it's bigger or equal than the number in 'one'
            while i > two[j]:
                j += 1
            # if now they are equal, append it to the array
            if i == two[j]:
                result.append(i)
                j += 1
    # return
    return result


def common_elements_v2(one, two):
    # one is longer
    if len(one) < len (two):
        one, two = two, one
    # basic idea
    # put the elements of the smaller to the dictionary with nums as keys
    # whilst traversing the bigger one, check if the num exists in the dictionary
    # if yes, add it to the list
    # since lookup is O(1) that shouldn't be a problem
    table = {}
    for num in two:
        table[num] = 0
    result = []
    for num in one:
        if num in table:
            result.append(num)
    return result


def common_elements_v3(one, two):
    # basic idea
    # 2 pointers, each pointing to an array
    # until one of them has reached the end-of-array
    # if the elements they're pointing to are equal add num to the list and increment both
    # if one of them is bigger, increment the pointer of the other by 1
    result = []
    j = i = 0
    while j != len(one) and i != len(two):
        if one[j] == two[i]:
            result.append(one[j])
            j += 1
            i += 1
        elif one[j] > two[i]:
            i += 1
        elif one[j] < two[i]:
            j += 1
    return result

