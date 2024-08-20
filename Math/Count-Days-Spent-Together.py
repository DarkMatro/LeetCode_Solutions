def countDaysTogether(arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
    """
    ID: 2409
    Tags:   Math, String
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the
    city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from
    the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format
    "MM-DD", corresponding to the month and day of the date.

    Return the total number of days that Alice and Bob are in Rome together.

    You can assume that all dates occur in the same calendar year, which is not a leap year. Note
    that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30,
    31, 30, 31].

    Parameters
    ----------
    arriveAlice: str

    leaveAlice: str

    arriveBob: str

    leaveBob: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> countDaysTogether("08-15", "08-18", "08-16", "08-19")
    3

    Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August
    16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is
    3.

    >>> countDaysTogether("10-01", "10-31", "11-01", "12-31")
    0

    Explanation: There is no day when Alice and Bob are in Rome together, so we return 0.
    """
    days_alice_arr = count_days(arriveAlice)
    days_alice_leave = count_days(leaveAlice)
    days_bob_arr = count_days(arriveBob)
    days_bob_leave = count_days(leaveBob)
    return len(set(range(days_alice_arr, days_alice_leave + 1)) & set(
        range(days_bob_arr, days_bob_leave + 1)))


def count_days(date: str) -> int:
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    arr_month, arr_day= map(int, date.split('-'))
    return sum(days_per_month[: arr_month - 1]) + arr_day
