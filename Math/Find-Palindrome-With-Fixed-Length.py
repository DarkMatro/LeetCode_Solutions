def kthPalindrome(queries: list[int], intLength: int) -> list[int]:
    """
    ID: 2217
    Tags:   Array, Math
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an integer array queries and a positive integer intLength, return an array answer where
    answer[i] is either the queries[i]th smallest positive palindrome of length intLength or -1 if
    no such palindrome exists.

    A palindrome is a number that reads the same backwards and forwards. Palindromes cannot have
    leading zeros.

    Parameters
    ----------
    queries: list[int]

    intLength: int

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> kthPalindrome([1,2,3,4,5,90], 3)
    [101, 111, 121, 131, 141, 999]

    Explanation: The first few palindromes of length 3 are:
    101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, ...
    The 90th palindrome of length 3 is 999.

    >>> kthPalindrome([2,4,6], 4)
    [1111, 1331, 1551]

    Explanation: The first six palindromes of length 4 are:
    1001, 1111, 1221, 1331, 1441, and 1551.
    """
    result = []
    half_len = (intLength + 1) // 2  # Half length
    start = 10 ** (half_len - 1)  # Smallest number with 'half_len' digits
    end = 10 ** half_len  # Upper bound for 'half_len' digits

    for q in queries:
        num = start + q - 1  # The q-th smallest number
        if num >= end:
            result.append(-1)
        else:
            num_str = str(num)
            if intLength % 2 == 0:
                palindrome = num_str + num_str[::-1]
            else:
                palindrome = num_str + num_str[-2::-1]  # Exclude middle digit when mirroring
            result.append(int(palindrome))

    return result
