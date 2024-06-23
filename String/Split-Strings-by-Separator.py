def splitWordsBySeparator(words: list[str], separator: str) -> list[str]:
    """
    ID: 2788
    Tags:   Array, String
    Time:   O(Nm)
    Memory: O(1)

    Task
    ----------
    Given an array of strings words and a character separator, split each string in words by
    separator.

    Return an array of strings containing the new strings formed after the splits, excluding empty
    strings.

    Notes

    separator is used to determine where the split should occur, but it is not included as part of
    the resulting strings.
    A split may result in more than two strings.
    The resulting strings must maintain the same order as they were initially given.

    Parameters
    ----------
    words: list[str]

    separator: str

    Returns
    -------
    out: list[str]

    Examples
    --------
    >>> splitWordsBySeparator(["one.two.three","four.five","six"], ".")
    ['one', 'two', 'three', 'four', 'five', 'six']

    Explanation: In this example we split as follows:

    "one.two.three" splits into "one", "two", "three"
    "four.five" splits into "four", "five"
    "six" splits into "six"

    Hence, the resulting array is ["one","two","three","four","five","six"].

    >>> splitWordsBySeparator(["$easy$","$problem$"], "$")
    ['easy', 'problem']

    Explanation: In this example we split as follows:

    "$easy$" splits into "easy" (excluding empty strings)
    "$problem$" splits into "problem" (excluding empty strings)

    Hence, the resulting array is ["easy","problem"].

    >>> splitWordsBySeparator(["|||"], "|")
    []

    Explanation: In this example the resulting split of "|||" will contain only empty strings, so we
    return an empty array [].
    """
    ans = []
    for word in words:
        for w in word.split(separator):
            if w:
                ans.append(w)
    return ans
