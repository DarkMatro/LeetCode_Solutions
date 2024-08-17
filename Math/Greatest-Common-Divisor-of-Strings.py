from math import gcd

def gcdOfStrings(str1: str, str2: str) -> str:
    """
    ID: 1071
    Tags:   Math, String
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e.,
    t is concatenated with itself one or more times).

    Given two strings str1 and str2, return the largest string x such that x divides both str1 and
    str2.

    Parameters
    ----------
    str1: str

    str2: str

    Returns
    -------
    out : str

    Examples
    --------
    >>> gcdOfStrings('ABCABC', 'ABC')
    'ABC'

    Explanation: The nearest multiple of 10 to 9 is 10. So your account balance becomes
    100 - 10 = 90.

    >>> gcdOfStrings('ABABAB', 'ABAB')
    'AB'

    >>> gcdOfStrings('LEET', 'CODE')
    ''
    """
    if str1 + str2 != str2 + str1:
        return ''
    return str1[: gcd(len(str1), len(str2))]
