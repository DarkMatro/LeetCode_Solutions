def checkZeroOnes(s: str) -> bool:
    """
    ID: 1869
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer
    than the longest contiguous segment of 0's in s, or return false otherwise.

    For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the
    longest continuous segment of 0s has length 3.
    Note that if there are no 0's, then the longest continuous segment of 0's is considered to have
    a length 0. The same applies if there is no 1's.

    Parameters
    ----------
    s: str

    Returns
    -------
    out: bool

    Examples
    --------
    >>> checkZeroOnes("1101")
    True

    Explanation:
    The longest contiguous segment of 1s has length 2: "1101"
    The longest contiguous segment of 0s has length 1: "1101"
    The segment of 1s is longer, so return true.

    >>> checkZeroOnes("111000")
    False

    Explanation:
    The longest contiguous segment of 1s has length 3: "111000"
    The longest contiguous segment of 0s has length 3: "111000"
    The segment of 1s is not longer, so return false.

    >>> checkZeroOnes("110100010")
    False

    Explanation:
    The longest contiguous segment of 1s has length 2: "110100010"
    The longest contiguous segment of 0s has length 3: "110100010"
    The segment of 1s is not longer, so return false.
    """
    prev = s[0]
    max_len1 = len1 = 1 if prev == '1' else 0
    max_len0 = len0 = 1 if prev == '0' else 0
    for i in range(1, len(s)):
        num = s[i]
        if num == '1':
            len1 += 1
            if prev == '0':
                max_len0 = max(max_len0, len0)
                len0 = 0
        else:
            len0 += 1
            if prev == '1':
                max_len1 = max(max_len1, len1)
                len1 = 0
        prev = num
    return max(max_len1, len1) > max(max_len0, len0)
