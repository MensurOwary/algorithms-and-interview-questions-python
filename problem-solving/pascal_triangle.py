def pascal_triangle(n):
    list = [1]
    for i in range(n):
        print_sequence(list, n)
        print()
        list = extend_list(list)


def extend_list(list):
    l = len(list)
    new = []
    for i in range(-1, l):
        a = list[i] if l > i > -1 else 0
        b = list[i+1] if (i+1) < l else 0
        new.append(a + b)
    return new


def print_sequence(list, n):
    l = len(list)
    total_len = 4*n - 3
    curr_width = 4*l - 3
    pad = (total_len - curr_width) // 2
    for i in range(pad):
        print(' ', end='')
    for el in list:
        print("{:^4d}".format(el), end=' ')



