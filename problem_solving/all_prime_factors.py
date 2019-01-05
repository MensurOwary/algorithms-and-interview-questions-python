"""
Find all the prime factors of a number
"""
import math


def all_prime_factors(num):
    """
    Algorithm here is Trial Division
    :param num: num to be prime factorized
    :return: prime factors of the number
    """
    # list to store the factors
    prime_factors = []
    # take the upper bound as square root of the given number
    # because it won't be bigger than that
    upper = int(math.sqrt(num)) + 1
    # if number is divisible by 2, keep dividing
    # whilst doing it, append 2 to the list
    # until it is no longer divisible by 2
    while num % 2 == 0:
        prime_factors.append(2)
        num = num // 2
    # after finishing division by 2
    # check if the number is finished, if yes return the factors
    if num == 0:
        return prime_factors
    # if there exists more
    # start from 3 (because the next prime number is 3) and step is 2, because
    # we no longer encounter even numbers
    # until upper bound, continue
    for i in range(3, upper, 2):
        # for each number
        # divide the number to that, if divisible
        # and append it to the list
        while num % i == 0:
            prime_factors.append(i)
            num = num // i
    # if number is prime itself. since it won't be divided to any number, it will stay as it is
    if num > 2:
        prime_factors.append(num)
    # after finishing return the list
    return prime_factors
