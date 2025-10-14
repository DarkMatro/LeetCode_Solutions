def earliestTime(tasks: list[list[int]]) -> int:
    """
    ID: 3683
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a 2D integer array tasks where tasks[i] = [si, ti].

    Each [si, ti] in tasks represents a task with start time si that takes ti units of time to finish.

    Return the earliest time at which at least one task is finished.

    Parameters
    ----------
    tasks: list[list[int]]

    Returns
    -------
    int

    Examples
    --------
    >>> earliestTime([[1,6],[2,3]])
    5

    Explanation:
    The first task starts at time t = 1 and finishes at time 1 + 6 = 7. The second task finishes at time 2 + 3 = 5.
    You can finish one task at time 5.

    >>> earliestTime([[100,100],[100,100],[100,100]])
    200

    Explanation:
    All three tasks finish at time 100 + 100 = 200.
    """
    return min([x[0] + x[1] for x in tasks])