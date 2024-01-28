def shuffle(nums: list[int], n: int) -> list[int]:
    """
    ID: 1470
    Tags:   Array
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

    Return the array in the form [x1,y1,x2,y2,...,xn,yn].

    Parameters
    ----------
    nums : list[int]

    n : int

    Returns
    -------
    out : int

    Examples
    --------
    >>> shuffle([2,5,1,3,4,7], 3)
    [2, 3, 5, 4, 1, 7]

    Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

    >>> shuffle([1,2,3,4,4,3,2,1], 4)
    [1, 4, 2, 3, 3, 2, 4, 1]


    >>> shuffle([1,1,2,2], 2)
    [1, 2, 1, 2]
    """
    ans = []
    for i in range(n):
        ans.append(nums[i])
        ans.append(nums[i + n])
    return ans
