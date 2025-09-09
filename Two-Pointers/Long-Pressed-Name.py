from itertools import groupby


def isLongPressedName(name: str, typed: str) -> bool:
    """
    ID: 925
    Tags:   Two Pointers, String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long
    pressed, and the character will be typed 1 or more times.

    You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with
    some characters (possibly none) being long pressed.

    Parameters
    ----------
    name: str

    typed: str

    Returns
    -------
    out : bool

    Examples
    --------
    >>> isLongPressedName("alex", "aaleex")
    True

    Explanation: 'a' and 'e' in 'alex' were long pressed.

    >>> isLongPressedName("saeed", "ssaaedd")
    False

    Explanation: 'e' must have been pressed twice, but it was not in the typed output.
    """
    g1 = [(k, len(list(grp))) for k, grp in groupby(name)]
    g2 = [(k, len(list(grp))) for k, grp in groupby(typed)]
    if len(g1) != len(g2):
        return False

    return all(k1 == k2 and v1 <= v2 for (k1, v1), (k2, v2) in zip(g1, g2))
