import string


def cellsInRange(s: str) -> list[str]:
    """
    ID: 2194
    Tags:   String
    Time:   O(r * c)
    Memory: O(1)

    Task
    ----------
    A cell (r, c) of an Excel sheet is represented as a string "<col><row>" where:

    <col> denotes the column number c of the cell. It is represented by alphabetical letters.
    For example, the 1st column is denoted by 'A', the 2nd by 'B', the 3rd by 'C', and so on.
    <row> is the row number r of the cell. The rth row is represented by the integer r.
    You are given a string s in the format "<col1><row1>:<col2><row2>", where <col1> represents
    the column c1, <row1> represents the row r1, <col2> represents the column c2, and <row2>
    represents the row r2, such that r1 <= r2 and c1 <= c2.

    Return the list of cells (x, y) such that r1 <= x <= r2 and c1 <= y <= c2. The cells should be
    represented as strings in the format mentioned above and be sorted in non-decreasing order first
    by columns and then by rows.


    Parameters
    ----------
    s: str

    Returns
    -------
    list[str]

    Examples
    --------
    >>> cellsInRange("K1:L2")
    ['K1', 'K2', 'L1', 'L2']

    Explanation: The above diagram shows the cells which should be present in the list.
    The red arrows denote the order in which the cells should be presented.

    >>> cellsInRange("A1:F1")
    ['A1', 'B1', 'C1', 'D1', 'E1', 'F1']
    """
    first_row = int(s[1])
    last_row = int(s[-1])
    letters = string.ascii_uppercase
    first_letter_id = letters.find(s[0])
    last_letter_id = letters.find(s[3])
    ans = []
    for col_id in range(first_letter_id, last_letter_id + 1):
        for row_id in range(first_row, last_row + 1):
            ans.append(letters[col_id] + str(row_id))
    return ans