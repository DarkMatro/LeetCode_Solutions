def countOdds(low: int, high: int) -> int:
    """
    ID: 1523
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Given two non-negative integers low and high. Return the count of odd numbers between low and
    high (inclusive).

    Parameters
    ----------
    low: int

    high: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> countOdds(3, 7)
    3

    Explanation: The odd numbers between 3 and 7 are [3,5,7].

    >>> countOdds(8, 10)
    1

    Explanation: The odd numbers between 8 and 10 are [9].
    """
    ans = (high - low) // 2
    if high % 2 != 0 or low % 2:
        ans += 1
    return ans
