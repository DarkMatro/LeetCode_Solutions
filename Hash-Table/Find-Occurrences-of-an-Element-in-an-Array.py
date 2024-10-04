def occurrencesOfElement(nums: list[int], queries: list[int], x: int) -> list[int]:
    """
    ID: 442
    Tags:   Array, Hash Table
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given an integer array nums, an integer array queries, and an integer x.

    For each queries[i], you need to find the index of the queries[i]th occurrence of x in the nums
    array. If there are fewer than queries[i] occurrences of x, the answer should be -1 for that
    query.

    Return an integer array answer containing the answers to all queries.

    Parameters
    ----------
    nums: list[int]

    queries: list[int]

    x: int

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> occurrencesOfElement([1,3,1,7], [1,3,2,4], 1)
    [0, -1, 2, -1]

    Explanation:

    For the 1st query, the first occurrence of 1 is at index 0.
    For the 2nd query, there are only two occurrences of 1 in nums, so the answer is -1.
    For the 3rd query, the second occurrence of 1 is at index 2.
    For the 4th query, there are only two occurrences of 1 in nums, so the answer is -1.

    >>> occurrencesOfElement([1,2,3], [10], 5)
    [-1]

    Explanation: For the 1st query, 5 doesn't exist in nums, so the answer is -1.
    """
    cnt = {}
    occur = 1
    for i, num in enumerate(nums):
        if num == x:
            cnt[occur] = i
            occur += 1
    n = len(cnt)
    return [-1 if q > n else cnt[q] for q in queries]
