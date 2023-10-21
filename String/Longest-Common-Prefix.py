def longest_common_prefix(strs: list[str]) -> str:
    """
    ID: 0014
    Tags:   String, Trie
    Time:   O(NlogN)
    Memory: O(1)

    Task
    ----------
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    Parameters
    ----------
    strs : list[str]
        array of strings

    Returns
    -------
    and: str
        longest common prefix string amongst strs

    Examples
    --------
    >>> longest_common_prefix(["flower","flow","flight"])
    'fl'

    >>> longest_common_prefix(["dog","racecar","car"])
    ''

    Explanation: There is no common prefix amongst the input strings.

    """
    if not strs:
        return ''
    strs = sorted(strs)
    min_len = min(len(strs[0]), len(strs[-1]))
    first_word = strs[0]
    last_word = strs[-1]
    ans = ''
    for i in range(min_len):
        if first_word[i] == last_word[i]:
            ans += first_word[i]
        else:
            break
    return ans
