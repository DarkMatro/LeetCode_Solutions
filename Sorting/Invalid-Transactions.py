from collections import defaultdict


def invalidTransactions(transactions: list[str]) -> list[str]:
    """
    ID: 1169
    Tags:   Array, Hash Table, String, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    A transaction is possibly invalid if:

    the amount exceeds $1000, or;
    if it occurs within (and including) 60 minutes of another transaction with the same name in a
    different city.
    You are given an array of strings transaction where transactions[i] consists of comma-separated
    values representing the name, time (in minutes), amount, and city of the transaction.

    Return a list of transactions that are possibly invalid. You may return the answer in any order.

    Parameters
    ----------
    transactions: list[str]

    Returns
    -------
    list[str]

    Examples
    --------
    >>> invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"])
    ['alice,20,800,mtv', 'alice,50,100,beijing']

    Explanation: The first transaction is invalid because the second transaction occurs within a
    difference of 60 minutes, have the same name and is in a different city. Similarly the second
    one is invalid too.

    >>> invalidTransactions(["alice,20,800,mtv","alice,50,1200,mtv"])
    ['alice,50,1200,mtv']

    >>> invalidTransactions(["alice,20,800,mtv","bob,50,1200,mtv"])
    ['bob,50,1200,mtv']
    """
    invalid = set()
    parsed_transactions = []

    for i, transaction in enumerate(transactions):
        name, time, amount, city = transaction.split(',')
        time, amount = int(time), int(amount)
        parsed_transactions.append((name, time, amount, city, i))

    transactions_by_name = defaultdict(list)

    for transaction in parsed_transactions:
        name, time, amount, city, index = transaction
        transactions_by_name[name].append(transaction)

        if amount > 1000:
            invalid.add(index)

    for name, trans_list in transactions_by_name.items():
        trans_list.sort(key=lambda x: x[1])  # Sort transactions by time

        for i in range(len(trans_list)):
            for j in range(i + 1, len(trans_list)):
                if trans_list[j][1] - trans_list[i][1] > 60:
                    break
                if trans_list[i][3] != trans_list[j][3]:  # Different cities
                    invalid.add(trans_list[i][4])
                    invalid.add(trans_list[j][4])

    return [transactions[i] for i in invalid]
