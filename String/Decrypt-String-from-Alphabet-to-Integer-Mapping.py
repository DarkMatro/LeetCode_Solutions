import string

def freqAlphabets(s: str) -> str:
    """
    ID: 1309
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a string s formed by digits and '#'. We want to map s to English lowercase
    characters as follows:

    Characters ('a' to 'i') are represented by ('1' to '9') respectively.
    Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
    Return the string formed after mapping.

    The test cases are generated so that a unique mapping will always exist.

    Parameters
    ----------
    s: str

    Returns
    -------
    str

    Examples
    --------
    >>> freqAlphabets('10#11#12')
    'jkab'

    Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

    >>> freqAlphabets('1326#')
    'acz'
    """
    alp = string.ascii_lowercase
    ans = ''
    i = len(s) - 1
    while i >= 0:
        ch = s[i]
        has_trailing = ch == '#'
        if has_trailing:
            ans += alp[int(s[i - 2: i]) - 1]
            i -= 3
        else:
            ans += alp[int(ch) - 1]
            i -= 1
    return ans[::-1]
