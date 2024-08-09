def convert(s: str, numRows: int) -> str:
    """
    ID: 6
    Tags:   String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
    (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: "PAHNAPLSIIGYIR"

    Write the code that will take a string and make this conversion given a number of rows:

    string convert(string s, int numRows);

    Parameters
    ----------
    s: str

    numRows: int

    Returns
    -------
    out : str

    Examples
    --------
    >>> convert('PAYPALISHIRING', 3)
    'PAHNAPLSIIGYIR'

    >>> convert('PAYPALISHIRING', 4)
    'PINALSIGYAHRPI'

    Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I

    >>> convert('A', 1)
    'A'
    """
    lines = ['' for i in range(numRows)]
    i = 0
    n = 0
    while i < len(s):
        if n < numRows:
            lines[n] += s[i]
        else:
            n -= 2
            while n > 0 and i < len(s):
                lines[n] += s[i]
                n -= 1
                i += 1
            else:
                n = 0
            continue
        i += 1
        n += 1
    return ''.join(lines)
