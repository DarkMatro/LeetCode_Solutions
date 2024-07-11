def findTheLongestBalancedSubstring(s: str) -> int:
    """
    ID: 2609
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a binary string s consisting only of zeroes and ones.

    A substring of s is considered balanced if all zeroes are before ones and the number of zeroes
    is equal to the number of ones inside the substring. Notice that the empty substring is
    considered a balanced substring.

    Return the length of the longest balanced substring of s.

    A substring is a contiguous sequence of characters within a string.

    Parameters
    ----------
    s: str

    Returns
    -------
    out: int

    Examples
    --------
    >>> findTheLongestBalancedSubstring("01000111")
    6

    Explanation: The longest balanced substring is "000111", which has length 6.

    >>> findTheLongestBalancedSubstring("00111")
    4

    Explanation: The longest balanced substring is "0011", which has length 4.

    >>> findTheLongestBalancedSubstring("111")
    0

    Explanation: There is no balanced substring except the empty substring, so the answer is 0.
    """
    subarrays = []
    sub_array = ''
    for i, b in enumerate(s):
        if b == '0' and i > 0 and s[i - 1] == '1':
            subarrays.append(sub_array)
            sub_array = ''
            sub_array += b
        elif sub_array and b == '1':
            sub_array += b
        elif b == '0':
            sub_array += b
    else:
        if sub_array and sub_array[-1] == '1':
            subarrays.append(sub_array)
    ans = 0
    for sub in subarrays:
        longest = min(sub.count('0'), sub.count('1')) * 2
        ans = max(ans, longest)

    return ans
