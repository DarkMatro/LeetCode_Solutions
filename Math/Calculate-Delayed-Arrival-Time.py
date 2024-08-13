def findDelayedArrivalTime(arrivalTime: int, delayedTime: int) -> int:
    """
    ID: 2651
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    You are given a positive integer arrivalTime denoting the arrival time of a train in hours,
    and another positive integer delayedTime denoting the amount of delay in hours.

    Return the time when the train will arrive at the station.

    Note that the time in this problem is in 24-hours format.

    Parameters
    ----------
    arrivalTime: int

    delayedTime: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> findDelayedArrivalTime(15, 5)
    20

    Explanation: Arrival time of the train was 15:00 hours. It is delayed by 5 hours. Now it will
    reach at 15+5 = 20 (20:00 hours).

    >>> findDelayedArrivalTime(13, 11)
    0

    Explanation: Arrival time of the train was 13:00 hours. It is delayed by 11 hours. Now it will
    reach at 13+11=24 (Which is denoted by 00:00 in 24 hours format so return 0).
    """
    return (arrivalTime + delayedTime) % 24
