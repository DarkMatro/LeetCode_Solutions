def findLongestWord(s: str, dictionary: list[str]) -> str:
    """
    ID: 524
    Tags: Array, Two Pointers, String, Sorting
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by
    deleting some of the given string characters. If there is more than one possible result, return the longest word
    with the smallest lexicographical order. If there is no possible result, return the empty string.

    Parameters
    ----------
    s: str

    dictionary: list[str]

    Returns
    -------
    out : str

    Examples
    --------
    >>> findLongestWord("abpcplea", ["ale","apple","monkey","plea"])
    'apple'

    >>> findLongestWord("abpcplea", ["a","b","c"])
    'a'
    """
    res = ""
    for word in dictionary:
        a, b = len(word), len(res)
        if a < b or (a == b and word > res):
            continue
        idx = -1
        for char in word:
            idx = s.find(char, idx + 1)
            if idx == -1:
                break
        else:
            res = word
    return res
