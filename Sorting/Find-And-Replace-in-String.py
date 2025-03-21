def findReplaceString(s: str, indices: list[int], sources: list[str], targets: list[str]) -> str:
    """
    ID: 833
    Tags:   Array, Hash Table, String, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    You are given a 0-indexed string s that you must perform k replacement operations on. The
    replacement operations are given as three 0-indexed parallel arrays, indices, sources, and
    targets, all of length k.

    To complete the ith replacement operation:

    Check if the substring sources[i] occurs at index indices[i] in the original string s.
    If it does not occur, do nothing.
    Otherwise, if it does occur, replace that substring with targets[i].
    For example, if s = "abcd", indices[i] = 0, sources[i] = "ab", and targets[i] = "eee", then the
    result of this replacement will be "eeecd".

    All replacement operations must occur simultaneously, meaning the replacement operations should
    not affect the indexing of each other. The testcases will be generated such that the
    replacements will not overlap.

    For example, a testcase with s = "abc", indices = [0, 1], and sources = ["ab","bc"] will not be
    generated because the "ab" and "bc" replacements overlap.
    Return the resulting string after performing all replacement operations on s.

    A substring is a contiguous sequence of characters in a string.

    Parameters
    ----------
    s: str

    indices: list[int]

    sources: list[str]

    targets: list[str]

    Returns
    -------
    str

    Examples
    --------
    >>> findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"])
    'eeebffff'

    Explanation: "a" occurs at index 0 in s, so we replace it with "eee".
    "cd" occurs at index 2 in s, so we replace it with "ffff".

    >>> findReplaceString("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"])
    'eeecd'

    Explanation: "ab" occurs at index 0 in s, so we replace it with "eee".
    "ec" does not occur at index 2 in s, so we do nothing.
    """
    replacements = sorted(zip(indices, sources, targets), reverse=True)

    # Convert the string into a list to allow modifications
    s_list = list(s)

    for index, source, target in replacements:
        # Check if the substring at the given index matches the source string
        if s[index:index + len(source)] == source:
            # Perform the replacement
            s_list[index:index + len(source)] = list(target)
    return "".join(s_list)
