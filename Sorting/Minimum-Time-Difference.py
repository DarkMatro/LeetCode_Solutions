def findMinDifference(timePoints: list[str]) -> int:
    """
    ID: 539
    Tags:   Array, Math, String, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes
    difference between any two time-points in the list.

    Parameters
    ----------
    timePoints: list[str]

    Returns
    -------
    int

    Examples
    --------
    >>> findMinDifference(["23:59","00:00"])
    1

    >>> findMinDifference(["00:00","23:59","00:00"])
    0
    """
    times = sorted([int(x[:2]) * 60 + int(x[3:]) for x in timePoints])
    min_v = 1440
    prev = times[0]
    for i, x in enumerate(times):
        if i == 0:
            continue
        min_v = min(min_v, x - prev)
        prev = x
    min_v = min(min_v, 1440 - times[-1] + times[0])
    return min_v
