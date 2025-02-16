def numWays(s: str) -> int:
    """
    ID: 1573
    Tags:   Math, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a binary string s, you can split s into 3 non-empty strings s1, s2, and s3 where
    s1 + s2 + s3 = s.

    Return the number of ways s can be split such that the number of ones is the same in s1, s2,
    and s3. Since the answer may be too large, return it modulo 109 + 7.

    Parameters
    ----------
    s: str

    Returns
    -------
    int

    Examples
    --------
    >>> numWays("10101")
    4

    Explanation: There are four ways to split s in 3 parts where each part contain the same number of letters '1'.
    "1|010|1"
    "1|01|01"
    "10|10|1"
    "10|1|01"

    >>> numWays("1001")
    0

    >>> numWays("0000")
    3

    Explanation: There are three ways to split s in 3 parts.
    "0|0|00"
    "0|00|0"
    "00|0|0"
    """
    MOD = 10 ** 9 + 7
    ones_count = s.count('1')

    # If total number of ones is not divisible by 3, it's impossible to split equally
    if ones_count % 3 != 0:
        return 0

    # If there are no ones, count ways to split zeros
    if ones_count == 0:
        n = len(s)
        return ((n - 1) * (n - 2) // 2) % MOD  # Choosing 2 out of (n-1) places to split

    ones_per_part = ones_count // 3
    first_cut_options = second_cut_options = 0
    count = 0

    for ch in s:
        if ch == '1':
            count += 1
        if count == ones_per_part:
            first_cut_options += 1
        elif count == 2 * ones_per_part:
            second_cut_options += 1

    return (first_cut_options * second_cut_options) % MOD
