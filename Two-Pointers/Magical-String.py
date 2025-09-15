def magicalString(n: int) -> int:
    """
    ID: 481
    Tags: Two Pointers, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    A magical string s consists of only '1' and '2' and obeys the following rules:

    The string s is magical because concatenating the number of contiguous occurrences of characters '1' and '2'
    generates the string s itself.
    The first few elements of s is s = "1221121221221121122……". If we group the consecutive 1's and 2's in s, it will
    be "1 22 11 2 1 22 1 22 11 2 11 22 ......" and the occurrences of 1's or 2's in each group are "1 2 2 1 1 2 1 2 2 1 2 2 ......". You can see that the occurrence sequence is s itself.

    Given an integer n, return the number of 1's in the first n number in the magical string s.

    Parameters
    ----------
    n: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> magicalString(6)
    3

    Explanation: The first 6 elements of magical string s is "122112" and it contains three 1's, so return 3.

    >>> magicalString(1)
    1
    """
    if n == 0:
        return 0
    if n <= 3:
        return 1  # "122" has only one '1' in its first 3 chars

    s = [1, 2, 2]
    head = 2  # reading pointer
    num = 1  # next number to append

    while len(s) < n:
        count = s[head]
        s.extend([num] * count)
        num = 3 - num  # flip between 1 and 2
        head += 1

    return s[:n].count(1)
