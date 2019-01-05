"""
Check if number is palindrome
"""


def is_palindrome(num):
    """
    Algorithm:
    Extract each digit out of number
    Check if nth and (len-n)th digits are equal
    :param num: num to be checked for being palindrome
    :return: if it is palindrome
    """
    digits = []
    while num != 0:
        mod = num % 10
        digits.append(mod)
        num = num // 10  # integer division
    l = len(digits)-1
    for i in range(1+l//2):
        if digits[i] != digits[l-i]:
            return False
    return True
