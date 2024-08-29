def addNegabinary(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    ID: 1073
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given two numbers arr1 and arr2 in base -2, return the result of adding them together.

    Each number is given in array format:  as an array of 0s and 1s, from most significant bit to
    least significant bit.  For example, arr = [1,1,0,1] represents the number
    (-2)^3 + (-2)^2 + (-2)^0 = -3.  A number arr in array, format is also guaranteed to have no
    leading zeros: either arr == [0] or arr[0] == 1.

    Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no
    leading zeros.

    Parameters
    ----------
    arr1: list[int]

    arr2: list[int]

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> addNegabinary([1,1,1,1,1], [1,0,1])
    [1, 0, 0, 0, 0]

    Explanation: arr1 represents 11, arr2 represents 5, the output represents 16.

    >>> addNegabinary([0], [0])
    [0]

    >>> addNegabinary([0], [1])
    [1]
    """
    # Reverse arrays to make least significant bit at index 0
    arr1.reverse()
    arr2.reverse()

    # Resultant array
    result = []

    carry = 0
    n = max(len(arr1), len(arr2))

    for i in range(n):
        # Add current bits plus carry
        bit1 = arr1[i] if i < len(arr1) else 0
        bit2 = arr2[i] if i < len(arr2) else 0
        total = bit1 + bit2 + carry

        # Handle base -2 logic
        if total == 0 or total == 1:
            result.append(total)
            carry = 0
        elif total == 2:
            result.append(0)
            carry = -1
        elif total == 3:
            result.append(1)
            carry = -1
        elif total == -1:
            result.append(1)
            carry = 1

    # If there's a carry left
    while carry != 0:
        total = carry
        if total == 1:
            result.append(1)
            carry = 0
        elif total == -1:
            result.append(1)
            carry = 1
        elif total == 2:
            result.append(0)
            carry = -1

    # Remove leading zeros and reverse back
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    result.reverse()
    return result
