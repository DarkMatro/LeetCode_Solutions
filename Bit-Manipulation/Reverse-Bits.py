def reverse_bits(n: int) -> int:
    """
    ID: 0190
    Tags:   Divide and Conquer, Bit Manipulation
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Reverse bits of a given 32 bits unsigned integer.

    Parameters
    ----------
    n : int

    Returns
    -------
    res : int

    Examples
    --------
    >>> reverse_bits(0b00000010100101000001111010011100)
    964176192

    Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so
     return 964176192 which its binary representation is 00111001011110000010100101000000.

    >>> reverse_bits(0b11111111111111111111111111111101)
    3221225471

    Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293,
     so return 3221225471 which its binary representation is 10111111111111111111111111111111.
    """
    rev_num = 0
    for i in range(32):
        rev_num = (rev_num << 1) | n & 1
        n >>= 1
    return rev_num

