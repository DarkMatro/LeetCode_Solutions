def buddyStrings(s: str, goal: str) -> bool:
    """
    ID: 859
    Tags:   Hash Table, String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given two strings s and goal, return true if you can swap two letters in s so the result is
    equal to goal, otherwise, return false.

    Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and
    swapping the characters at s[i] and s[j].

    For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

    Parameters
    ----------
    s: str

    goal: str

    Returns
    -------
    out : bool

    Examples
    --------
    >>> buddyStrings('ab', 'ba')
    True

    Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

    >>> buddyStrings('ab', 'ab')
    False

    Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in
    "ba" != goal.

    >>> buddyStrings('aa', 'aa')
    True

    Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
    """
    # Case 1: If the lengths of s and goal are different, return False
    if len(s) != len(goal):
        return False

    # Case 2: If s and goal are already the same
    if s == goal:
        # Check if there are at least two duplicate characters in s
        # because we need two same characters to swap without changing the string
        return len(set(s)) < len(s)

    # Case 3: Find the positions where s and goal differ
    diff = []
    for i, x in enumerate(s):
        if x != goal[i]:
            diff.append(i)

    # There must be exactly two differences and swapping them should make the strings equal
    return len(diff) == 2 and s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]
