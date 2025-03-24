def alertNames(keyName: list[str], keyTime: list[str]) -> list[str]:
    """
    ID: 1604
    Tags:   Array, Hash Table, String, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their
    key-card, the security system saves the worker's name and the time when it was used. The system
    emits an alert if any worker uses the key-card three or more times in a one-hour period.

    You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds
    to a person's name and the time when their key-card was used in a single day.

    Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".

    Return a list of unique worker names who received an alert for frequent keycard use. Sort the
    names in ascending order alphabetically.

    Notice that "10:00" - "11:00" is considered to be within a one-hour period, while
    "22:51" - "23:52" is not considered to be within a one-hour period.

    Parameters
    ----------
    keyName: list[str]

    keyTime: list[str]

    Returns
    -------
    list[str]

    Examples
    --------
    >>> alertNames(["daniel","daniel","daniel","luis","luis","luis","luis"], ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"])
    ['daniel']

    Explanation: "daniel" used the keycard 3 times in a one-hour period ("10:00","10:40", "11:00").

    >>> alertNames(["alice","alice","alice","bob","bob","bob","bob"], ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"])
    ['bob']

    Explanation: "bob" used the keycard 3 times in a one-hour period ("21:00","21:20", "21:30").
    """

    def often_access(arr: list[int]) -> bool:
        for i in range(0, len(arr) - 2):
            if arr[i + 2] - arr[i] <= 60:
                return True
        return False

    at = {}
    for name, time in zip(keyName, keyTime):
        time = int(time[:2]) * 60 + int(time[3:])
        if name not in at:
            at[name] = [time]
        else:
            at[name].append(time)
    ans = []
    for k, v in at.items():
        if often_access(sorted(v)):
            ans.append(k)
    return sorted(ans)
