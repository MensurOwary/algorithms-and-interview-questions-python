def is_narcissistic(num):
    """
    Narcissistic number is a number where num is equal to the summation of digits raised to the power of digit count
    :param num: number to check
    :return: if it is narcissistic
    """
    c = digit_count(num)
    sum = 0
    save = num
    while num != 0:
        digit = num % 10
        num = num // 10
        sum += digit**c
    return sum == save


def digit_count(num):
    c = 0
    while num != 0:
        num = num // 10
        c += 1
    return c