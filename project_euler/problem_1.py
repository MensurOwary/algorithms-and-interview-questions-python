"""
Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multiples_of_3_and_5(n):
    """
    Explanation:
    Nums divisible by 3  |   Nums divisible by 5  |   Difference
    0       |   0       |   +0
    3       |   5       |   +2
    6       |   10      |   +4
    9       |   15      |   +6
    12      |   20      |   +8
    15      |   25      |   +10
    18      |   30      |   +12

    As we can see the difference is increasing by 2, so we only need to loop through three's divisors and then
    add the difference to it and increase the difference by 2

    :param n: upper bound
    :return: the sum
    """
    total = 0
    diff = 0
    for i in range(0, n+1, 3):
        five = i + diff
        total += i
        if five <= n and five % 3 != 0:
            total += five
        diff += 2
    return total


def multiples_of_3_and_5_math(n):
    th = arithmetic_progression(0, n, 3)
    fv = arithmetic_progression(0, n, 5)
    ft = arithmetic_progression(0, n, 15)
    return th + fv - ft


def arithmetic_progression(low, high, diff):
    a1 = ((low // diff) + 1) * diff
    an = (high // diff) * diff
    n = ((an - a1) // diff) + 1
    return (a1 + an) * n // 2


if __name__ == '__main__':
    print("Using a loop", multiples_of_3_and_5(1000))
    print("Using arithmetic progression", multiples_of_3_and_5_math(1000))
