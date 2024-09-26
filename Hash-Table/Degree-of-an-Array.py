from collections import Counter


def findShortestSubArray(nums: list[int]) -> int:
    """
    ID: 697
    Tags:   Array, Hash Table
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given a non-empty array of non-negative integers nums, the degree of this array is defined as
    the maximum frequency of any one of its elements.

    Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has
    the same degree as nums.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> findShortestSubArray([1,2,2,3,1])
    2

    Explanation: The input array has a degree of 2 because both elements 1 and 2 appear twice.
    Of the subarrays that have the same degree:
    [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
    The shortest length is 2. So return 2.

    >>> findShortestSubArray([1,2,2,3,1,4,2])
    6

    Explanation: The degree is 3 because the element 2 is repeated 3 times.
    So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
    """
    cnt = Counter(nums)
    degree = max(cnt.values())
    elements = {k for k, v in cnt.items() if v == degree}
    ans = len(nums)
    d = {}
    for i, num in enumerate(nums):
        if not num in elements:
            continue
        if num in d:
            d[num].append(i)
        else:
            d[num] = [i]
    for idxs in d.values():
        ans = min(ans, idxs[-1] - idxs[0] + 1)
    return ans
