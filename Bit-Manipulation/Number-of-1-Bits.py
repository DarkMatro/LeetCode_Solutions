def hamming_weight(n: int) -> int:
    """
    ID: 0191
    Tags:   Divide and Conquer, Bit Manipulation
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it
    has (also known as the Hamming weight).

    Parameters
    ----------
    n : int

    Returns
    -------
    res : int

    Examples
    --------
    >>> hamming_weight(0b00000000000000000000000000001011)
    3

    Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

    >>> hamming_weight(0b00000000000000000000000010000000)
    1

    Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

    >>> hamming_weight(0b11111111111111111111111111111101)
    31

    Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
    """
    res = 0
    while n != 0:
        res += n & 1
        n >>= 1
    return res

