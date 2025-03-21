from collections import Counter


def checkStrings(s1: str, s2: str) -> bool:
    """
    ID: 2840
    Tags:   Hash Table, String, Sorting
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.

    You can apply the following operation on any of the two strings any number of times:

    Choose any two indices i and j such that i < j and the difference j - i is even, then swap the
    two characters at those indices in the string.
    Return true if you can make the strings s1 and s2 equal, and false otherwise.

    Parameters
    ----------
    s1: str

    s2: str

    Returns
    -------
    bool

    Examples
    --------
    >>> checkStrings("abcdba", "cabdab")
    True

    Explanation: We can apply the following operations on s1:
    - Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
    - Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
    - Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.

    >>> checkStrings("abe", "bea")
    False

    Explanation: It is not possible to make the two strings equal.
    """
    return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])
