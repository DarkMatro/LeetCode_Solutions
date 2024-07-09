def parse_time(event_time: str) -> int:
    new_time = event_time.split(':')
    return int(new_time[0]) * 60 + int(new_time[1])

def haveConflict(event1: list[str], event2: list[str]) -> bool:
    """
    ID: 2446
    Tags:   Array, String
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    You are given two arrays of strings that represent two inclusive events that happened on the
    same day, event1 and event2, where:

    event1 = [startTime1, endTime1] and
    event2 = [startTime2, endTime2].
    Event times are valid 24 hours format in the form of HH:MM.

    A conflict happens when two events have some non-empty intersection (i.e., some moment is common
    to both events).

    Return true if there is a conflict between two events. Otherwise, return false.

    Parameters
    ----------
    event1: list[str]

    event2: list[str]

    Returns
    -------
    out: bool

    Examples
    --------
    >>> haveConflict(["01:15","02:00"], ["02:00","03:00"])
    True

    Explanation: The two events intersect at time 2:00.

    >>> haveConflict(["01:00","02:00"], ["01:20","03:00"])
    True

    Explanation: The two events intersect starting from 01:20 to 02:00.

    >>> haveConflict(["10:00","11:00"], ["14:00","15:00"])
    False

    Explanation: The two events do not intersect.
    """
    start_time1, end_time1 = parse_time(event1[0]), parse_time(event1[1])
    start_time2, end_time2 = parse_time(event2[0]), parse_time(event2[1])
    return start_time1 <= start_time2 <= end_time1 or start_time2 <= start_time1 <= end_time2
