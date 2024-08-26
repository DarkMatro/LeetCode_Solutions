def numOfBurgers(tomatoSlices: int, cheeseSlices: int) -> list[int]:
    """
    ID: 1276
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Given two integers tomatoSlices and cheeseSlices. The ingredients of different burgers are as
    follows:

    Jumbo Burger: 4 tomato slices and 1 cheese slice.
    Small Burger: 2 Tomato slices and 1 cheese slice.
    Return [total_jumbo, total_small] so that the number of remaining tomatoSlices equal to 0 and
    the number of remaining cheeseSlices equal to 0. If it is not possible to make the remaining
    tomatoSlices and cheeseSlices equal to 0 return [].

    Parameters
    ----------
    tomatoSlices: int

    cheeseSlices: int

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> numOfBurgers(16, 7)
    [1, 6]

    Explantion: To make one jumbo burger and 6 small burgers we need 4*1 + 2*6 = 16 tomato and
    1 + 6 = 7 cheese. There will be no remaining ingredients.

    >>> numOfBurgers(17, 4)
    []

    Explantion: There will be no way to use all ingredients to make small and jumbo burgers.

    >>> numOfBurgers(4, 17)
    []

    Explantion:  Making 1 jumbo burger there will be 16 cheese remaining and making 2 small burgers
    there will be 15 cheese remaining.
    """
    if tomatoSlices % 2 != 0:
        return []
    x = tomatoSlices // 2 - cheeseSlices
    y = 2 * cheeseSlices - tomatoSlices // 2
    if x % 1 != 0 or y % 1 != 0 or x < 0 or y < 0:
        return []
    return [x, y]

