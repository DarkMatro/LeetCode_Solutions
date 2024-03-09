def maxScoreIndices(nums: list[int]) -> list[int]:
    """
    ID: 2155
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a 0-indexed binary array nums of length n. nums can be divided at index i (where 0 <= i <= n) into
    two arrays (possibly empty) numsleft and numsright:

    numsleft has all the elements of nums between index 0 and i - 1 (inclusive), while numsright has all the elements
    of nums between index i and n - 1 (inclusive).
    If i == 0, numsleft is empty, while numsright has all the elements of nums.
    If i == n, numsleft has all the elements of nums, while numsright is empty.
    The division score of an index i is the sum of the number of 0's in numsleft and the number of 1's in numsright.

    Return all distinct indices that have the highest possible division score. You may return the answer in any order.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> maxScoreIndices([0,0,1,0])
    [2, 4]

    Explanation: Division at index
    - 0: numsleft is []. numsright is [0,0,1,0]. The score is 0 + 1 = 1.
    - 1: numsleft is [0]. numsright is [0,1,0]. The score is 1 + 1 = 2.
    - 2: numsleft is [0,0]. numsright is [1,0]. The score is 2 + 1 = 3.
    - 3: numsleft is [0,0,1]. numsright is [0]. The score is 2 + 0 = 2.
    - 4: numsleft is [0,0,1,0]. numsright is []. The score is 3 + 0 = 3.
    Indices 2 and 4 both have the highest possible division score 3.
    Note the answer [4,2] would also be accepted.

    >>> maxScoreIndices([0,0,0])
    [3]

    Explanation: Division at index
    - 0: numsleft is []. numsright is [0,0,0]. The score is 0 + 0 = 0.
    - 1: numsleft is [0]. numsright is [0,0]. The score is 1 + 0 = 1.
    - 2: numsleft is [0,0]. numsright is [0]. The score is 2 + 0 = 2.
    - 3: numsleft is [0,0,0]. numsright is []. The score is 3 + 0 = 3.
    Only index 3 has the highest possible division score 3.

    >>> maxScoreIndices([1,1])
    [0]

    Explanation: Division at index
    - 0: numsleft is []. numsright is [1,1]. The score is 0 + 2 = 2.
    - 1: numsleft is [1]. numsright is [1]. The score is 0 + 1 = 1.
    - 2: numsleft is [1,1]. numsright is []. The score is 0 + 0 = 0.
    Only index 0 has the highest possible division score 2.
    """
    total_ones = sum(nums)
    total_zeros = 0
    max_score = total_ones
    idx = [0]
    for i in range(len(nums)):
        num = nums[i]
        if num == 0:
            total_zeros += 1
        else:
            total_ones -= 1
        score = total_zeros + total_ones
        if score > max_score:
            idx = [i + 1]
            max_score = score
        elif score == max_score:
            idx.append(i + 1)
    return idx
