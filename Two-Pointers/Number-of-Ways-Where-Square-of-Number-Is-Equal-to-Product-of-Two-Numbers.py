from collections import Counter, defaultdict


def numTriplets(nums1: list[int], nums2: list[int]) -> int:
    """
    ID: 1577
    Tags: Array, Hash Table, Math, Two Pointers
    Time:   O(N^2 + M^2)
    Memory: O(N^2 + M^2)

    Task
    ----------
    Given two arrays of integers nums1 and nums2, return the number of triplets formed (type 1 and type 2) under the
    following rules:

    Type 1: Triplet (i, j, k) if nums1[i]2 == nums2[j] * nums2[k] where 0 <= i < nums1.length and 0 <= j < k <
    nums2.length.
    Type 2: Triplet (i, j, k) if nums2[i]2 == nums1[j] * nums1[k] where 0 <= i < nums2.length and 0 <= j < k <
    nums1.length.

    Parameters
    ----------
    nums1: list[int]

    nums2: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> numTriplets([7,4], [5,2,8,9])
    1

    Explanation: Type 1: (1, 1, 2), nums1[1]2 = nums2[1] * nums2[2]. (42 = 2 * 8).

    >>> numTriplets([1,1], [1,1,1])
    9

    Explanation: All Triplets are valid, because 12 = 1 * 1.
    Type 1: (0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2).  nums1[i]2 = nums2[j] * nums2[k].
    Type 2: (0,0,1), (1,0,1), (2,0,1). nums2[i]2 = nums1[j] * nums1[k].

    >>> numTriplets([7,7,8,3], [1,2,9,7])
    2

    Explanation: There are 2 valid triplets.
    Type 1: (3,0,2).  nums1[3]2 = nums2[0] * nums2[2].
    Type 2: (3,0,1).  nums2[3]2 = nums1[0] * nums1[1].

    """
    # Считаем квадраты
    freq1 = Counter(x * x for x in nums1)
    freq2 = Counter(x * x for x in nums2)

    # Функция для построения словаря произведений всех пар
    def build_prod_map(arr):
        prod_map = defaultdict(int)
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):  # только j > i
                prod = arr[i] * arr[j]
                prod_map[prod] += 1
        return prod_map

    # Словари произведений
    prod2 = build_prod_map(nums2)  # пары в nums2
    prod1 = build_prod_map(nums1)  # пары в nums1

    ans = 0
    # type 1: квадрат из nums1 против пар из nums2
    for sq, cnt in freq1.items():
        if sq in prod2:
            ans += cnt * prod2[sq]

    # type 2: квадрат из nums2 против пар из nums1
    for sq, cnt in freq2.items():
        if sq in prod1:
            ans += cnt * prod1[sq]

    return ans
