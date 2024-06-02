def createTargetArray(nums: list[int], index: list[int]) -> list[int]:
    """
    ID: 1389
    Tags:   Array, Simulation
    Time:   O(N^2)
    Memory: O(1)

    Task
    ----------
    Given two arrays of integers nums and index. Your task is to create target array under the following rules:

    Initially target array is empty.
    From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
    Repeat the previous step until there are no elements to read in nums and index.
    Return the target array.

    It is guaranteed that the insertion operations will be valid.

    Parameters
    ----------
    nums : list[int]

    index: list[int]

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> createTargetArray([0,1,2,3,4], [0,1,2,2,1])
    [0, 4, 1, 3, 2]

    Explanation:
    nums       index     target
    0            0        [0]
    1            1        [0,1]
    2            2        [0,1,2]
    3            2        [0,1,3,2]
    4            1        [0,4,1,3,2]

    >>> createTargetArray([1,2,3,4,0], [0,1,2,3,0])
    [0, 1, 2, 3, 4]

    Explanation:
    nums       index     target
    1            0        [1]
    2            1        [1,2]
    3            2        [1,2,3]
    4            3        [1,2,3,4]
    0            0        [0,1,2,3,4]

    >>> createTargetArray([1], [0])
    [1]
    """
    arr = []
    for i, n in enumerate(nums):
        arr.insert(index[i], n)
    return arr
