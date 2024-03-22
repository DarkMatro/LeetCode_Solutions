from math import ceil


def maxDistToClosest(seats: list[int]) -> int:
    """
    ID: 0849
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat,
    and seats[i] = 0 represents that the ith seat is empty (0-indexed).

    There is at least one empty seat, and at least one person sitting.

    Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

    Return that maximum distance to the closest person.

    Parameters
    ----------
    seats : list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> maxDistToClosest([1,0,0,0,1,0,1])
    2

    Explanation:
    If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
    If Alex sits in any other open seat, the closest person has distance 1.
    Thus, the maximum distance to the closest person is 2.

    >>> maxDistToClosest([1,0,0,0])
    3

    Explanation:
    If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
    This is the maximum distance possible, so the answer is 3.

    >>> maxDistToClosest([0,1])
    1

    >>> maxDistToClosest([0,0,1])
    2
    """
    ans, dist = 0, seats.index(1)
    for seat in seats:
        if seat:
            ans, dist = max(ans, ceil(dist / 2)), 0
        else:
            dist += 1
    return max(dist, ans)
