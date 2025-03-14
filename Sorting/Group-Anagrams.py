def groupAnagrams(strs: list[str]) -> list[list[str]]:
    """
    ID: 49
    Tags:   Array, Hash Table, String, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    Given an array of strings strs, group the anagrams together. You can return the answer in any
    order.

    Parameters
    ----------
    strs: list[str]

    Returns
    -------
    list[list[str]]

    Examples
    --------
    >>> groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    Explanation: There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

    >>> groupAnagrams([""])
    [['']]

    >>> groupAnagrams(["a"])
    [['a']]
    """
    mp = {}
    ans = []
    for s in strs:
        c = ''.join(sorted(s))
        if c not in mp:
            mp[c] = len(ans)
            ans.append([s])
        else:
            ans[mp[c]].append(s)
    return ans
