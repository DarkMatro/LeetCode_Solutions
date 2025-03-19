def maxConsecutive(bottom: int, top: int, special: list[int]) -> int:
    """
    ID: 2274
    Tags:   Array, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    Alice manages a company and has rented some floors of a building as office space. Alice has
    decided some of these floors should be special floors, used for relaxation only.

    You are given two integers bottom and top, which denote that Alice has rented all the floors
    from bottom to top (inclusive). You are also given the integer array special, where special[i]
    denotes a special floor that Alice has designated for relaxation.

    Return the maximum number of consecutive floors without a special floor.

    Parameters
    ----------
    bottom: int

    top: int

    special: list[int]

    Returns
    -------
    int

    Examples
    --------
    >>> maxConsecutive(2, 9, [4,6])
    3

    Explanation: The following are the ranges (inclusive) of consecutive floors without a special
    floor:
    - (2, 3) with a total amount of 2 floors.
    - (5, 5) with a total amount of 1 floor.
    - (7, 9) with a total amount of 3 floors.
    Therefore, we return the maximum number which is 3 floors.

    >>> maxConsecutive(6, 8, [7,6,8])
    0

    Explanation: Every floor rented is a special floor, so we return 0.
    """
    if top - bottom == len(special) - 1:
        return 0
    special.sort()
    ans = 0
    prev = special[0]
    ans = max(ans, prev - bottom, top - special[-1])
    for i, s in enumerate(special):
        if i == 0:
            continue
        ans = max(ans, s - prev - 1)
        prev = s
    return ans
