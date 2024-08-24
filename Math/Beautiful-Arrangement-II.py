def constructArray(n: int, k: int) -> list[int]:
    """
    ID: 667
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given two integers n and k, construct a list answer that contains n different positive integers
    ranging from 1 to n and obeys the following requirement:

    Suppose this list is answer = [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|,
    |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.
    Return the list answer. If there multiple valid answers, return any of them.

    Parameters
    ----------
    n: int

    k: int

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> constructArray(3, 1)
    [3, 2, 1]

    Explanation: The [1,2,3] has three different positive integers ranging from 1 to 3, and the
    [1,1] has exactly 1 distinct integer: 1

    >>> constructArray(3, 2)
    [3, 1, 2]

    Explanation: The [1,3,2] has three different positive integers ranging from 1 to 3, and the
    [2,1] has exactly 2 distinct integers: 1 and 2.
    """
    answer = []

    # Step 1: Create the first part with alternating high-low pattern
    left, right = 1, n
    for i in range(1, k + 1):
        if i % 2 == 0:
            answer.append(left)
            left += 1
        else:
            answer.append(right)
            right -= 1

    # Step 2: Fill the rest of the array in sequential order
    if k % 2 == 0:
        answer.extend(range(left, right + 1))
    else:
        answer.extend(range(right, left - 1, -1))

    return answer
