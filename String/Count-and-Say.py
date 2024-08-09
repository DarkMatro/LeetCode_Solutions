def rle( s: str) -> str:
    ans = ''
    prev = None
    n = 1
    for x in s:
        if prev is None:
            prev = x
            continue
        if x == prev:
            n += 1
        else:
            ans += f'{n}{prev}'
            n = 1
        prev = x
    else:
        ans += f'{n}{prev}'
    return ans

def countAndSay(n: int) -> str:
    """
    ID: 38
    Tags:   String
    Time:   O(N * 2^N)
    Memory: O(N)

    Task
    ----------
    The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

    countAndSay(1) = "1"
    countAndSay(n) is the run-length encoding of countAndSay(n - 1).
    Run-length encoding (RLE) is a string compression method that works by replacing consecutive
    identical characters (repeated 2 or more times) with the concatenation of the character and the
    number marking the count of the characters (length of the run). For example, to compress the
    string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and
    replace "1" with "11". Thus, the compressed string becomes "23321511".

    Given a positive integer n, return the nth element of the count-and-say sequence.

    Parameters
    ----------
    n: int

    Returns
    -------
    out : str

    Examples
    --------
    >>> countAndSay(4)
    '1211'

    Explanation:

    countAndSay(1) = "1"
    countAndSay(2) = RLE of "1" = "11"
    countAndSay(3) = RLE of "11" = "21"
    countAndSay(4) = RLE of "21" = "1211"

    >>> countAndSay(1)
    '1'

    Explanation: This is the base case.
    """
    ans = '1'
    for _ in range(2, n + 1):
        ans = rle(ans)
    return ans
