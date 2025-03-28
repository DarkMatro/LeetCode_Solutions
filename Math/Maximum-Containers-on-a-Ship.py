def maxContainers(n: int, w: int, maxWeight: int) -> int:
    """
    ID: 3492
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    You are given a positive integer n representing an n x n cargo deck on a ship. Each cell on the
    deck can hold one container with a weight of exactly w.

    However, the total weight of all containers, if loaded onto the deck, must not exceed the ship's
    maximum weight capacity, maxWeight.

    Return the maximum number of containers that can be loaded onto the ship.

    Parameters
    ----------
    n: int

    w: int

    maxWeight: int

    Returns
    -------
    int

    Examples
    --------
    >>> maxContainers(2, 3, 15)
    4

    Explanation: The deck has 4 cells, and each container weighs 3. The total weight of loading all
    containers is 12, which does not exceed maxWeight.

    >>> maxContainers(3, 5, 20)
    4

    Explanation: The deck has 9 cells, and each container weighs 5. The maximum number of containers
    that can be loaded without exceeding maxWeight is 4.
    """
    return min(n*n, maxWeight//w)

