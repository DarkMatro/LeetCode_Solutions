def busyStudent(startTime: list[int], endTime: list[int], queryTime: int) -> int:
    """
    ID: 1450
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given two integer arrays startTime and endTime and given an integer queryTime.

    The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

    Return the number of students doing their homework at time queryTime. More formally, return the number of students
    where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

    Parameters
    ----------
    startTime : list[int]

    endTime : list[int]

    queryTime : int

    Returns
    -------
    out : int

    Examples
    --------
    >>> busyStudent([1,2,3], [3,2,7], 4)
    1
    Explanation: We have 3 students where:
    The first student started doing homework at time 1 and finished at time 3 and wasn't doing anything at time 4.
    The second student started doing homework at time 2 and finished at time 2 and also wasn't doing anything at time 4.
    The third student started doing homework at time 3 and finished at time 7 and was the only student doing homework at
    time 4.

    >>> busyStudent([4], [4], 4)
    1
    Explanation: The only student was doing their homework at the queryTime.
    """
    ans = 0
    for start, end in zip(startTime, endTime):
        if start <= queryTime <= end:
            ans += 1
    return ans
