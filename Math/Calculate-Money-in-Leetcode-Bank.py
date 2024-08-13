def totalMoney(n: int) -> int:
    """
    ID: 1716
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

    He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will
    put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
    Given n, return the total amount of money he will have in the Leetcode bank at the end of the
    nth day.

    Parameters
    ----------
    n: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> totalMoney(4)
    10

    Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.


    >>> totalMoney(10)
    37

    Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37.
    Notice that on the 2nd Monday, Hercy only puts in $2.

    >>> totalMoney(20)
    96

    Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) +
     (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
    """
    # Calculate the number of full weeks and remaining days
    weeks = n // 7
    remaining_days = n % 7

    # Calculate the total amount for complete weeks
    total = 0
    for i in range(weeks):
        total += sum([i + j + 1 for j in range(7)])

    # Calculate the total amount for remaining days in the last incomplete week
    total += sum([weeks + j + 1 for j in range(remaining_days)])

    return total

