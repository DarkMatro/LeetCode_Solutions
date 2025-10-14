def minSwaps(nums: list[int]) -> int:
    """
    ID: 3551
    Tags:   Array, Hash Table, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    You are given an array nums of distinct positive integers. You need to sort the array in increasing order based on
    the sum of the digits of each number. If two numbers have the same digit sum, the smaller number appears first in
    the sorted order.

    Return the minimum number of swaps required to rearrange nums into this sorted order.

    A swap is defined as exchanging the values at two distinct positions in the array.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> minSwaps([37,100])
    1

    Explanation:
    Compute the digit sum for each integer: [3 + 7 = 10, 1 + 0 + 0 = 1] → [10, 1]
    Sort the integers based on digit sum: [100, 37]. Swap 37 with 100 to obtain the sorted order.
    Thus, the minimum number of swaps required to rearrange nums is 1.

    >>> minSwaps([22,14,33,7])
    0

    Explanation:
    Compute the digit sum for each integer: [2 + 2 = 4, 1 + 4 = 5, 3 + 3 = 6, 7 = 7] → [4, 5, 6, 7]
    Sort the integers based on digit sum: [22, 14, 33, 7]. The array is already sorted.
    Thus, the minimum number of swaps required to rearrange nums is 0.

    >>> minSwaps([18,43,34,16])
    2

    Explanation:
    Compute the digit sum for each integer: [1 + 8 = 9, 4 + 3 = 7, 3 + 4 = 7, 1 + 6 = 7] → [9, 7, 7, 7]
    Sort the integers based on digit sum: [16, 34, 43, 18]. Swap 18 with 16, and swap 43 with 34 to obtain the sorted order.
    Thus, the minimum number of swaps required to rearrange nums is 2.
    """
    sorted_nums = sorted(nums, key=lambda x: (digits_sum(x), x))

    # 2️⃣ Map value → target index
    index_map = {num: i for i, num in enumerate(sorted_nums)}

    # 3️⃣ Count cycles in current → target permutation
    visited = [False] * len(nums)
    swaps = 0

    for i in range(len(nums)):
        # already visited or already in correct position
        if visited[i] or index_map[nums[i]] == i:
            continue

        # cycle detection
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = index_map[nums[j]]
            cycle_size += 1

        if cycle_size > 1:
            swaps += cycle_size - 1

    return swaps


def digits_sum(n: int) -> int:
    digits = []
    while n != 0:
        digits.append(n % 10)
        n //= 10
    return sum(digits)
