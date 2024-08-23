def escapeGhosts(ghosts: list[list[int]], target: list[int]) -> bool:
    """
    ID: 789
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are playing a simplified PAC-MAN game on an infinite 2-D grid. You start at the point
    [0, 0], and you are given a destination point target = [xtarget, ytarget] that you are trying
    to get to. There are several ghosts on the map with their starting positions given as a 2D array
    ghosts, where ghosts[i] = [xi, yi] represents the starting position of the ith ghost. All inputs
    are integral coordinates.

    Each turn, you and all the ghosts may independently choose to either move 1 unit in any of the
    four cardinal directions: north, east, south, or west, or stay still. All actions happen
    simultaneously.

    You escape if and only if you can reach the target before any ghost reaches you. If you reach
    any square (including the target) at the same time as a ghost, it does not count as an escape.

    Return true if it is possible to escape regardless of how the ghosts move, otherwise return
    false.

    Parameters
    ----------
    ghosts: list[list[int]]

    target: list[int]

    Returns
    -------
    out : bool

    Examples
    --------
    >>> escapeGhosts([[1,0],[0,3]], [0,1])
    True

    Explanation: You can reach the destination (0, 1) after 1 turn, while the ghosts located at
    (1, 0) and (0, 3) cannot catch up with you.

    --------
    >>> escapeGhosts([[1,0]], [2,0])
    False

    Explanation: You need to reach the destination (2, 0), but the ghost at (1, 0) lies between you
    and the destination.

    >>> escapeGhosts([[2,0]], [1,0])
    False

    Explanation: The ghost can reach the target at the same time as you.
    """
    pacman_md = manhattan_distance([0, 0], target)
    ghosts_md = min(manhattan_distance(x, target) for x in ghosts)
    return pacman_md < ghosts_md


def manhattan_distance(point1: list[int], point2: list[int]) -> int:
    return sum(abs(a - b) for a, b in zip(point1, point2))
