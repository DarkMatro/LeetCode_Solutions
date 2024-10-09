from collections import defaultdict


def leastBricks(wall: list[list[int]]) -> int:
    """
    ID: 554
    Tags:   Array, Hash Table
    Time:   O(NM)
    Memory: O(N)

    Task
    ----------
    There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some
    number of bricks each of the same height (i.e., one unit) but they can be of different widths.
    The total width of each row is the same.

    Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes
    through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line
    just along one of the two vertical edges of the wall, in which case the line will obviously
    cross no bricks.

    Given the 2D array wall that contains the information about the wall, return the minimum number
    of crossed bricks after drawing such a vertical line.

    Parameters
    ----------
    wall: list[list[int]]

    Returns
    -------
    out : int

    Examples
    --------
    >>> leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]])
    2

    >>> leastBricks([[1],[1],[1]])
    3
    """
    edge_count = defaultdict(int)
    # Loop over each row in the wall
    for bricks in wall:
        edge_position = 0
        # Loop over each brick in the row, excluding the last brick
        for i, b in enumerate(bricks):
            if i == len(bricks) - 1:
                continue
            edge_position += b
            edge_count[edge_position] += 1
    max_edges = max(edge_count.values(), default=0)
    return len(wall) - max_edges
