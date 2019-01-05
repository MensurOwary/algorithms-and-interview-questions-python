"""
10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import math


def nth_prime(n):
    guess = -1
    x = 1
    while guess < n:
        guess = count_of_primes(x)
        x *= 10
    for i in range(x, 0, -1):
        if is_prime(i):
            if guess == n:
                return i
            guess -= 1


def count_of_primes(x):
    return x


def is_prime(num):
    up = math.ceil(math.sqrt(num))
    for i in range(2, up):
        if num % i == 0:
            return False
    return True