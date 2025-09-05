def minimumAverage(nums: list[int]) -> float:
    """
    ID: 3194
    Tags:   Array, Two Pointers, Sorting
    Time:   O(nlogn)
    Memory: O(n)

    Task
    ----------
    You have an array of floating point numbers averages which is initially empty. You are given an array nums of n
    integers where n is even.

    You repeat the following procedure n / 2 times:

    Remove the smallest element, minElement, and the largest element maxElement, from nums.
    Add (minElement + maxElement) / 2 to averages.
    Return the minimum element in averages.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : float

    Examples
    --------
    >>> minimumAverage([7,8,3,4,15,13,4,1])
    5.5

    Explanation:
    step	nums	averages
    0	[7,8,3,4,15,13,4,1]	[]
    1	[7,8,3,4,13,4]	[8]
    2	[7,8,4,4]	[8,8]
    3	[7,4]	[8,8,6]
    4	[]	[8,8,6,5.5]
    The smallest element of averages, 5.5, is returned.

    >>> minimumAverage([1,9,8,3,10,5])
    5.5

    Explanation:
    step	nums	averages
    0	[1,9,8,3,10,5]	[]
    1	[9,8,3,5]	[5.5]
    2	[8,5]	[5.5,6]
    3	[]	[5.5,6,6.5]

    >>> minimumAverage([1,2,3,7,8,9])
    5.0

    Explanation:
    step	nums	averages
    0	[1,2,3,7,8,9]	[]
    1	[2,3,7,8]	[5]
    2	[3,7]	[5,5]
    3	[]	[5,5,5]
    """
    nums.sort()
    n = len(nums) // 2
    averages = []
    lp = 0
    rp = len(nums) - 1
    for _ in range(n):
        averages.append((nums[lp] + nums[rp]) / 2)
        lp += 1
        rp -= 1
    return min(averages)
