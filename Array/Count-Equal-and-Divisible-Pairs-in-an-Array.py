def countPairs(nums: list[int], k: int) -> int:
    """
    ID: 2176
    Tags:   Array
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j)
    where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.

    Parameters
    ----------
    nums : list[int]

    k: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> countPairs([3,1,2,2,2,1,3], 2)
    4

    Explanation:
    There are 4 pairs that meet all the requirements:
    - nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
    - nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
    - nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
    - nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.

    >>> countPairs([1,2,3,4], 1)
    0

    Explanation: Since no value in nums is repeated, there are no pairs (i,j) that meet all the requirements.

    """
    n_pairs = 0
    d = {}
    for i, num in enumerate(nums):
        if num in d:
            d[num].append(i)
        else:
            d[num] = [i]
    for idx_list in d.values():
        for i in range(len(idx_list)):
            for j in range(i + 1, len(idx_list)):
                if (idx_list[i] * idx_list[j]) % k == 0:
                    n_pairs += 1
    return n_pairs
