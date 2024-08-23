def angleClock(hour: int, minutes: int) -> float:
    """
    ID: 1344
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the
    hour and the minute hand.

    Answers within 10-5 of the actual value will be accepted as correct.

    Parameters
    ----------
    hour: int

    minutes: int

    Returns
    -------
    out : float

    Examples
    --------
    >>> angleClock(12, 30)
    165.0

    >>> angleClock(3, 30)
    75.0

    >>> angleClock(3, 15)
    7.5
    """
    minutes_angle = minutes * 6.
    minutes_angle %= 360
    hour_angle = hour * 30. + (minutes * 30. / 60.)
    hour_angle %= 360
    return min(abs(hour_angle - minutes_angle), abs((360 - minutes_angle) + hour_angle),
               abs((360 - hour_angle) + minutes_angle))
