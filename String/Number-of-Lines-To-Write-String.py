from string import ascii_lowercase

def numberOfLines(widths: list[int], s: str) -> list[int]:
    """
    ID: 0806
    Tags:   Array, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a string s of lowercase English letters and an array widths denoting how many
    pixels wide each lowercase English letter is. Specifically, widths[0] is the width of 'a',
    widths[1] is the width of 'b', and so on.

    You are trying to write s across several lines, where each line is no longer than 100 pixels.
    Starting at the beginning of s, write as many letters on the first line such that the total
    width does not exceed 100 pixels. Then, from where you stopped in s, continue writing as many
    letters as you can on the second line. Continue this process until you have written all of s.

    Return an array result of length 2 where:

    result[0] is the total number of lines.
    result[1] is the width of the last line in pixels.

    Parameters
    ----------
    widths: list[int]

    s: str

    Returns
    -------
    out: list[int]

    Examples
    --------
    >>> numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "abcdefghijklmnopqrstuvwxyz")
    [3, 60]

    Explanation:
    You can write s as follows:
    abcdefghij  // 100 pixels wide
    klmnopqrst  // 100 pixels wide
    uvwxyz      // 60 pixels wide
    There are a total of 3 lines, and the last line is 60 pixels wide.

    >>> numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa")
    [2, 4]

    Explanation:
    You can write s as follows:
    bbbcccdddaa  // 98 pixels wide
    a            // 4 pixels wide
    There are a total of 2 lines, and the last line is 4 pixels wide.
    """
    alp = ascii_lowercase
    line_width = 0
    lines = 1
    for letter in s:
        idx = alp.index(letter)
        width = widths[idx]
        if line_width + width <= 100:
            line_width += width
        else:
            lines += 1
            line_width = width
    return [lines, line_width]
