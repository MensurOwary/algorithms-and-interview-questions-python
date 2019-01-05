"""
Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from problem_solving import all_prime_factors as apf


def smallest_multiple(low, high):
    """
    Explanation:
    Take the first 2 numbers in the sequence, find their LCM and then find its LCM with the next number
    :param low: lower bound
    :param high: upper bound
    :return: the smallest multiple
    """
    li = range(low, high+1)
    a = li[0]
    b = li[1]
    for i in range(low+1, high):
        a = lcm(a, b)
        b = li[i]
    return a


def lcm(a, b):
    """
    Least common multiple
    :param a: a number
    :param b: another number
    :return: least common multiple of 2 numbers
    """
    # if they are equal, then return one of them
    if a == b:
        return a
    # a should be bigger than b
    # algorithm expects that, if otherwise, we swap them
    if b > a:
        a, b = b, a
    # get the prime factors of both numbers
    aprimes = apf.all_prime_factors(a)
    bprimes = apf.all_prime_factors(b)
    # go through all the elements of the bigger number
    for i in aprimes:
        # remove a number that exists in the factors of smaller number
        if i in bprimes:
            bprimes.remove(i)
    # total is the bigger number initially
    total = a
    # multiply remaining prime factors
    for el in bprimes:
        total *= el
    # return the result
    return total


if __name__ == "__main__":
    print(smallest_multiple(1, 20))