def destCity(paths: list[list[str]]) -> str:
    """
    ID: 1436
    Tags:   Array, Hash Table, String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct
    path going from cityAi to cityBi. Return the destination city, that is, the city without any
    path outgoing to another city.

    It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be
    exactly one destination city.

    Parameters
    ----------
    paths: list[list[str]]

    Returns
    -------
    out : str

    Examples
    --------
    >>> destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])
    'Sao Paulo'

    Explanation:
    Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your
    trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

    >>> destCity([["B","C"],["D","B"],["C","A"]])
    'A'

    Explanation:
    All possible trips are:
    "D" -> "B" -> "C" -> "A".
    "B" -> "C" -> "A".
    "C" -> "A".
    "A".
    Clearly the destination city is "A".

    >>> destCity([["A","Z"]])
    'Z'
    """
    outgoing = set()
    incoming = set()
    for path in paths:
        outgoing.add(path[0])
        incoming.add(path[1])
    return (incoming - outgoing).pop()
