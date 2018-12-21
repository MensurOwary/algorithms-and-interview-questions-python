import math


def prime_nums_upto(n):
    """
    Prime numbers up to given n
    :param n:
    :return:
    """
    # list to store primes
    primes = []
    # flag to show if divisible
    divisible = False
    # start from 2 up to n
    for i in range(2, n+1):
        # if the current number is divisible by any of
        # already seen primes
        # then skip that number
        for j in primes:
            if i % j == 0:
                divisible = True
                break
        # otherwise add it to the list
        if not divisible:
            primes.append(i)
        divisible = False
    # return
    return primes


def sieve_of_eratosthenes(n):
    """
    Sieve of Eratosthenes
    :param n: number
    :return: prime numbers up to n
    """
    # the sieve that marks non-prime nums as False
    # initially, we have an array of n+1 True entries
    # reason for n+1 is that when I access sieve[n],
    # I want to access the state of that n
    # so the first 2 entries aren't important [0 and 1]
    sieve = [True] * (n+1)
    # define upper bound
    # upper bound is square root of the number
    # because, the non-prime numbers up to n, are divisible by numbers up to square root
    upper = int(math.sqrt(n))+1
    # loop from 2 until upper bound
    for i in range(2, upper):
        # if number is not marked as non-prime
        if sieve[i]:
            # mark the rest as non-prime
            # we do it by hopping over entries by step size of i
            # and start from i + i because ith number is prime
            for j in range(i+i, n+1, i):
                sieve[j] = False
    # store primes
    primes = []
    # if entry is True, return add its index to the array
    for i in range(2, n+1):
        if sieve[i]:
            primes.append(i)
    # return the answer
    return primes


