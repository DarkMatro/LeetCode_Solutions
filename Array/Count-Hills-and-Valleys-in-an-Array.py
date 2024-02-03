def countHillValley(nums: list[int]) -> int:
    """
    ID: 2210
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal
    neighbors of i are smaller than nums[i]. Similarly, an index i is part of a valley in nums if the closest
    non-equal neighbors of i are larger than nums[i]. Adjacent indices i and j are part of the same hill or valley if
    nums[i] == nums[j].

    Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right
    of the index.

    Return the number of hills and valleys in nums.

    Parameters
    ----------
    nums : list[int]

    Returns
    -------
    out : bool

    Examples
    --------
    >>> countHillValley([2,4,1,1,6,5])
    3

    Explanation:
    At index 0: There is no non-equal neighbor of 2 on the left, so index 0 is neither a hill nor a valley.
    At index 1: The closest non-equal neighbors of 4 are 2 and 1. Since 4 > 2 and 4 > 1, index 1 is a hill.
    At index 2: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index 2 is a valley.
    At index 3: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index 3 is a valley, but note
    that it is part of the same valley as index 2.
    At index 4: The closest non-equal neighbors of 6 are 1 and 5. Since 6 > 1 and 6 > 5, index 4 is a hill.
    At index 5: There is no non-equal neighbor of 5 on the right, so index 5 is neither a hill nor a valley.
    There are 3 hills and valleys so we return 3.

    >>> countHillValley([6,6,5,5,4,1])
    0

    Explanation:
    At index 0: There is no non-equal neighbor of 6 on the left, so index 0 is neither a hill nor a valley.
    At index 1: There is no non-equal neighbor of 6 on the left, so index 1 is neither a hill nor a valley.
    At index 2: The closest non-equal neighbors of 5 are 6 and 4. Since 5 < 6 and 5 > 4, index 2 is neither a hill nor
    a valley.
    At index 3: The closest non-equal neighbors of 5 are 6 and 4. Since 5 < 6 and 5 > 4, index 3 is neither a hill nor
    a valley.
    At index 4: The closest non-equal neighbors of 4 are 5 and 1. Since 4 < 5 and 4 > 1, index 4 is neither a hill nor
    a valley.
    At index 5: There is no non-equal neighbor of 1 on the right, so index 5 is neither a hill nor a valley.
    There are 0 hills and valleys so we return 0.
    """
    ans = 0
    for i in range(1, len(nums) - 1):
        cur_v = nums[i]
        prev_v = nums[i - 1]
        if cur_v == prev_v:
            continue
        for num_j in reversed(nums[:i]):
            if num_j != cur_v:
                prev_v = num_j
                break
        next_v = nums[i + 1]
        for num_j in nums[i + 1:]:
            if num_j != cur_v:
                next_v = num_j
                break
        if prev_v < cur_v > next_v or prev_v > cur_v < next_v:
            ans += 1
    return ans

