def isPathCrossing(path: str) -> bool:
    """
    ID: 1496
    Tags:   Hash Table, String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit
    north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk
    on the path specified by path.

    Return true if the path crosses itself at any point, that is, if at any time you are on a
    location you have previously visited. Return false otherwise.

    Parameters
    ----------
    path: str

    Returns
    -------
    out : bool

    Examples
    --------
    >>> isPathCrossing('NES')
    False

    Explanation: Notice that the path doesn't cross any point more than once.

    >>> isPathCrossing('NESWW')
    True

    Explanation: Notice that the path visits the origin twice.
    """
    x, y = 0, 0
    cache = set()
    cache.add((0, 0))
    for p in path:
        if p == 'N':
            x += 1
        elif p == 'S':
            x -= 1
        elif p == 'E':
            y += 1
        elif p == 'W':
            y -= 1
        new = (x, y)
        if new in cache:
            return True
        cache.add(new)
    return False
