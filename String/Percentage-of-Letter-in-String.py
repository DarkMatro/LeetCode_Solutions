def percentageLetter(s: str, letter: str) -> int:
    """
    ID: 2278
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a string s and a character letter, return the percentage of characters in s that equal
    letter rounded down to the nearest whole percent.

    Parameters
    ----------
    s: str

    letter: str

    Returns
    -------
    out: int

    Examples
    --------
    >>> percentageLetter("foobar", "o")
    33

    Explanation:
    The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded
    down, so we return 33.

    >>> percentageLetter("jjjj", "k")
    0

    Explanation:
    The percentage of characters in s that equal the letter 'k' is 0%, so we return 0.
    """
    occurrences = sum([1 for x in s if x == letter])
    return int(occurrences * 100 / len(s))
