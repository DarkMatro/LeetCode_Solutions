def canAliceWin(nums: list[int]) -> bool:
    """
    ID: 3232
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given an array of positive integers nums.

    Alice and Bob are playing a game. In the game, Alice can choose either all single-digit numbers
    or all double-digit numbers from nums, and the rest of the numbers are given to Bob. Alice wins
    if the sum of her numbers is strictly greater than the sum of Bob's numbers.

    Return true if Alice can win this game, otherwise, return false.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : boo

    Examples
    --------
    >>> canAliceWin([1,2,3,4,10])
    False

    Explanation: Alice cannot win by choosing either single-digit or double-digit numbers.

    >>> canAliceWin([1,2,3,4,5,14])
    True

    Explanation: Alice can win by choosing single-digit numbers which have a sum equal to 15.

    >>> canAliceWin([5,5,5,25])
    True

    Explanation: Alice can win by choosing double-digit numbers which have a sum equal to 25.
    """
    one_dig = 0
    two_dig = 0
    for i in nums:
        if i < 10:
            one_dig += i
        else:
            two_dig += i
    return one_dig != two_dig
