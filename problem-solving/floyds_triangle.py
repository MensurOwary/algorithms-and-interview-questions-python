def floyds_triangle(n):
    i = 1  # maximum number of elements in each row
    j = 0  # counter to check if reached the max element count in row
    k = 1  # printed numbers
    # if count of elements in row
    # are less than or equal to n
    # proceed
    while i <= n:
        # print the number
        print(str(k), end=' ')
        # increment the counter
        j += 1
        # if reached the limit
        if i == j:
            print()
            i += 1
            j = 0
        k += 1