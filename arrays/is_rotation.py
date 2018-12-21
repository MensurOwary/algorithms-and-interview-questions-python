def is_rotation(one, two):
    # check if they are equi-length
    if len(one) != len(two):
        return False
    # pointer to the first same character in second array
    i = 0
    # look for the first same element
    while i < len(two) and one[0] != two[i]:
        i += 1
    # if it is not present, return False
    if i >= len(two):
        return False
    # otherwise
    # start from the first character
    # move through
    for ch in one:
        # if those chars aren't the same
        # return false, since they aren't rotations
        if two[i] != ch:
            return False
        # move the pointer
        i += 1
        # if it exceeds the limits
        # return it to the beginning
        if i >= len(two):
            i = 0
    # return true if successfully reached end
    return True

