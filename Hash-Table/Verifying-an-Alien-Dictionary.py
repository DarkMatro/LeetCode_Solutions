def isAlienSorted(words: list[str], order: str) -> bool:
    """
    ID: 953
    Tags:   Array, Hash Table, String
    Time:   O(N*M)
    Memory: O(N)

    Task
    ----------
    In an alien language, surprisingly, they also use English lowercase letters, but possibly in a
    different order. The order of the alphabet is some permutation of lowercase letters.

    Given a sequence of words written in the alien language, and the order of the alphabet, return
    true if and only if the given words are sorted lexicographically in this alien language.

    Parameters
    ----------
    words: list[str]

    order: str

    Returns
    -------
    out : bool

    Examples
    --------
    >>> isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
    True

    Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

    >>> isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")
    False

    Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the
    sequence is unsorted.

    >>> isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")
    False

    Explanation: The first three characters "app" match, and the second string is shorter (in size.)
    According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as
    the blank character which is less than any other character (More info).
    """
    idx_order = {x: i for i, x in enumerate(order)}
    new_words = [[idx_order[x] for x in w] for w in words]
    prev = new_words[0]
    for i, w in enumerate(new_words):
        if i == 0:
            continue
        if w < prev:
            return False
        prev = w
    return True
