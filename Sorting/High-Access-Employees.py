def findHighAccessEmployees(access_times: list[list[str]]) -> list[str]:
    """
    ID: 2933
    Tags:   Array, Hash Table, String, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    You are given a 2D 0-indexed array of strings, access_times, with size n. For each i where
    0 <= i <= n - 1, access_times[i][0] represents the name of an employee, and access_times[i][1]
    represents the access time of that employee. All entries in access_times are within the same day

    The access time is represented as four digits using a 24-hour time format, for example, "0800"
    or "2250".

    An employee is said to be high-access if he has accessed the system three or more times within a
    one-hour period.

    Times with exactly one hour of difference are not considered part of the same one-hour period.
    For example, "0815" and "0915" are not part of the same one-hour period.

    Access times at the start and end of the day are not counted within the same one-hour period.
    For example, "0005" and "2350" are not part of the same one-hour period.

    Return a list that contains the names of high-access employees with any order you want.

    Parameters
    ----------
    access_times: list[list[str]]

    Returns
    -------
    list[str]

    Examples
    --------
    >>> findHighAccessEmployees([["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]])
    ['a']

    Explanation: "a" has three access times in the one-hour period of [05:32, 06:31] which are
    05:32, 05:49, and 06:21.
    But "b" does not have more than two access times at all.
    So the answer is ["a"].

    >>> findHighAccessEmployees([["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]])
    ['d', 'c']

    Explanation: "c" has three access times in the one-hour period of [08:08, 09:07] which are
    08:08, 08:09, and 08:29.
    "d" has also three access times in the one-hour period of [14:10, 15:09] which are 14:10, 14:44,
    and 15:08.
    However, "e" has just one access time, so it can not be in the answer and the final answer is
    ["c", "d"].

    >>> findHighAccessEmployees([["cd","1025"],["ab","1025"],["cd","1046"],["cd","1055"],["ab","1124"],["ab","1120"]])
    ['cd', 'ab']

    Explanation: "ab" has three access times in the one-hour period of [10:25, 11:24] which are
    10:25, 11:20, and 11:24.
    "cd" has also three access times in the one-hour period of [10:25, 11:24] which are 10:25,
    10:46, and 10:55.
    So the answer is ["ab","cd"].
    """

    def often_access(arr: list[int]) -> bool:
        for i in range(0, len(arr) - 2):
            if arr[i + 2] - arr[i] < 60:
                return True
        return False

    at = {}
    for name, time in access_times:
        time = int(time[:2]) * 60 + int(time[2:])
        if name not in at:
            at[name] = [time]
        else:
            at[name].append(time)
    ans = []
    for k, v in at.items():
        if often_access(sorted(v)):
            ans.append(k)
    return ans
