def findMinimumOperations(s1: str, s2: str, s3: str) -> int:
    """
    ID: 2937
    Tags:   String
    Time:   O(NlogN)
    Memory: O(1)

    Task
    ----------
    You are given three strings: s1, s2, and s3. In one operation you can choose one of these
    strings and delete its rightmost character. Note that you cannot completely empty a string.

    Return the minimum number of operations required to make the strings equal. If it is impossible
    to make them equal, return -1.

    Parameters
    ----------
    s1: str

    s2: str

    s3: str

    Returns
    -------
    and: int

    Examples
    --------
    >>> findMinimumOperations("abc", "abb", "ab")
    2

    Explanation: Deleting the rightmost character from both s1 and s2 will result in three equal
    strings.

    >>> findMinimumOperations("dac", "bac", "cac")
    -1

    Explanation: Since the first letters of s1 and s2 differ, they cannot be made equal.
    """
    strs = sorted([s1, s2, s3])
    min_len = min(len(strs[0]), len(strs[-1]))
    first_word = strs[0]
    last_word = strs[-1]
    longest_common_prefix = ''
    for i in range(min_len):
        if first_word[i] == last_word[i]:
            longest_common_prefix += first_word[i]
        else:
            break
    if not longest_common_prefix:
        return -1
    lens = sum([len(x) for x in strs])
    return lens - len(longest_common_prefix) * 3
