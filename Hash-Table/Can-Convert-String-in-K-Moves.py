def canConvertString(s: str, t: str, k: int) -> bool:
    """
    ID: 1540
    Tags: Hash Table, String
    Time: O(N)
    Memory: O(1)

    Task
    ----------
    Given two strings s and t, your goal is to convert s into t in k moves or less.

    During the ith (1 <= i <= k) move you can:

    Choose any index j (1-indexed) from s, such that 1 <= j <= s.length and j has not been chosen in
    any previous move, and shift the character at that index i times.
    Do nothing.
    Shifting a character means replacing it by the next letter in the alphabet (wrapping around so
    that 'z' becomes 'a'). Shifting a character by i means applying the shift operations i times.

    Remember that any index j can be picked at most once.

    Return true if it's possible to convert s into t in no more than k moves, otherwise return
    false.

    Parameters
    ----------
    s: str

    t: str

    k: int

    Returns
    -------
    bool

    Examples
    --------
    >>> canConvertString('input', 'ouput', k=9)
    True

    Explanation:
    In the 6th move, we shift 'i' 6 times to get 'o'. And in the 7th move we shift 'n' to get 'u'.

    >>> canConvertString('abc', 'bcd', k=10)
    False

    Explanation:
    We need to shift each character in s one time to convert it into t. We can shift 'a' to 'b'
    during the 1st move. However, there is no way to shift the other characters in the remaining
    moves to obtain t from s.

    >>> canConvertString('aab', 'bbb', k=27)
    True

    Explanation:
    In the 1st move, we shift the first 'a' 1 time to get 'b'. In the 27th move, we shift the second
    'a' 27 times to get 'b'.
    """
    if len(s) != len(t):
        return False
    dp = [-1] * 27
    for a, b in zip(s, t):
        n = ord(b) - ord(a)
        dp[n if n >= 0 else 26 + n] += 1
    return all([dp[i] <= (k - i) // 26 for i in range(1, 27)])
