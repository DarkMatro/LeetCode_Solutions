def flowerGame(n: int, m: int) -> int:
    """
    ID: 3021
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Alice and Bob are playing a turn-based game on a circular field surrounded by flowers. The
    circle represents the field, and there are x flowers in the clockwise direction between Alice
    and Bob, and y flowers in the anti-clockwise direction between them.

    The game proceeds as follows:

    Alice takes the first turn.
    In each turn, a player must choose either the clockwise or anti-clockwise direction and pick one
    flower from that side.
    At the end of the turn, if there are no flowers left at all, the current player captures their
    opponent and wins the game.
    Given two integers, n and m, the task is to compute the number of possible pairs (x, y) that
    satisfy the conditions:

    Alice must win the game according to the described rules.
    The number of flowers x in the clockwise direction must be in the range [1,n].
    The number of flowers y in the anti-clockwise direction must be in the range [1,m].
    Return the number of possible pairs (x, y) that satisfy the conditions mentioned in the statement.

    Parameters
    ----------
    n: int

    m: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> flowerGame(3, 2)
    3

    The following pairs satisfy conditions described in the statement: (1,2), (3,2), (2,1).

    >>> flowerGame(1, 1)
    0

    No pairs satisfy the conditions described in the statement.
    """
    return n * m // 2
