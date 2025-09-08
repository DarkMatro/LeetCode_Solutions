def reverseOnlyLetters(s: str) -> str:
    """
    ID: 917
    Tags:   Two Pointers, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a string s, reverse the string according to the following rules:

    All the characters that are not English letters remain in the same position.
    All the English letters (lowercase or uppercase) should be reversed.
    Return s after reversing it.

    Parameters
    ----------
    s: str

    Returns
    -------
    out : str

    Examples
    --------
    >>> reverseOnlyLetters("ab-cd")
    'dc-ba'

    >>> reverseOnlyLetters("a-bC-dEf-ghIj")
    'j-Ih-gfE-dCba'

    >>> reverseOnlyLetters("Test1ng-Leet=code-Q!")
    'Qedo1ct-eeLg=ntse-T!'
    """
    res = len(s) * [0]

    i = 0
    j = len(s) - 1

    while i <= j:
        if s[i].isalpha() and s[j].isalpha():
            res[i] = s[j]
            res[j] = s[i]
            i += 1
            j -= 1
        elif s[i].isalpha():
            res[j] = s[j]
            j -= 1
        else:
            res[i] = s[i]
            i += 1

    return ''.join(res)
