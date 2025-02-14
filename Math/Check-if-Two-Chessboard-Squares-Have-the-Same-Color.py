def checkTwoChessboards(coordinate1: str, coordinate2: str) -> bool:
    """
    ID: 3274
    Tags:   Math, String
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    You are given two strings, coordinate1 and coordinate2, representing the coordinates of a square
    on an 8 x 8 chessboard.

    Below is the chessboard for reference.

    Return true if these two squares have the same color and false otherwise.

    The coordinate will always represent a valid chessboard square. The coordinate will always have
    the letter first (indicating its column), and the number second (indicating its row).

    Parameters
    ----------
    coordinate1: str

    coordinate2: str

    Returns
    -------
    bool

    Examples
    --------
    >>> checkTwoChessboards("a1", 'c3')
    True

    Explanation:
    Both squares are black.

    >>> checkTwoChessboards("a1", 'h3')
    False

    Explanation:
    Square "a1" is black and "h3" is white.
    """
    x1, y1 = ord(coordinate1[0]) - 96, int(coordinate1[1])
    x2, y2 = ord(coordinate2[0]) - 96, int(coordinate2[1])
    return (x1 + y1) % 2 == (x2 + y2) % 2
