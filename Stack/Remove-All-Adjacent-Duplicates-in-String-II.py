def removeDuplicates(s: str, k: int) -> str:
    """
    ID: 1209
    Tags:   String, Stack
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters
    from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

    We repeatedly make k duplicate removals on s until we no longer can.

    Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is
    unique.

    Parameters
    ----------
    s: str

    k: int

    Returns
    -------
    out : str

    Examples
    --------
    >>> removeDuplicates('abcd', 2)
    'abcd'

    Explanation: There's nothing to delete.

    >>> removeDuplicates('deeedbbcccbdaa', 3)
    'aa'

    Explanation: First delete "eee" and "ccc", get "ddbbbdaa"
    Then delete "bbb", get "dddaa"
    Finally delete "ddd", get "aa"

    >>> removeDuplicates('pbbcggttciiippooaais', 2)
    'ps'
    """
    stack = []
    for x in s:
        if stack and stack[-1][0] == x:
            stack[-1][1] += 1
        else:
            stack.append([x, 1])
        while stack and stack[-1][0] == x and stack[-1][1] >= k:
            if stack[-1][1] == k:
                stack.pop()
            else:
                stack[-1][1] -= k
    return ''.join([x * cnt for x, cnt in stack])
