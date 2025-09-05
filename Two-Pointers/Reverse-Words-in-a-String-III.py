def reverseWords(s: str) -> str:
    """
    ID: 557
    Tags:   Two Pointers, Sorting
    Time:   O(n)
    Memory: O(1)

    Task
    ----------
    Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace
    and initial word order.

    Parameters
    ----------
    s : str

    Returns
    -------
    out : str

    Examples
    --------
    >>> reverseWords("Let's take LeetCode contest")
    "s'teL ekat edoCteeL tsetnoc"

    >>> reverseWords("Mr Ding")
    'rM gniD'
    """
    return ' '.join((x[::-1] for x in s.split(' ')))