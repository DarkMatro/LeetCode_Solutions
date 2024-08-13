def sumZero(n: int) -> list[int]:
    """
    ID: 1304
    Tags:   Array, Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Given an integer n, return any array containing n unique integers such that they add up to 0.

    Parameters
    ----------
    n: int

    k: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> sumZero(5)
    [0, 1, -1, 2, -2]

    Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].


    >>> sumZero(3)
    [0, 1, -1]

    >>> sumZero(1)
    [0]
    """
    # Convert n from base 10 to base k
    result = []
    # If n is odd, add 0
    if n % 2 != 0:
        result.append(0)
        n -= 1

    # Add pairs of integers
    for i in range(1, n // 2 + 1):
        result.append(i)
        result.append(-i)

    return result
