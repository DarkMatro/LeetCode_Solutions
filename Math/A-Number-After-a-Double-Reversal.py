def isSameAfterReversals(num: int) -> bool:
    """
    ID: 2119
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Reversing an integer means to reverse all its digits.

    For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not
    retained.
    Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2.
    Return true if reversed2 equals num. Otherwise, return false.

    Parameters
    ----------
    num: int

    Returns
    -------
    out : bool

    Examples
    --------
    >>> isSameAfterReversals(526)
    True

    Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.

    >>> isSameAfterReversals(1800)
    False

    Explanation: Reverse num to get 81, then reverse 81 to get 18, which does not equal num.

    >>> isSameAfterReversals(0)
    True

    Explanation: Reverse num to get 0, then reverse 0 to get 0, which equals num.
    """
    if num == 0 or num % 10 != 0:
        return True
    return False
