"""
Most frequently occurring integer in the array
"""


def most_frequent(array):
    # initialize a dictionary
    table = {}
    # maximum count so far
    max_count = 1 if len(array) != 0 else None
    # the most occurred number
    max_num = array[0] if len(array) != 0 else None
    # go through the array
    for num in array:
        # add to the table if not there
        if num not in table:
            table[num] = 1
        # otherwise
        else:
            # increment by 1 its counter
            table[num] += 1
            # if its counter hits the current max
            # update the max count and the most occurred number
            if table[num] > max_count:
                max_count = table[num]
                max_num = num
    return max_num, max_count

