def countBinarySubstrings(s: str) -> int:
    """
    ID: 696
    Tags:   Two Pointers, String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and
    all the 0's and all the 1's in these substrings are grouped consecutively.

    Substrings that occur multiple times are counted the number of times they occur.

    Parameters
    ----------
    s: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> countBinarySubstrings("00110011")
    6

    Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10",
    "0011", and "01".
    Notice that some of these substrings repeat and are counted the number of times they occur.
    Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

    >>> countBinarySubstrings("10101")
    4

    Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
    """
    runs = []
    cnt = 1
    last_x = s[0]
    for i, x in enumerate(s):
        if i == 0:
            continue
        if x != last_x:
            runs.append(cnt)
            cnt = 0
        last_x = x
        cnt += 1
    else:
        runs.append(cnt)

    return sum(min(runs[i], runs[i + 1]) for i in range(len(runs) - 1))
