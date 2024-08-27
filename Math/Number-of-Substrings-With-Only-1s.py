def numSub(s: str) -> int:
    """
    ID: 1513
    Tags:   Math, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a binary string s, return the number of substrings with all characters 1's. Since the
    answer may be too large, return it modulo 10^9 + 7.

    Parameters
    ----------
    s: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> numSub("0110111")
    9

    Explanation: There are 9 substring in total with only 1's characters.
    "1" -> 5 times.
    "11" -> 3 times.
    "111" -> 1 time.

    >>> numSub("101")
    2

    Explanation: Substring "1" is shown 2 times in s.

    >>> numSub("111111")
    21

    Explanation: Each substring contains only 1's characters.
    """
    MOD = 10 ** 9 + 7
    n = 0
    total = 0

    for x in s:
        if x == '1':
            n += 1
        else:
            total += (n * (n + 1)) // 2
            total %= MOD
            n = 0

    # If the string ends with a sequence of '1's, add its contribution
    if n > 0:
        total += (n * (n + 1)) // 2
        total %= MOD

    return total
