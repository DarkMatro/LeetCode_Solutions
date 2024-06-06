def countAsterisks(s: str) -> int:
    """
    ID: 2315
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair.
    In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.

    Return the number of '*' in s, excluding the '*' between each pair of '|'.

    Note that each '|' will belong to exactly one pair.

    Parameters
    ----------
    s: str

    Returns
    -------
    int

    Examples
    --------
    >>> countAsterisks("l|*e*et|c**o|*de|")
    2

    Explanation: The considered characters are underlined: "l|*e*et|c**o|*de|".
    The characters between the first and second '|' are excluded from the answer.
    Also, the characters between the third and fourth '|' are excluded from the answer.
    There are 2 asterisks considered. Therefore, we return 2.

    >>> countAsterisks("iamprogrammer")
    0

    Explanation: In this example, there are no asterisks in s. Therefore, we return 0.

    >>> countAsterisks("yo|uar|e**|b|e***au|tifu|l")
    5

    Explanation: The considered characters are underlined: "yo|uar|e**|b|e***au|tifu|l". There are
    5 asterisks considered. Therefore, we return 5.
    """
    n = 0
    ans = 0
    for ch in s:
        if n == 0 and ch == '*':
            ans += 1
        elif n == 0 and ch == '|':
            n = 1
        elif n == 1 and ch == '|':
            n = 0
    return ans
