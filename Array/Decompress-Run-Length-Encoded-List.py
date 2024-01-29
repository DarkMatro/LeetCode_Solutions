def decompressRLElist(nums: list[int]) -> list[int]:
    """
    ID: 1313
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    We are given a list nums of integers representing a list compressed with run-length encoding.

    Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair,
    there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right
    to generate the decompressed list.

    Return the decompressed list.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> decompressRLElist([1,2,3,4])
    [2, 4, 4, 4]

    Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
    The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
    At the end the concatenation [2] + [4,4,4] is [2,4,4,4].

    >>> decompressRLElist([1,1,2,3])
    [1, 3, 3]
    """
    ans = []
    for i in range(0, len(nums), 2):
        arr = [nums[i + 1]] * nums[i]
        ans.extend(arr)
    return ans
