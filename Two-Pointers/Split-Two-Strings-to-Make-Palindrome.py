def checkPalindromeFormation(a: str, b: str) -> bool:
    """
    ID: 1616
    Tags:   Two Pointers, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given two strings a and b of the same length. Choose an index and split both strings at the same index,
    splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, and splitting b into two strings:
    bprefix and bsuffix where b = bprefix + bsuffix. Check if aprefix + bsuffix or bprefix + asuffix forms a palindrome.

    When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is allowed to be empty. For example,
    if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , and "abc" + "" are valid splits.

    Return true if it is possible to form a palindrome string, otherwise return false.

    Notice that x + y denotes the concatenation of strings x and y.

    Parameters
    ----------
    a: str

    b: str

    Returns
    -------
    out : bool

    Examples
    --------
    >>> checkPalindromeFormation('x', 'y')
    True

    Explaination: If either a or b are palindromes the answer is true since you can split in the following way:
    aprefix = "", asuffix = "x"
    bprefix = "", bsuffix = "y"
    Then, aprefix + bsuffix = "" + "y" = "y", which is a palindrome.

    >>> checkPalindromeFormation('xbdef', 'xecab')
    False

    >>> checkPalindromeFormation('ulacfd', 'jizalu')
    True

    Explaination: Split them at index 3:
    aprefix = "ula", asuffix = "cfd"
    bprefix = "jiz", bsuffix = "alu"
    Then, aprefix + bsuffix = "ula" + "alu" = "ulaalu", which is a palindrome.
    """
    return check(a, b) or check(b, a)

def check(a: str, b: str) -> bool:
    n = len(a)
    lp = 0
    rp = n - 1
    while lp < rp and a[lp] == b[rp]:
        lp += 1
        rp -= 1
    t = a[lp: rp + 1]
    p = b[lp: rp + 1]
    return t == t[::-1] or p == p[::-1]
