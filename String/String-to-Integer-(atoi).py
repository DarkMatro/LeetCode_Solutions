def myAtoi(s: str) -> int:
    """
    ID: 8
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

    The algorithm for myAtoi(string s) is as follows:

    Whitespace: Ignore any leading whitespace (" ").
    Signedness: Determine the sign by checking if the next character is '-' or '+', assuming
    positivity is neither present.
    Conversion: Read the integer by skipping leading zeros until a non-digit character is
    encountered or the end of the string is reached. If no digits were read, then the result is 0.
    Rounding: If the integer is out of the 32-bit signed integer range [-2**31, 2**31 - 1],
    then round
    the integer to remain in the range. Specifically, integers less than -2**31 should be rounded to
    -2**31, and integers greater than 2**31 - 1 should be rounded to 2**31 - 1.
    Return the integer as the final result.

    Parameters
    ----------
    s: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> myAtoi('42')
    42

    Explanation: The underlined characters are what is read in and the caret is the current reader
    position.
    Step 1: "42" (no characters read because there is no leading whitespace)
             ^
    Step 2: "42" (no characters read because there is neither a '-' nor '+')
             ^
    Step 3: "42" ("42" is read in)

    >>> myAtoi(' -042')
    -42

    Step 1: "   -042" (leading whitespace is read and ignored)
                ^
    Step 2: "   -042" ('-' is read, so the result should be negative)
                 ^
    Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)

    >>> myAtoi('1337c0d3')
    1337

    Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
             ^
    Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
             ^
    Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)

    >>> myAtoi('0-1')
    0

    Step 1: "0-1" (no characters read because there is no leading whitespace)
             ^
    Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
             ^
    Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)

    >>> myAtoi('words and 987')
    0

    Reading stops at the first non-digit character 'w'.
    """
    s = s.strip()
    ans = ''
    negative = False
    for i, x in enumerate(s):
        if i == 0 and x == '-':
            negative = True
            continue
        if i == 0 and x == '+':
            continue
        if not ans and x == '0':
            continue
        if x.isdigit():
            ans += x
        else:
            break
    if not ans:
        return 0
    float(5)
    ans = int(ans)
    ans = ans if not negative else -ans
    ans = 2147483647 if ans > 2147483647 else ans
    ans = -2147483648 if ans < -2147483648 else ans
    return ans
