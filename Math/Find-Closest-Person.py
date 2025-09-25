def findClosest(x: int, y: int, z: int) -> int:
    """
    ID: 3516
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    You are given three integers x, y, and z, representing the positions of three people on a number line:

    x is the position of Person 1.
    y is the position of Person 2.
    z is the position of Person 3, who does not move.
    Both Person 1 and Person 2 move toward Person 3 at the same speed.

    Determine which person reaches Person 3 first:

    Return 1 if Person 1 arrives first.
    Return 2 if Person 2 arrives first.
    Return 0 if both arrive at the same time.
    Return the result accordingly.

    Parameters
    ----------
    x: int

    y: int

    z: int

    Returns
    -------
    int

    Examples
    --------
    >>> findClosest(2, 7, 4)
    1

    Explanation:
    Person 1 is at position 2 and can reach Person 3 (at position 4) in 2 steps.
    Person 2 is at position 7 and can reach Person 3 in 3 steps.
    Since Person 1 reaches Person 3 first, the output is 1.

    >>> findClosest(2, 5, 6)
    2

    Explanation:
    Person 1 is at position 2 and can reach Person 3 (at position 6) in 4 steps.
    Person 2 is at position 5 and can reach Person 3 in 1 step.
    Since Person 2 reaches Person 3 first, the output is 2.

    >>> findClosest(1, 5, 3)
    0

    Explanation:
    Person 1 is at position 1 and can reach Person 3 (at position 3) in 2 steps.
    Person 2 is at position 5 and can reach Person 3 in 2 steps.
    Since both Person 1 and Person 2 reach Person 3 at the same time, the output is 0.
    """
    d1 = abs(z - x)
    d2 = abs(z - y)
    if d1 < d2:
        return 1
    elif d2 < d1:
        return 2
    else:
        return 0
