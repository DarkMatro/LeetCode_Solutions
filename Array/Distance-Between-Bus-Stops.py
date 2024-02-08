def distanceBetweenBusStops(distance: list[int], start: int, destination: int) -> int:
    """
    ID: 1184
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of
    neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.

    The bus goes along both directions i.e. clockwise and counterclockwise.

    Return the shortest distance between the given start and destination stops.

    Parameters
    ----------
    distance: list[int]

    start: int

    destination: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> distanceBetweenBusStops([1,2,3,4], 0, 1)
    1

    Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.

    >>> distanceBetweenBusStops([1,2,3,4], 0, 2)
    3

    Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.

    >>> distanceBetweenBusStops([1,2,3,4], 0, 3)
    4

    Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.
    """
    start, destination = (start, destination) if start > destination else (destination, start)
    return min(sum(distance[start:]) + sum(distance[:destination]), sum(distance[destination:start]))
