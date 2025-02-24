def flipgame(fronts: list[int], backs: list[int]) -> int:
    """
    ID: 822
    Tags: Array, Hash Table
    Time: O(N)
    Memory: O(1)

    Task
    ----------
    You are given two 0-indexed integer arrays fronts and backs of length n, where the ith card has
    the positive integer fronts[i] printed on the front and backs[i] printed on the back. Initially,
    each card is placed on a table such that the front number is facing up and the other is facing
    down. You may flip over any number of cards (possibly zero).

    After flipping the cards, an integer is considered good if it is facing down on some card and
    not facing up on any card.

    Return the minimum possible good integer after flipping the cards. If there are no good
    integers, return 0.

    Parameters
    ----------
    fronts: list[int]

    backs: list[int]

    Returns
    -------
    int

    Examples
    --------
    >>> flipgame([1,2,4,4,7], [1,3,4,1,3])
    2

    Explanation:
    If we flip the second card, the face up numbers are [1,3,4,4,7] and the face down are [1,2,4,1,3].
    2 is the minimum good integer as it appears facing down but not facing up.
    It can be shown that 2 is the minimum possible good integer obtainable after flipping some cards.

    >>> flipgame([1], [1])
    0

    Explanation:
    There are no good integers no matter how we flip the cards, so we return 0.
    """
    return min(set(fronts + backs) - {f for f, b in zip(fronts, backs) if f == b}, default=0)
