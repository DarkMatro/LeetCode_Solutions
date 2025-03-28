def numSpecialEquivGroups(words: list[str]) -> int:
    """
    ID: 893
    Tags:   Array, Hash Table, String, Sorting
    Time:   O(NMlogM)
    Memory: O(NM)

    Task
    ----------
    You are given an array of strings of the same length words.

    In one move, you can swap any two even indexed characters or any two odd indexed characters of a
    string words[i].

    Two strings words[i] and words[j] are special-equivalent if after any number of moves,
    words[i] == words[j].

    For example, words[i] = "zzxy" and words[j] = "xyzz" are special-equivalent because we may make
    the moves "zzxy" -> "xzzy" -> "xyzz".
    A group of special-equivalent strings from words is a non-empty subset of words such that:

    Every pair of strings in the group are special equivalent, and
    The group is the largest size possible (i.e., there is not a string words[i] not in the group
    such that words[i] is special-equivalent to every string in the group).
    Return the number of groups of special-equivalent strings from words.

    Parameters
    ----------
    words: list[str]

    Returns
    -------
    int

    Examples
    --------
    >>> numSpecialEquivGroups(["abcd","cdab","cbad","xyzz","zzxy","zzyx"])
    3

    Explanation: One group is ["abcd", "cdab", "cbad"], since they are all pairwise special
    equivalent, and none of the other strings is all pairwise special equivalent to these.
    The other two groups are ["xyzz", "zzxy"] and ["zzyx"].
    Note that in particular, "zzxy" is not special equivalent to "zzyx".

    >>> numSpecialEquivGroups(["abc","acb","bac","bca","cab","cba"])
    3

    """
    return len({''.join(sorted(w[::2]) + sorted(w[1::2])) for w in words})
