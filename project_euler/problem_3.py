"""
Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from math import sqrt


def largest_prime_factor(n):
    """
    Explanation:
    We do basic trial method, but preserve just the largest
    :param n: the number
    :return: the largest prime factor
    """
    # initial largest is zero
    largest = 0
    # we divide the number to 2 until it is an odd number
    # while doing so, we remove all the even divisors, if it has any
    while n % 2 == 0:
        n = n // 2
        largest = 2
    # since it has no even divisors, we start from 3 and continue until
    # square root of the remaining part
    # step size is 2, because it has no even divisors
    for i in range(3, round(sqrt(n)), 2):
        # we divide the number to i until it is no more divisible
        while n % i == 0:
            n = n // i
            # save the largest factor
            if largest < i:
                largest = i
    # if number is prime itself
    # largest is the number itself
    if n > 2:
        largest = n
    # return it
    return largest


if __name__ == '__main__':
    print(largest_prime_factor(600851475143))
