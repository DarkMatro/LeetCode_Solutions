def smallestNumber(num: int) -> int:
    """
    ID: 2165
    Tags:   Math, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    You are given an integer num. Rearrange the digits of num such that its value is minimized and
    it does not contain any leading zeros.

    Return the rearranged number with minimal value.

    Note that the sign of the number does not change after rearranging the digits.

    Parameters
    ----------
    num: int

    Returns
    -------
    int

    Examples
    --------
    >>> smallestNumber(310)
    103

    Explanation: The possible arrangements for the digits of 310 are 013, 031, 103, 130, 301, 310.
    The arrangement with the smallest value that does not contain any leading zeros is 103.

    >>> smallestNumber(-7605)
    -7650

    Explanation: Some possible arrangements for the digits of -7605 are -7650, -6705, -5076, -0567.
    The arrangement with the smallest value that does not contain any leading zeros is -7650.
    """
    digits = sorted(str(abs(num)), reverse=num < 0)  # if -ve sort in reverse
    # swap leading zeros for pos number
    if digits[0] == '0':
        for i in range(1, len(digits)):
            if digits[i] != '0':
                digits[0], digits[i] = digits[i], '0'
                break

    return int("".join(digits)) * (1 if num > 0 else -1)
