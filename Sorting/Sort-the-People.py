def sortPeople(names: list[str], heights: list[int]) -> list[str]:
    """
    ID: 2418
    Tags:   Array, Hash Table, String, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    You are given an array of strings names, and an array heights that consists of distinct positive
    integers. Both arrays are of length n.

    For each index i, names[i] and heights[i] denote the name and height of the ith person.

    Return names sorted in descending order by the people's heights.

    Parameters
    ----------
    names: list[str]

    heights: list[int]

    Returns
    -------
    list[str]

    Examples
    --------
    >>> sortPeople(["Mary","John","Emma"], [180,165,170])
    ['Mary', 'Emma', 'John']

    Explanation: Mary is the tallest, followed by Emma and John.

    >>> sortPeople(["Alice","Bob","Bob"], [155,185,150])
    ['Bob', 'Alice', 'Bob']

    Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
    """
    d = {h: n for n, h in zip(names, heights)}
    return [d[x] for x in sorted(d.keys(), reverse=True)]
