def lengthOfLastWord(s: str) -> int:
    """
    ID: 0058
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a string s consisting of words and spaces, return the length of the last word in the string.

    A word is a maximal substring consisting of non-space characters only.

    Parameters
    ----------
    s: str

    Returns
    -------
    int

    Examples
    --------
    >>> lengthOfLastWord('Hello World')
    5

    Explanation: The last word is "World" with length 5.

    >>> lengthOfLastWord('   fly me   to   the moon  ')
    4

    Explanation: The last word is "moon" with length 4.

    >>> lengthOfLastWord('luffy is still joyboy')
    6

    Explanation: The last word is "joyboy" with length 6.
    """
    return len(s.split()[-1])