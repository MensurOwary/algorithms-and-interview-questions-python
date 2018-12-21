"""
Binary search
"""


def binary(arr, searched):
    low = 0
    high = len(arr)
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] > searched:
            high = mid-1
        elif arr[mid] < searched:
            low = mid+1
        else:
            return True
    return False


# task is to find the closest
def binary_closest(arr, searched):
    low = 0
    high = len(arr)
    minix = None
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] > searched:
            high = mid-1
        elif arr[mid] < searched:
            low = mid+1
        else:
            return arr[mid]
        
        if minix is None:
            minix = mid
        elif abs(arr[mid] - searched) < abs(arr[minix] - searched):
            minix = mid
    return arr[minix]