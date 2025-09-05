def mergeAlternately(word1: str, word2: str) -> str:
    """
    ID: 1768
    Tags:   Two Pointers, String
    Time:   O(n)
    Memory: O(1)

    Task
    ----------
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with
    word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

    Return the merged string.

    Parameters
    ----------
    word1 : str
    word2 : str

    Returns
    -------
    out : str

    Examples
    --------
    >>> mergeAlternately("abc", "pqr")
    'apbqcr'

    Explanation: The merged string will be merged as so:
    word1:  a   b   c
    word2:    p   q   r
    merged: a p b q c r

    >>> mergeAlternately("ab", "pqrs")
    'apbqrs'

    Explanation: Notice that as word2 is longer, "rs" is appended to the end.
    word1:  a   b
    word2:    p   q   r   s
    merged: a p b q   r   s

    >>> mergeAlternately("abcd", "pq")
    'apbqcd'

    Explanation: Notice that as word1 is longer, "cd" is appended to the end.
    word1:  a   b   c   d
    word2:    p   q
    merged: a p b q c   d
    """
    lp = 0
    rp = 0
    n1 = len(word1)
    n2 = len(word2)
    min_n = min(n1, n2)
    ans = ''
    while lp < n1 and rp < n2:
        ans += word1[lp] + word2[rp]
        lp += 1
        rp += 1
    else:
        if n1 != n2:
            ans = ans + (word1[min_n:] if n1 > n2 else word2[min_n:])
    return ans
