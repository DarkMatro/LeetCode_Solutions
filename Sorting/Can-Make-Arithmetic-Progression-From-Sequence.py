def canMakeArithmeticProgression(arr: list[int]) -> bool:
    """
    ID: 1502
    Tags:   Array, Sorting
    Time:   O(NlogN)
    Memory: O(1)

    Task
    ----------
    A sequence of numbers is called an arithmetic progression if the difference between any two
    consecutive elements is the same.

    Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic
    progression. Otherwise, return false.

    Parameters
    ----------
    arr: list[int]

    Returns
    -------
    bool

    Examples
    --------
    >>> canMakeArithmeticProgression([3,5,1])
    True

    Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2
    respectively, between each consecutive elements.

    >>> canMakeArithmeticProgression([1,2,4])
    False

    Explanation: There is no way to reorder the elements to obtain an arithmetic progression.
    """
    arr.sort()
    diff = arr[1] - arr[0]
    prev = arr[1]
    for i, x in enumerate(arr):
        if i < 2:
            continue
        if x - prev != diff:
            return False
        prev = x
    return True
