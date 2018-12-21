"""
Return the power set - set of all subsets
Power set of {1, 2} -> {  {}, {1}, {2}, {1, 2}  }
"""


def power_set(inp_set):
    """
    The algorithm:
    The power set can be calculated as follows:
    Let's say the size of given set is n
    Then there are 2^n elements in the power set.
    Those elements can be represented via binary numbers from 0 up to 2^n
    So let's say, the set is {1, 2}
    Total count is 2^2 = 4, hence there're 4 elements in the power set
    Those combinations can be represented using binary numbers:
    dec - bin - set
    0 - 00 - {} - none is selected
    1 - 01 - {2} - 2 is the second element
    2 - 10 - {1} - 1 is the first element
    3 - 11 - {1, 2} - both are selected
    :param inp_set: input set
    :return: power set of the input
    """
    # total number of elements
    size = 2**len(inp_set)
    # power set initialization
    powerset = set()
    # from 0 to the total size
    for i in range(size):
        # convert the num to binary
        # return the corresponding subset - tuple
        # add it to the power set
        powerset.add(subset(bin(i), inp_set))
    # return powerset
    return powerset


# find the corresponding subset
def subset(binary, the_set):
    # initial list
    _set = []
    # since the binary output of bin function is of form '0b[real output]'
    # we have to skip the first 2
    for i in range(2, len(binary)):
        # if the number is 1 (on)
        # add the corresponding element to the list
        if binary[i] == '1':
            _set.append(the_set[i-2])
    # return the tuple
    return tuple(_set)

