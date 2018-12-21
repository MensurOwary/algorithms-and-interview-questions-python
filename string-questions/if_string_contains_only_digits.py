"""
Check if a String contains only digits
"""
import re


def check_only_digits(string):
    pattern = re.compile('^[0-9\s]+$')
    return pattern.match(string) is not None

