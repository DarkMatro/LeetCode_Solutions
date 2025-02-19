def minDifference(nums: list[int], queries: list[list[int]]) -> list[int]:
    """
    ID: 1906
    Tags: Array, Hash Table
    Time: O(N + Q)
    Memory: O(100N)

    Task
    ----------
    The minimum absolute difference of an array a is defined as the minimum value of |a[i] - a[j]|,
    where 0 <= i < j < a.length and a[i] != a[j]. If all elements of a are the same, the minimum
    absolute difference is -1.

    For example, the minimum absolute difference of the array [5,2,3,7,2] is |2 - 3| = 1. Note that
    it is not 0 because a[i] and a[j] must be different.
    You are given an integer array nums and the array queries where queries[i] = [li, ri]. For each
    query i, compute the minimum absolute difference of the subarray nums[li...ri] containing the
    elements of nums between the 0-based indices li and ri (inclusive).

    Return an array ans where ans[i] is the answer to the ith query.

    A subarray is a contiguous sequence of elements in an array.

    The value of |x| is defined as:

    x if x >= 0.
    -x if x < 0.

    Parameters
    ----------
    nums: list[int]

    queries: list[list[int]]

    Returns
    -------
    list[int]

    Examples
    --------
    >>> minDifference([1,3,4,8], [[0,1],[1,2],[2,3],[0,3]])
    [2, 1, 4, 1]

    Explanation:
    The queries are processed as follows:
    - queries[0] = [0,1]: The subarray is [1,3] and the minimum absolute difference is |1-3| = 2.
    - queries[1] = [1,2]: The subarray is [3,4] and the minimum absolute difference is |3-4| = 1.
    - queries[2] = [2,3]: The subarray is [4,8] and the minimum absolute difference is |4-8| = 4.
    - queries[3] = [0,3]: The subarray is [1,3,4,8] and the minimum absolute difference is |3-4| = 1.

    >>> minDifference([4,5,2,2,7,10], [[2,3],[0,2],[0,5],[3,5]])
    [-1, 1, 1, 3]

    Explanation:
    The queries are processed as follows:
    - queries[0] = [2,3]: The subarray is [2,2] and the minimum absolute difference is -1 because all the
      elements are the same.
    - queries[1] = [0,2]: The subarray is [4,5,2] and the minimum absolute difference is |4-5| = 1.
    - queries[2] = [0,5]: The subarray is [4,5,2,2,7,10] and the minimum absolute difference is |4-5| = 1.
    - queries[3] = [3,5]: The subarray is [2,7,10] and the minimum absolute difference is |7-10| = 3.
    """
    MAX_VAL = 100  # Since 1 <= nums[i] <= 100
    n = len(nums)

    # Step 1: Build prefix frequency array
    freq = [[0] * (MAX_VAL + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(1, MAX_VAL + 1):
            freq[i + 1][j] = freq[i][j]  # Carry forward previous counts
        freq[i + 1][nums[i]] += 1  # Add current number

    result = []

    # Step 2: Process each query
    for li, ri in queries:
        # Get unique elements in range [li, ri]
        unique_numbers = []
        for val in range(1, MAX_VAL + 1):
            if freq[ri + 1][val] - freq[li][val] > 0:
                unique_numbers.append(val)

        # Step 3: Compute minimum absolute difference
        if len(unique_numbers) < 2:
            result.append(-1)
        else:
            min_diff = float('inf')
            for i in range(1, len(unique_numbers)):
                min_diff = min(min_diff, unique_numbers[i] - unique_numbers[i - 1])
            result.append(min_diff)

    return result

