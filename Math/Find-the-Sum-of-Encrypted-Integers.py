def sumOfEncryptedInt(nums: list[int]) -> int:
    """
    ID: 3079
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given an integer array nums containing positive integers. We define a function encrypt
    such that encrypt(x) replaces every digit in x with the largest digit in x. For example,
    encrypt(523) = 555 and encrypt(213) = 333.

    Return the sum of encrypted elements.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> sumOfEncryptedInt([1,2,3])
    6

    Explanation: The encrypted elements are [1,2,3]. The sum of encrypted elements is 1 + 2 + 3 == 6.

    >>> sumOfEncryptedInt([10,21,31])
    66

    Explanation: The encrypted elements are [11,22,33]. The sum of encrypted elements is 11 + 22 + 33 == 66.
    """
    ans = 0
    for num in nums:
        ans += encrypt(num)
    return ans


def encrypt(num: int) -> int:
    n = num + 0
    max_dig = 0
    m = 0
    while n != 0:
        max_dig = max(n % 10, max_dig)
        n //= 10
        m += 1
    ans = 0
    z = 1
    for _ in range(0, m):
        ans += max_dig * z
        z *= 10
    return ans
