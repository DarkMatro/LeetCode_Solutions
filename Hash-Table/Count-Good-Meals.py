from collections import Counter


def countPairs(deliciousness: list[int]) -> int:
    """
    ID: 1711
    Tags:   Array, Hash Table
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    A good meal is a meal that contains exactly two different food items with a sum of deliciousness
    equal to a power of two.

    You can pick any two different foods to make a good meal.

    Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the
    ith item of food, return the number of different good meals you can make from this list modulo
    10^9 + 7.

    Note that items with different indices are considered different even if they have the same
    deliciousness value.

    Parameters
    ----------
    deliciousness: list[int]

    Returns
    -------
    int

    Examples
    --------
    >>> countPairs([1,3,5,7,9])
    4

    Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
    Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.

    >>> countPairs([1,1,1,3,3,3,7])
    15

    Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.
    """
    cnt = Counter(deliciousness)
    powers = [2 ** x for x in range(22) if 2 ** x <= max(cnt.keys()) * 2]
    ans = 0
    for k, v in cnt.items():
        for p in powers:
            pk = p - k
            if pk <= k and pk in cnt:
                ans += v * (v - 1) // 2 if pk == k else v * cnt[pk]
    return ans % 1_000_000_007
