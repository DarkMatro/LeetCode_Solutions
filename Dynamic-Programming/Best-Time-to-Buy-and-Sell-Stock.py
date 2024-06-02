def max_profit(prices: list[int]) -> int:
    """
    ID: 0121
    Tags:   Array, Dynamic Programming
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
     future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    Parameters
    ----------
    prices : list[int]

    Returns
    -------
    profit : int

    Examples
    --------
    >>> max_profit([7,1,5,3,6,4])
    5

    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

    >>> max_profit([7,6,4,3,1])
    0

    Explanation: In this case, no transactions are done and the max profit = 0.
    """
    buy = prices[0]
    profit = 0
    for i, price in enumerate(prices):
        if i == 0:
            continue
        current_profit = price - buy
        if buy < price:
            profit = max(current_profit, profit)
        else:
            buy = price
    return profit
