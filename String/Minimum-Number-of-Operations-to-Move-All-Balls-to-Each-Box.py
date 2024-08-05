from itertools import accumulate

def minOperations(boxes: str) -> list[int]:
    """
    ID: 1769
    Tags:   String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the
    ith box is empty, and '1' if it contains one ball.

    In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box
    j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

    Return an array answer of size n, where answer[i] is the minimum number of operations needed to
    move all the balls to the ith box.

    Each answer[i] is calculated considering the initial state of the boxes.

    Parameters
    ----------
    boxes : str

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> minOperations("110")
    [1, 1, 3]

    Explanation: The answer for each box is as follows:
    1) First box: you will have to move one ball from the second box to the first box in one
    operation.
    2) Second box: you will have to move one ball from the first box to the second box in one
    operation.
    3) Third box: you will have to move one ball from the first box to the third box in two
    operations, and move one ball from the second box to the third box in one operation.
    Example 2:

    >>> minOperations("001011")
    [11, 8, 5, 4, 3, 4]
    """
    bxs = [int(x) for x in boxes]
    count_add = list(accumulate(bxs, func=lambda x, y: x + 1 if y else x))[:-1]
    count = [0]
    count.extend(count_add)
    left_cost = list(accumulate(count))
    count = list(accumulate(bxs[-1::-1], func=lambda x, y: x + 1 if y else x))[:-1]
    right_cost = list(accumulate(count))[-1::-1]
    right_cost.append(0)
    for i, x in enumerate(right_cost):
        left_cost[i] += x
    return left_cost
