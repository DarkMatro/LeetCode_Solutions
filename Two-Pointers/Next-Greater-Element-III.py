def nextGreaterElement(n: int) -> int:
    """
    ID: 556
    Tags: Math, Two Pointers, String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n
    and is greater in value than n. If no such positive integer exists, return -1.

    Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in
    32-bit integer, return -1.

    Parameters
    ----------
    n: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> nextGreaterElement(12)
    21

    >>> nextGreaterElement(21)
    -1

    """
    digits = list(str(n))
    i = len(digits) - 2

    # Step 1: find pivot
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    if i < 0:
        return -1  # already max permutation

    # Step 2: find successor
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1

    # Step 3: swap
    digits[i], digits[j] = digits[j], digits[i]

    # Step 4: reverse suffix
    digits[i + 1:] = reversed(digits[i + 1:])

    result = int("".join(digits))

    # Step 5: check 32-bit
    return result if result <= 2 ** 31 - 1 else -1
