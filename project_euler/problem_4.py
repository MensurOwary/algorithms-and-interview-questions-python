"""
Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def largest_palindrome_product_of_n_digits(n):
    # minimum and maximum bounds of n-digit numbers
    low, high = get_high_low(n)
    # largest palindrome variable
    mx = -1
    # start from the biggest numbers and proceed until the end
    for i in range(high, low, -1):
        for j in range(high, i, -1):
            # term is the multiplication of i and j
            term = i * j
            # if that number is a palindrome and larger than the previous max
            # then make it the new one
            if is_palindrome(term) and mx < term:
                mx = term
    # return max
    return mx


def is_palindrome(n):
    nums = []
    while n != 0:
        nums.append(n % 10)
        n = n // 10
    i = 0
    j = len(nums) - 1
    while i <= j:
        if nums[i] == nums[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


def get_high_low(n):
    high = 0
    mult = 1
    for i in range(n):
        high += mult * 9
        mult *= 10
    return mult//10, high


if __name__ == '__main__':
    print(largest_palindrome_product_of_n_digits(3))