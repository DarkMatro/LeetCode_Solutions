from itertools import groupby


def minimumLength(s: str) -> int:
    """
    ID: 1750
    Tags:   Two Pointers, String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on
    the string any number of times:

    Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
    Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
    The prefix and the suffix should not intersect at any index.
    The characters from the prefix and suffix must be the same.
    Delete both the prefix and the suffix.
    Return the minimum length of s after performing the above operation any number of times (possibly zero times).

    Parameters
    ----------
    s: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> minimumLength("ca")
    2

    Explanation: You can't remove any characters, so the string stays as is.

    >>> minimumLength("cabaabac")
    0

    Explanation: An optimal sequence of operations is:
    - Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
    - Take prefix = "a" and suffix = "a" and remove them, s = "baab".
    - Take prefix = "b" and suffix = "b" and remove them, s = "aa".
    - Take prefix = "a" and suffix = "a" and remove them, s = "".

    >>> minimumLength("aabccabba")
    3

    Explanation: An optimal sequence of operations is:
    - Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
    - Take prefix = "b" and suffix = "bb" and remove them, s = "cca".
    """
    n = len(s)
    if n == 1:
        return 1
    compressed = [(char, len(list(group))) for char, group in groupby(s)]
    ans = 0
    lp, rp = 0, len(compressed) - 1
    while lp <= rp:
        l_char, ln = compressed[lp]
        r_char, rn = compressed[rp]
        if l_char != r_char:
            break
        else:
            ans += ln + rn if lp != rp else ln if ln > 1 else 0
            lp += 1
            rp -= 1
    return n - ans