from math import floor

def accountBalanceAfterPurchase(purchaseAmount: int) -> int:
    """
    ID: 2806
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Initially, you have a bank account balance of 100 dollars.

    You are given an integer purchaseAmount representing the amount you will spend on a purchase in
    dollars, in other words, its price.

    When making the purchase, first the purchaseAmount is rounded to the nearest multiple of 10. Let
    us call this value roundedAmount. Then, roundedAmount dollars are removed from your bank account

    Return an integer denoting your final bank account balance after this purchase.

    Notes:

    0 is considered to be a multiple of 10 in this problem.
    When rounding, 5 is rounded upward (5 is rounded to 10, 15 is rounded to 20, 25 to 30, and so
    on).

    Parameters
    ----------
    purchaseAmount: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> accountBalanceAfterPurchase(9)
    90

    Explanation: The nearest multiple of 10 to 9 is 10. So your account balance becomes
    100 - 10 = 90.

    >>> accountBalanceAfterPurchase(15)
    80

    Explanation: The nearest multiple of 10 to 15 is 20. So your account balance becomes
    100 - 20 = 80.

    >>> accountBalanceAfterPurchase(10)
    90

    Explanation: 10 is a multiple of 10 itself. So your account balance becomes 100 - 10 = 90.
    """
    return 100 - floor((purchaseAmount + 5) / 10) * 10
