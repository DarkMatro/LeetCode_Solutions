def distributeCandies(candyType: list[int]) -> int:
    """
    ID: 575
    Tags:   Array, Hash Table
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started
    to gain weight, so she visited a doctor.

    The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice
    likes her candies very much, and she wants to eat the maximum number of different types of
    candies while still following the doctor's advice.

    Given the integer array candyType of length n, return the maximum number of different types of
    candies she can eat if she only eats n / 2 of them.

    Parameters
    ----------
    candyType: list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> distributeCandies([1,1,2,2,3,3])
    3

    Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one
    of each type.

    >>> distributeCandies([1,1,2,3])
    2

    Explanation: Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2], [1,3],
    or [2,3], she still can only eat 2 different types.

    >>> distributeCandies([6,6,6,6])
    1

    Explanation: Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only
    has 1 type.
    """
    return min(len(candyType) // 2, len(set(candyType)))
