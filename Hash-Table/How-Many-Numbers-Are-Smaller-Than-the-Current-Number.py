from collections import Counter


def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    """
    ID: 1365
    Tags:   Array, Hash Table, Sorting, Counting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for
    each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

    Return the answer in an array.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out: list[int]

    Examples
    --------
    >>> smallerNumbersThanCurrent([8,1,2,2,3])
    [4, 0, 1, 1, 3]

    Explanation:
    For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
    For nums[1]=1 does not exist any smaller number than it.
    For nums[2]=2 there exist one smaller number than it (1).
    For nums[3]=2 there exist one smaller number than it (1).
    For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

    >>> smallerNumbersThanCurrent([6,5,4,8])
    [2, 1, 0, 3]

    >>> smallerNumbersThanCurrent([7,7,7,7])
    [0, 0, 0, 0]
    """
    nums_sorted = sorted(nums, reverse=True)
    counted = Counter(nums_sorted)
    nums_result = {}
    for num in nums_sorted:
        if num in nums_result:
            continue
        counted.pop(num, 0)
        nums_result[num] = sum(counted.values())
    return [nums_result[i] for i in nums]


