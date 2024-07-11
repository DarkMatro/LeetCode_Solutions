def licenseKeyFormatting(s: str, k: int) -> str:
    """
    ID: 482
    Tags:   String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given a license key represented as a string s that consists of only alphanumeric
    characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given
    an integer k.

    We want to reformat the string s such that each group contains exactly k characters, except for
    the first group, which could be shorter than k but still must contain at least one character.
    Furthermore, there must be a dash inserted between two groups, and you should convert all
    lowercase letters to uppercase.

    Return the reformatted license key.

    Parameters
    ----------
    s: str

    k: int

    Returns
    -------
    out: str

    Examples
    --------
    >>> licenseKeyFormatting("5F3Z-2e-9-w", 4)
    '5F3Z-2E9W'

    Explanation: The string s has been split into two parts, each part has 4 characters.
    Note that the two extra dashes are not needed and can be removed.

    >>> licenseKeyFormatting("2-5g-3-J", 2)
    '2-5G-3J'

    Explanation: The string s has been split into three parts, each part has 2 characters except the
    first part as it could be shorter as mentioned above.
    """
    lic = ''.join(s.split('-')).upper()[::-1]
    ans = ''
    for i in range(0, len(lic), k):
        ans += lic[i: i + k] + '-'
    return ans[-2::-1]
