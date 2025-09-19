from itertools import zip_longest


def compareVersion(version1: str, version2: str) -> int:
    """
    ID: 165
    Tags: Two Pointers, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by
    dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

    To compare version strings, compare their revision values in left-to-right order. If one of the version strings has
    fewer revisions, treat the missing revision values as 0.

    Return the following:

    If version1 < version2, return -1.
    If version1 > version2, return 1.
    Otherwise, return 0.

    Parameters
    ----------
    version1: str

    version2: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> compareVersion("1.2", "1.10")
    -1

    Explanation:
    version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

    >>> compareVersion("1.01", "1.001")
    0

    Explanation:
    Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

    >>> compareVersion("1.0", "1.0.0.0")
    0

    Explanation:
    version1 has less revisions, which means every missing revision are treated as "0".
    """
    for v1, v2 in zip_longest(version1.split('.'), version2.split('.')):
        if v1 is None and int(v2) > 0:
            return -1
        elif v2 is None and int(v1) > 0:
            return 1
        elif v1 is None and int(v2) == 0:
            continue
        elif v2 is None and int(v1) == 0:
            continue
        v1 = int(v1)
        v2 = int(v2)
        if v1 > v2:
            return 1
        elif v2 > v1:
            return -1
    return 0
