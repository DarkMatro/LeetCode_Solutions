from collections import defaultdict


def majority_element(nums: list[int]) -> int:
    """
    ID: 0169
    Tags:   Array, Hash Table, Divide and Conquer, Sorting, Counting
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
    always exists in the array.


    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    majority element : int

    Examples
    --------
    >>> majority_element([3,2,3])
    3

    >>> majority_element([2,2,1,1,1,2,2])
    2
    """
    n = len(nums)
    m = defaultdict(int)

    for num in nums:
        m[num] += 1

    n = n // 2
    for key, value in m.items():
        if value > n:
            return key

    return 0
