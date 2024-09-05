def numberOfSteps(num: int) -> int:
    """
    ID: 1342
    Tags:   Math, Bit Manipulation
    Time:   O(logN)
    Memory: O(1)

    Task
    ----------
    Given an integer num, return the number of steps to reduce it to zero.

    In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.


    Parameters
    ----------
    num : int

    Returns
    -------
    out : int

    Examples
    --------
    >>> numberOfSteps(14)
    6

    Explanation:
    Step 1) 14 is even; divide by 2 and obtain 7.
    Step 2) 7 is odd; subtract 1 and obtain 6.
    Step 3) 6 is even; divide by 2 and obtain 3.
    Step 4) 3 is odd; subtract 1 and obtain 2.
    Step 5) 2 is even; divide by 2 and obtain 1.
    Step 6) 1 is odd; subtract 1 and obtain 0.

    >>> numberOfSteps(8)
    4
    Explanation:
    Step 1) 8 is even; divide by 2 and obtain 4.
    Step 2) 4 is even; divide by 2 and obtain 2.
    Step 3) 2 is even; divide by 2 and obtain 1.
    Step 4) 1 is odd; subtract 1 and obtain 0.

    >>> numberOfSteps(123)
    12
    """
    res = 0
    while num != 0:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        res += 1
    return res
