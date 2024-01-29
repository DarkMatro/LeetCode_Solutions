def sumIndicesWithKSetBits(nums: list[int], k: int) -> int:
    """
    ID: 2859
    Tags:   Array, Bit Manipulation
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a 0-indexed integer array nums and an integer k.

    Return an integer that denotes the sum of elements in nums whose corresponding indices have exactly k set bits in
    their binary representation.

    The set bits in an integer are the 1's present when it is written in binary.

    For example, the binary representation of 21 is 10101, which has 3 set bits.

    Parameters
    ----------
    nums: list[int]

    k: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> sumIndicesWithKSetBits([5,10,1,5,2], 1)
    13

    Explanation: The binary representation of the indices are:
    0 = 0b000
    1 = 0b001
    2 = 0b010
    3 = 0b011
    4 = 0b100
    Indices 1, 2, and 4 have k = 1 set bits in their binary representation.
    Hence, the answer is nums[1] + nums[2] + nums[4] = 13.

    >>> sumIndicesWithKSetBits([4,3,2,1], 2)
    1

    Explanation: The binary representation of the indices are:
    0 = 0b002
    1 = 0b012
    2 = 0b102
    3 = 0b112
    Only index 3 has k = 2 set bits in its binary representation.
    Hence, the answer is nums[3] = 1.
    """
    max_k = 0
    for i, n in enumerate(nums):
        if i.bit_count() == k:
            max_k += n
    return max_k

