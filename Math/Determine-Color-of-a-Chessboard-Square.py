def squareIsWhite(coordinates: str) -> bool:
    """
    ID: 1812
    Tags:   Math, String
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    You are given coordinates, a string that represents the coordinates of a square of the
    chessboard. Below is a chessboard for your reference.

    Return true if the square is white, and false if the square is black.

    The coordinate will always represent a valid chessboard square. The coordinate will always have
    the letter first, and the number second.

    Parameters
    ----------
    coordinates: str

    Returns
    -------
    out : bool

    Examples
    --------
    >>> squareIsWhite('a1')
    False

    Explanation: From the chessboard above, the square with coordinates "a1" is black, so return
    false.

    >>> squareIsWhite('h3')
    True

    Explanation: From the chessboard above, the square with coordinates "h3" is white, so return
    true

    >>> squareIsWhite('c7')
    False

    """
    x = ord(coordinates[0]) - 96
    y = int(coordinates[1])
    return (x + y) % 2 != 0
