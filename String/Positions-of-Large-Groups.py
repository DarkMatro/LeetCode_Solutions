def largeGroupPositions(s: str) -> list[list[int]]:
    """
    ID: 830
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    In a string s of lowercase letters, these letters form consecutive groups of the same character.

    For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

    A group is identified by an interval [start, end], where start and end denote the start and end
    indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].

    A group is considered large if it has 3 or more characters.

    Return the intervals of every large group sorted in increasing order by start index.

    Parameters
    ----------
    s: str

    Returns
    -------
    out: list[list[int]]

    Examples
    --------
    >>> largeGroupPositions('abbxxxxzzy')
    [[3, 6]]

    Explanation: "xxxx" is the only large group with start index 3 and end index 6.

    >>> largeGroupPositions('abc')
    []

    Explanation: We have groups "a", "b", and "c", none of which are large groups.

    >>> largeGroupPositions('abcdddeeeeaabbbcd')
    [[3, 5], [6, 9], [12, 14]]

    Explanation: The large groups are "ddd", "eeee", and "bbb".
    """
    ans = []
    cnt = 1
    idx_start = 0
    prev = s[0]
    i = 0
    for i in range(1, len(s)):
        x = s[i]
        if x == prev:
            cnt += 1
        elif cnt >= 3:
            ans.append([idx_start, i - 1])
            idx_start = i
            cnt = 1
        else:
            idx_start = i
            cnt = 1
        prev = x
    if cnt >= 3:
        ans.append([idx_start, i])
    return ans
