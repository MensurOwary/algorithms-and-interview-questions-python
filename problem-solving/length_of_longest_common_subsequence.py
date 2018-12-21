"""
Length of longest common sub-sequence (not contiguous)
"""


def lcs(A, B):
    """
    Algorithm is as follows
    if A and B's first elements are equal, we count it as 1 and
    proceed with the next elements in each
    if they aren't equal
    - take the whole A array and B array after the next element
    - take the whole B array and A array after the next element
    - take the maximum of previous 2
    :param A: First array
    :param B: Second array
    :return: length of longest common sub-sequence
    """
    if len(A) == 0 or len(B) == 0:
        return 0
    if A[0] == B[0]:
        return 1 + lcs(A[1:], B[1:])
    else:
        return max(lcs(A, B[1:]), lcs(A[1:], B))