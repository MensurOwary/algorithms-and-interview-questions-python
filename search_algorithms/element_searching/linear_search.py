def linear_search(arr, searched):
    for i in range(len(arr)):
        if searched == arr[i]:
            return i
    return -1


def linear_closest(arr, searched):
    minix = arr[0]
    for el in arr:
        if abs(el-searched) < abs(minix-searched):
            minix = el
    return minix