from collections import Counter

def commonChars(words: list[str]) -> list[str]:
    """
    ID: 1002
    Tags:   Array, Hash Table, String
    Time:   O(NM)
    Memory: O(N)

    Task
    ----------
    Given a string array words, return an array of all characters that show up in all strings within
    the words (including duplicates). You may return the answer in any order.

    Parameters
    ----------
    words: list[str]

    Returns
    -------
    out : list[str]

    Examples
    --------
    >>> commonChars(["bella","label","roller"])
    ['l', 'l', 'e']

    >>> commonChars(["cool","lock","cook"])
    ['o', 'c']
    """
    s = set(words[0])
    for w in words[1:]:
        s = set(w) & s
    cnt = {k: 101 for k in s}
    for w in words:
        c = Counter(w)
        for k, v in cnt.items():
            cnt[k] = min(v, c[k])
    ans = []
    for k, v in cnt.items():
        if v == 101:
            continue
        for _ in range(v):
            ans.append(k)
    return ans
