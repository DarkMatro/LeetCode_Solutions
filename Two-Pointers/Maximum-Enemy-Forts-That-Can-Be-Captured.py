def captureForts(forts: list[int]) -> int:
    """
    ID: 2511
    Tags:   Array, Two Pointers
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a 0-indexed integer array forts of length n representing the positions of several forts. forts[i]
    can be -1, 0, or 1 where:

    -1 represents there is no fort at the ith position.
    0 indicates there is an enemy fort at the ith position.
    1 indicates the fort at the ith the position is under your command.
    Now you have decided to move your army from one of your forts at position i to an empty position j such that:

    0 <= i, j <= n - 1
    The army travels over enemy forts only. Formally, for all k where min(i,j) < k < max(i,j), forts[k] == 0.
    While moving the army, all the enemy forts that come in the way are captured.

    Return the maximum number of enemy forts that can be captured. In case it is impossible to move your army, or you
    do not have any fort under your command, return 0.

    Parameters
    ----------
    forts: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> captureForts([1,0,0,-1,0,0,0,0,1])
    4

    Explanation:
    - Moving the army from position 0 to position 3 captures 2 enemy forts, at 1 and 2.
    - Moving the army from position 8 to position 3 captures 4 enemy forts.
    Since 4 is the maximum number of enemy forts that can be captured, we return 4.

    >>> captureForts([0,0,1,-1])
    0

    Explanation: Since no enemy fort can be captured, 0 is returned.
    """
    max_f = 0
    cnt = -1
    for x in forts:
        if x == 1:
            cnt = 0
            if cnt > 0:
                max_f = max(max_f, cnt)
                cnt = -1
            continue
        elif x == 0 and cnt >= 0:
            cnt += 1
        elif x == -1:
            max_f = max(max_f, cnt)
            cnt = -1
            cnt = -1
    for x in reversed(forts):
        if x == 1:
            cnt = 0
            if cnt > 0:
                max_f = max(max_f, cnt)
                cnt = -1
            continue
        elif x == 0 and cnt >= 0:
            cnt += 1
        elif x == -1:
            max_f = max(max_f, cnt)
            cnt = -1
    return max_f

