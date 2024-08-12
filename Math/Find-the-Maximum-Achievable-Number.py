def theMaximumAchievableX(num: int, t: int) -> int:
    """
    ID: 2769
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Given two integers, num and t. A number is achievable if it can become equal to num after
    applying the following operation:

    Increase or decrease the number by 1, and simultaneously increase or decrease num by 1.
    Return the maximum achievable number after applying the operation at most t times.

    Parameters
    ----------
    num: int

    t: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> theMaximumAchievableX(4, 1)
    6

    Explanation: Apply the following operation once to make the maximum achievable number equal to
    num:
    Decrease the maximum achievable number by 1, and increase num by 1.

    >>> theMaximumAchievableX(3, 2)
    7

    Explanation: Apply the following operation twice to make the maximum achievable number equal to
    num:
    Decrease the maximum achievable number by 1, and increase num by 1.
    """
    return num + 2 * t
