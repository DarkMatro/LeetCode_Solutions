def divisibilityArray(word: str, m: int) -> list[int]:
    """
    ID: 2575
    Tags:   Array, Math, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a 0-indexed string word of length n consisting of digits, and a positive integer m

    The divisibility array div of word is an integer array of length n such that:

    div[i] = 1 if the numeric value of word[0,...,i] is divisible by m, or
    div[i] = 0 otherwise.
    Return the divisibility array of word.

    Parameters
    ----------
    word: str

    m: int

    Returns
    -------
    list[int]

    Examples
    --------
    >>> divisibilityArray('998244353', 3)
    [1, 1, 0, 0, 0, 1, 1, 0, 0]

    Explanation: There are only 4 prefixes that are divisible by 3: "9", "99", "998244", and
    "9982443".

    >>> divisibilityArray('1010', 10)
    [0, 1, 0, 1]

    Explanation: There are only 2 prefixes that are divisible by 10: "10", and "1010".
    """
    n = len(word)
    div = [0] * n
    remainder = 0

    for i in range(n):
        remainder = (remainder * 10 + int(word[i])) % m
        div[i] = 1 if remainder == 0 else 0

    return div
