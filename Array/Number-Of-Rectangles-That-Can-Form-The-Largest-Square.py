from collections import Counter


def countGoodRectangles(rectangles: list[list[int]]) -> int:
    """
    ID: 1725
    Tags:   Array
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given an array rectangles where rectangles[i] = [li, wi] represents the ith rectangle of length li and
     width wi.

    You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi. For example,
    if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.

    Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.

    Return the number of rectangles that can make a square with a side length of maxLen.

    Parameters
    ----------
    rectangles: list[list[int]]

    Returns
    -------
    out : int

    Examples
    --------
    >>> countGoodRectangles([[5,8],[3,9],[5,12],[16,5]])
    3

    Explanation: The largest squares you can get from each rectangle are of lengths [5,3,5,5].
    The largest possible square is of length 5, and you can get it out of 3 rectangles.

    >>> countGoodRectangles([[2,3],[3,7],[4,3],[3,7]])
    3
    """
    max_lens = [min(i) for i in rectangles]
    return max_lens.count(max(max_lens))
