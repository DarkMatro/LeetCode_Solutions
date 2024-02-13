def isOneBitCharacter(bits: list[int]) -> bool:
    """
    ID: 0717
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    We have two special characters:

    The first character can be represented by one bit 0.
    The second character can be represented by two bits (10 or 11).
    Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

    Parameters
    ----------
    bits : list[int]

    Returns
    -------
    out : bool

    Examples
    --------
    >>> isOneBitCharacter([1,0,0])
    True

    Explanation: The only way to decode it is two-bit character and one-bit character.
    So the last character is one-bit character.

    >>> isOneBitCharacter([1,1,1,0])
    False

    Explanation: The only way to decode it is two-bit character and two-bit character.
    So the last character is not one-bit character.
    """
    i = 0
    n = len(bits)
    while i < n - 1:
        if bits[i] == 0:
            i += 1
        else:
            i += 2
    return n - i == 1
