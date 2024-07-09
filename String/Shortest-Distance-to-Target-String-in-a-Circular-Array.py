def closetTarget(words: list[str], target: str, startIndex: int) -> int:
    """
    ID: 2515
    Tags:   Array, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a 0-indexed circular string array words and a string target. A circular array
    means that the array's end connects to the array's beginning.

    Formally, the next element of words[i] is words[(i + 1) % n] and the previous element of
    words[i] is words[(i - 1 + n) % n], where n is the length of words.
    Starting from startIndex, you can move to either the next word or the previous word with 1 step
    at a time.

    Return the shortest distance needed to reach the string target. If the string target does not
    exist in words, return -1.

    Parameters
    ----------
    words: list[str]

    target: str

    startIndex: int

    Returns
    -------
    out: int

    Examples
    --------
    >>> closetTarget(["hello","i","am","leetcode","hello"], "hello", 1)
    1

    Explanation: We start from index 1 and can reach "hello" by
    - moving 3 units to the right to reach index 4.
    - moving 2 units to the left to reach index 4.
    - moving 4 units to the right to reach index 0.
    - moving 1 unit to the left to reach index 0.
    The shortest distance to reach "hello" is 1.

    >>> closetTarget(["a","b","leetcode"], "leetcode", 0)
    1

    Explanation: We start from index 0 and can reach "leetcode" by
    - moving 2 units to the right to reach index 3.
    - moving 1 unit to the left to reach index 3.
    The shortest distance to reach "leetcode" is 1.

    >>> closetTarget(["i","eat","leetcode"], "ate", 0)
    -1

    Explanation: Since "ate" does not exist in words, we return -1.
    """
    n = len(words)
    for i in range(n):
        if words[(startIndex + i) % n] == target:
            break
    else:
        return -1
    for j in range(n):
        if words[(startIndex - j) % n] == target:
            break
    return min(i, j)
