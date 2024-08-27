def numberOfRounds(loginTime: str, logoutTime: str) -> int:
    """
    ID: 1904
    Tags:   Math, String
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    You are participating in an online chess tournament. There is a chess round that starts every 15
    minutes. The first round of the day starts at 00:00, and after every 15 minutes, a new round
    starts.

    For example, the second round starts at 00:15, the fourth round starts at 00:45, and the seventh
    round starts at 01:30.
    You are given two strings loginTime and logoutTime where:

    loginTime is the time you will login to the game, and
    logoutTime is the time you will logout from the game.
    If logoutTime is earlier than loginTime, this means you have played from loginTime to midnight
    and from midnight to logoutTime.

    Return the number of full chess rounds you have played in the tournament.

    Note: All the given times follow the 24-hour clock. That means the first round of the day starts
    at 00:00 and the last round of the day starts at 23:45.

    Parameters
    ----------
    loginTime: str

    logoutTime: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> numberOfRounds("09:31", "10:14")
    1

    Explanation: You played one full round from 09:45 to 10:00.
    You did not play the full round from 09:30 to 09:45 because you logged in at 09:31 after it
    began.
    You did not play the full round from 10:00 to 10:15 because you logged out at 10:14 before it
    ended.

    >>> numberOfRounds("21:30", "03:00")
    22

    Explanation: You played 10 full rounds from 21:30 to 00:00 and 12 full rounds from 00:00 to
    03:00. 10 + 12 = 22.
    """
    in_min = int(loginTime[:2]) * 60 + int(loginTime[3:])
    out_min = int(logoutTime[:2]) * 60 + int(logoutTime[3:])
    if out_min > in_min and out_min - in_min < 15:
        return 0
    if in_min % 15 != 0:
        in_min += 15 - in_min % 15
    if out_min % 15 != 0:
        out_min -= out_min % 15
    if out_min < in_min:
        return (1440 - in_min + out_min) // 15
    return (out_min - in_min) // 15
