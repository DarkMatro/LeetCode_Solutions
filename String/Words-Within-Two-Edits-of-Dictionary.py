def can_be_changed(q: str, d: str) -> bool:
    """
    Check q after a maximum of two edits can be equal to d.

    Parameters
    ----------
    q : str
        word from queries
    d : str
        dictionary from queries

    Returns
    -------
    out : bool
    """
    n_diffs = 0
    for i, j in zip(q, d):
        if i != j:
            n_diffs += 1
            if n_diffs > 2:
                return False
    return True

def twoEditWords(queries: list[str], dictionary: list[str]) -> list[str]:
    """
    ID: 2452
    Tags:   Array, String
    Time:   O(Len(Queries)∗Len(Dictionary)∗Len(Q))
    Memory: O(1)

    Task
    ----------
    You are given two string arrays, queries and dictionary. All words in each array comprise of
    lowercase English letters and have the same length.

    In one edit you can take a word from queries, and change any letter in it to any other letter.
    Find all words from queries that, after a maximum of two edits, equal some word from dictionary.

    Return a list of all words from queries, that match with some word from dictionary after a
    maximum of two edits. Return the words in the same order they appear in queries.

    Parameters
    ----------
    queries : list[str]

    dictionary : list[str]

    Returns
    -------
    out : list[str]

    Examples
    --------
    >>> twoEditWords(["word","note","ants","wood"], ["wood","joke","moat"])
    ['word', 'note', 'wood']

    >>> twoEditWords(["yes"], ["not"])
    []
    """
    ans = []
    for q in queries:
        for d in dictionary:
            if can_be_changed(q, d):
                ans.append(q)
                break
    return ans
