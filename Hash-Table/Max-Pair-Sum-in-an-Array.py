from collections import defaultdict

def maxSum(nums: list[int]) -> int:
    """
    ID: 2815
    Tags:   Array, Hash Table
    Time:   O(Nlogn)
    Memory: O(N)

    Task
    ----------
    You are given an integer array nums. You have to find the maximum sum of a pair of numbers from
    nums such that the largest digit in both numbers is equal.

    For example, 2373 is made up of three distinct digits: 2, 3, and 7, where 7 is the largest among
    them.

    Return the maximum sum or -1 if no such pair exists.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> maxSum([112,131,411])
    -1

    Explanation: Each numbers largest digit in order is [2,3,4].

    >>> maxSum([2536,1613,3366,162])
    5902

    All the numbers have 6 as their largest digit, so the answer is 2536 + 3366 = 5902.

    >>> maxSum([51,71,17,24,42])
    88

    Each number's largest digit in order is [5,7,7,4,4].
    So we have only two possible pairs, 71 + 17 = 88 and 24 + 42 = 66.
    """
    max_dig = 0
    d = defaultdict(list)
    for num in nums:
        dig = max_digit(num)
        max_dig = max(max_dig, dig)
        d[dig].append(num)
    sums = []
    for k in sorted(d.keys())[::-1]:
        ans = d[k]
        if len(ans) < 2:
            continue
        v1 = max(ans)
        ans.remove(v1)
        sums.append(v1 + max(ans))
    return max(sums) if sums else -1


def max_digit(num: int) -> int:
    ans = 0
    while True:
        s_dig = num % 10
        ans = max(s_dig, ans)
        num //= 10
        if num == 0:
            break
    return ans