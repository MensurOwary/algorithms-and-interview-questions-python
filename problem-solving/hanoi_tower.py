"""
Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following
constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.
"""


def hanoi(start, temp, dest, n):
    """
    Trick:
    The trick to solving this puzzle is to think recursively. Instead of trying to solve the entire
    puzzle all at once, let’s concentrate on moving just the largest disk. We can’t move it at the beginning,
    because all the other disks are covering it; we have to move those n − 1 disks to the
    third peg before we can move the nth disk. And then after we move the nth disk, we have to
    move those n − 1 disks back on top of it.
    :param start: Start label
    :param temp: Temporary label
    :param dest: Destination
    :param n: Number of pegs
    :return: print the steps
    """
    if n > 0:
        hanoi(start, dest, temp, n-1)
        print('Move {:d} from {} to {}'.format(n, start, dest))
        hanoi(temp, start, dest, n-1)

