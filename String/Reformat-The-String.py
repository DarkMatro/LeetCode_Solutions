def reformat(s: str) -> str:
    """
    ID: 1417
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given an alphanumeric string s. (Alphanumeric string is a string consisting of lowercase
    English letters and digits).

    You have to find a permutation of the string where no letter is followed by another letter and
    no digit is followed by another digit. That is, no two adjacent characters have the same type.

    Return the reformatted string or return an empty string if it is impossible to reformat the
    string.

    Parameters
    ----------
    s: str

    Returns
    -------
    out: str

    Examples
    --------
    >>> reformat('a0b1c2')
    '0a1b2c'

    Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c",
    "0c2a1b" are also valid permutations.

    >>> reformat('leetcode')
    ''

    Explanation: "leetcode" has only characters so we cannot separate them by digits.

    >>> reformat('1229857369')
    ''

    Explanation: "1229857369" has only digits so we cannot separate them by characters.
    """
    digits = ''
    letters = ''
    for x in s:
        if x.isdigit():
            digits += x
        else:
            letters += x
    if len(letters) - len(digits) not in [-1, 0, 1]:
        return ''

    if len(letters) > len(digits):
        ans = letters[0]
        letters = letters[1:]
        letter_first = False
    elif len(letters) < len(digits):
        ans = digits[0]
        digits = digits[1:]
        letter_first = True
    else:
        letter_first = False
        ans = ''
    for let, dig in zip(letters, digits):
        if letter_first:
            ans += let + dig
        else:
            ans += dig + let
    return ans
