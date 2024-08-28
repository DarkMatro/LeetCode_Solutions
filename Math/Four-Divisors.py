def sumFourDivisors(nums: list[int]) -> int:
    """
    ID: 1390
    Tags:   Array, Math
    Time:   O(Nsqrt(N))
    Memory: O(N)

    Task
    ----------
    Given an integer array nums, return the sum of divisors of the integers in that array that have
    exactly four divisors. If there is no such integer in the array, return 0.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> sumFourDivisors([21,4,7])
    32

    Explanation: 21 has 4 divisors: 1, 3, 7, 21
    4 has 3 divisors: 1, 2, 4
    7 has 2 divisors: 1, 7
    The answer is the sum of divisors of 21 only.

    >>> sumFourDivisors([21, 21])
    64

    >>> sumFourDivisors([1,2,3,4,5])
    0
    """
    total_sum = 0
    for num in nums:
        divisors = get_divisors(num)
        if len(divisors) == 4:
            total_sum += sum(divisors)
    return total_sum

def get_divisors(n: int) -> list[int]:
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
        if len(divisors) > 4:  # Early exit if more than 4 divisors
            return []
    return list(divisors) if len(divisors) == 4 else []
