def minOperations(s: str) -> int:
    """
    ID: 1758
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a string s consisting only of the characters '0' and '1'. In one operation, you
    can change any '0' to '1' or vice versa.

    The string is called alternating if no two adjacent characters are equal. For example, the
    string "010" is alternating, while the string "0100" is not.

    Return the minimum number of operations needed to make s alternating.

    Parameters
    ----------
    s: str

    Returns
    -------
    out: int

    Examples
    --------
    >>> minOperations("0100")
    1

    Explanation: If you change the last character to '1', s will be "0101", which is alternating.

    >>> minOperations("10")
    0

    Explanation: s is already alternating.

    >>> minOperations("1111")
    2

    Explanation: You need two operations to reach "0101" or "1010".
    """
    ans1 = ans2 = 0
    for i, b in enumerate(s):
        num = int(b)
        if i % 2 == num:
            ans1 += 1
        else:
            ans2 += 1
    return min(ans1, ans2)
