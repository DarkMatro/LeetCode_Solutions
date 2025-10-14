def countCoveredBuildings(n: int, buildings: list[list[int]]) -> int:
    """
    ID: 3531
    Tags:   Array, Hash Table, Sorting
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, where
    buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].

    A building is covered if there is at least one building in all four directions: left, right, above, and below.

    Return the number of covered buildings.

    Parameters
    ----------
    n: int

    buildings: list[list[int]]

    Returns
    -------
    out : int

    Examples
    --------
    >>> countCoveredBuildings(3, [[1,2],[2,2],[3,2],[2,1],[2,3]])
    1

    Explanation:
    Only building [2,2] is covered as it has at least one building:
    above ([1,2])
    below ([3,2])
    left ([2,1])
    right ([2,3])
    Thus, the count of covered buildings is 1.

    >>> countCoveredBuildings(3, [[1,1],[1,2],[2,1],[2,2]])
    0

    Explanation:
    No building has at least one building in all four directions.

    >>> countCoveredBuildings(5, [[1,3],[3,2],[3,3],[3,5],[5,3]])
    1

    Explanation:
    Only building [3,3] is covered as it has at least one building:
    above ([1,3])
    below ([5,3])
    left ([3,2])
    right ([3,5])
    Thus, the count of covered buildings is 1.
    """
    rows = dict()
    cols = dict()
    for x, y in buildings:
        if y in rows:
            x_min, x_max = rows[y]
            rows[y] = [min(x, x_min), max(x, x_max)]
        else:
            rows[y] = [x, x]
        if x in cols:
            y_min, y_max = cols[x]
            cols[x] = [min(y, y_min), max(y, y_max)]
        else:
            cols[x] = [y, y]
    ans = 0
    for x, y in buildings:
        x_min, x_max = rows[y]
        y_min, y_max = cols[x]
        if x_min < x < x_max and y_min < y < y_max:
            ans += 1
    return ans
