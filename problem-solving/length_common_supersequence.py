def scs(A, B):
    """
    Algorithm is as follows
    if one of the arrays are empty return the length of the other one
    if A and B's first elements are equal, we count it as 1 and
    proceed with the next elements in each
    if they aren't equal
    - take the whole A array and B array after the next element
    - take the whole B array and A array after the next element
    - take the minimum of previous 2
    - add 1 to the minimum, because not-common letter still counts
    :param A: First array
    :param B: Second array
    :return: length of shortest common super-sequence
    """
    if len(A) == 0:
        return len(B)
    if len(B) == 0:
        return len(A)
    if A[0] == B[0]:
        return 1 + scs(A[1:], B[1:])
    else:
        return 1 + min(scs(A, B[1:]), scs(A[1:], B))