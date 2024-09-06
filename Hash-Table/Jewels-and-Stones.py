from collections import Counter

def numJewelsInStones(jewels: str, stones: str) -> int:
    """
    ID: 771
    Tags:   Hash Table, String
    Time:   O(N + M)
    Memory: O(N)

    Task
    ----------
    You're given strings jewels representing the types of stones that are jewels, and stones
    representing the stones you have. Each character in stones is a type of stone you have. You want
    to know how many of the stones you have are also jewels.

    Letters are case-sensitive, so "a" is considered a different type of stone from "A".

    Parameters
    ----------
    jewels: str

    stones: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> numJewelsInStones('aA', 'aAAbbbb')
    3

    >>> numJewelsInStones('z', 'ZZ')
    0
    """
    s = Counter(stones)
    return sum([s[x] for x in jewels])
