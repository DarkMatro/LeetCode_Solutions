def isGood(nums: list[int]) -> bool:
    """
    ID: 2784
    Tags:   Array, Hash Table, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    You are given an integer array nums. We consider an array good if it is a permutation of an
    array base[n].

    base[n] = [1, 2, ..., n - 1, n, n] (in other words, it is an array of length n + 1 which
    contains 1 to n - 1 exactly once, plus two occurrences of n). For example, base[1] = [1, 1] and
    base[3] = [1, 2, 3, 3].

    Return true if the given array is good, otherwise return false.

    Note: A permutation of integers represents an arrangement of these numbers.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    bool

    Examples
    --------
    >>> isGood([2, 1, 3])
    False

    Explanation: Since the maximum element of the array is 3, the only candidate n for which this
    array could be a permutation of base[n], is n = 3. However, base[3] has four elements but array
    nums has three. Therefore, it can not be a permutation of base[3] = [1, 2, 3, 3]. So the answer
    is false.

    >>> isGood([1, 3, 3, 2])
    True

    Explanation: Since the maximum element of the array is 3, the only candidate n for which this
    array could be a permutation of base[n], is n = 3. It can be seen that nums is a permutation of
    base[3] = [1, 2, 3, 3] (by swapping the second and fourth elements in nums, we reach base[3]).
    Therefore, the answer is true.

    >>> isGood([1, 1])
    True

    Explanation: Since the maximum element of the array is 1, the only candidate n for which this
    array could be a permutation of base[n], is n = 1. It can be seen that nums is a permutation of
    base[1] = [1, 1]. Therefore, the answer is true.

    >>> isGood([3, 4, 4, 1, 2, 1])
    False

    Explanation: Since the maximum element of the array is 4, the only candidate n for which this
    array could be a permutation of base[n], is n = 4. However, base[4] has five elements but array
    nums has six. Therefore, it can not be a permutation of base[4] = [1, 2, 3, 4, 4]. So the answer
    is false.
    """
    d = {}
    max_v = 0
    for num in nums:
        d[num] = d.get(num, 0) + 1
        max_v = max(max_v, num)
    return len(nums) == max_v + 1 and d[max_v] == 2 and sorted(nums)[:-1] == [x for x in
                                                                              range(1, max_v + 1)]
