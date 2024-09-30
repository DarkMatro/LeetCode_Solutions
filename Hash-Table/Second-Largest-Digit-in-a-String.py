def secondHighest(s: str) -> int:
    """
    ID: 1796
    Tags:   Hash Table, String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given an alphanumeric string s, return the second largest numerical digit that appears in s, or
    -1 if it does not exist.

    An alphanumeric string is a string consisting of lowercase English letters and digits.

    Parameters
    ----------
    s: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> secondHighest('dfa12321afd')
    2

    Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.

    >>> secondHighest('abc1111')
    -1

    Explanation: The digits that appear in s are [1]. There is no second largest digit.
    """
    digits = set()
    max_v = -1
    for x in s:
        if x.isdigit():
            v = int(x)
            max_v = max(max_v, v)
            digits.add(v)
    if not digits:
        return -1
    digits.remove(max_v)
    return max(digits) if len(digits) >= 1 else -1
