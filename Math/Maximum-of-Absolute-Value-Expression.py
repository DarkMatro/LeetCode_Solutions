def maxAbsValExpr(arr1: list[int], arr2: list[int]) -> int:
    """
    ID: 1131
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given two arrays of integers with equal lengths, return the maximum value of:

    |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

    where the maximum is taken over all 0 <= i, j < arr1.length.

    Parameters
    ----------
    arr1: list[int]

    arr2: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> maxAbsValExpr([1,2,3,4], [-1,4,5,6])
    13

    >>> maxAbsValExpr([1,-2,-5,0,10], [0,-2,-1,-7,-4])
    20
    """
    max1 = max2 = max3 = max4 = float('-inf')
    min1 = min2 = min3 = min4 = float('inf')

    for i in range(len(arr1)):
        # Four possible expressions
        expr1 = arr1[i] + arr2[i] + i
        expr2 = arr1[i] + arr2[i] - i
        expr3 = arr1[i] - arr2[i] + i
        expr4 = arr1[i] - arr2[i] - i

        # Update max and min for each expression
        max1 = max(max1, expr1)
        min1 = min(min1, expr1)

        max2 = max(max2, expr2)
        min2 = min(min2, expr2)

        max3 = max(max3, expr3)
        min3 = min(min3, expr3)

        max4 = max(max4, expr4)
        min4 = min(min4, expr4)

    # Calculate the maximum difference for each case
    return max(max1 - min1, max2 - min2, max3 - min3, max4 - min4)
