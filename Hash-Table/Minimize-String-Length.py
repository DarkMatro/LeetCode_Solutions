def minimizedStringLength(s: str) -> int:
    """
    ID: 2716
    Tags:   Hash Table, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a string s, you have two types of operation:

    Choose an index i in the string, and let c be the character in position i. Delete the closest
    occurrence of c to the left of i (if exists).
    Choose an index i in the string, and let c be the character in position i. Delete the closest
    occurrence of c to the right of i (if exists).
    Your task is to minimize the length of s by performing the above operations zero or more times.

    Return an integer denoting the length of the minimized string.


    Parameters
    ----------
    nums: s: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> minimizedStringLength('aaabc')
    3

    Explanation:

    Operation 2: we choose i = 1 so c is 'a', then we remove s[2] as it is closest 'a' character to
    the right of s[1]. s becomes "aabc" after this.
    Operation 1: we choose i = 1 so c is 'a', then we remove s[0] as it is closest 'a' character to
    the left of s[1]. s becomes "abc" after this.

    >>> minimizedStringLength('cbbd')
    3

    Explanation: Operation 1: we choose i = 2 so c is 'b', then we remove s[1] as it is closest 'b'
    character to the left of s[1]. s becomes "cbd" after this.

    >>> minimizedStringLength('baadccab')
    4

    Explanation: Operation 1: we choose i = 6 so c is 'a', then we remove s[2] as it is closest 'a'
    character to the left of s[6]. s becomes "badccab" after this.
    Operation 2: we choose i = 0 so c is 'b', then we remove s[6] as it is closest 'b' character to
    the right of s[0]. s becomes "badcca" fter this.
    Operation 2: we choose i = 3 so c is 'c', then we remove s[4] as it is closest 'c' character to
    the right of s[3]. s becomes "badca" after this.
    Operation 1: we choose i = 4 so c is 'a', then we remove s[1] as it is closest 'a' character to
    the left of s[4]. s becomes "bdca" after this.
    """
    return len(set(s))
