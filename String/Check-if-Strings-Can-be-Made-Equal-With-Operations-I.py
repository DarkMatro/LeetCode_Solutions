def canBeEqual(s1: str, s2: str) -> bool:
    """
    ID: 2839
    Tags:   String
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    You are given two strings s1 and s2, both of length 4, consisting of lowercase English letters.

    You can apply the following operation on any of the two strings any number of times:

    Choose any two indices i and j such that j - i = 2, then swap the two characters at those
    indices in the string.
    Return true if you can make the strings s1 and s2 equal, and false otherwise.

    Parameters
    ----------
    s1: str

    s2: str

    Returns
    -------
    out: bool

    Examples
    --------
    >>> canBeEqual("abcd", "cdab")
    True

    Explanation: We can do the following operations on s1:
    - Choose the indices i = 0, j = 2. The resulting string is s1 = "cbad".
    - Choose the indices i = 1, j = 3. The resulting string is s1 = "cdab" = s2.

    >>> canBeEqual("abcd", "dacb")
    False

    Explanation: It is not possible to make the two strings equal.
    """
    return {s1[0], s1[2]} == {s2[0], s2[2]} and {s1[1], s1[3]} == {s2[1], s2[3]}
