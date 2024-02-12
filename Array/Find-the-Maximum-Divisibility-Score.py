from collections import Counter


def maxDivScore(nums: list[int], divisors: list[int]) -> int:
    """
    ID: 2644
    Tags:   Array
    Time:   O(N * D)
    Memory: O(N)

    Task
    ----------
    You are given two 0-indexed integer arrays nums and divisors.

    The divisibility score of divisors[i] is the number of indices j such that nums[j] is divisible by divisors[i].

    Return the integer divisors[i] with the maximum divisibility score. If there is more than one integer with the
    maximum score, return the minimum of them.

    Parameters
    ----------
    nums : list[int]

    divisors: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> maxDivScore([4,7,9,3,9], [5,2,3])
    3

    Explanation: The divisibility score for every element in divisors is:
    The divisibility score of divisors[0] is 0 since no number in nums is divisible by 5.
    The divisibility score of divisors[1] is 1 since nums[0] is divisible by 2.
    The divisibility score of divisors[2] is 3 since nums[2], nums[3], and nums[4] are divisible by 3.
    Since divisors[2] has the maximum divisibility score, we return it.

    >>> maxDivScore([20,14,21,10], [5,7,5])
    5

    Explanation: The divisibility score for every element in divisors is:
    The divisibility score of divisors[0] is 2 since nums[0] and nums[3] are divisible by 5.
    The divisibility score of divisors[1] is 2 since nums[1] and nums[2] are divisible by 7.
    The divisibility score of divisors[2] is 2 since nums[0] and nums[3] are divisible by 5.
    Since divisors[0], divisors[1], and divisors[2] all have the maximum divisibility score, we return the minimum of
    them (i.e., divisors[2]).

    >>> maxDivScore([12], [10,16])
    10

    Explanation: The divisibility score for every element in divisors is:
    The divisibility score of divisors[0] is 0 since no number in nums is divisible by 10.
    The divisibility score of divisors[1] is 0 since no number in nums is divisible by 16.
    Since divisors[0] and divisors[1] both have the maximum divisibility score, we return the minimum of them (i.e.,
    divisors[0]).

    >>> maxDivScore([73,13,20,6], [56,75,83,26,24,53,56,61])
    24

    >>> maxDivScore([31,91,47,6,37,62,72,42,85], [95,10,8,43,21,63,26,45,23,69,16,99,92,5,97,69,33,44,8])
    5

    >>> maxDivScore([39,70,33], [27,73,37,31,28,82,96,12,31,77,17,83,19,46,7,4,74,70,66,73,25,50,79])
    7
    """
    nums = Counter(nums)

    max_nums = max(nums) + 1

    max_ans = 0
    ans = 1_000_000_000

    for divisor in divisors:
        c = 0
        for a in range(0, max_nums, divisor):
            if a in nums:
                c += nums[a]
        if c == max_ans:
            ans = min(ans, divisor)
        elif c > max_ans:
            max_ans = c
            ans = divisor
    return ans
