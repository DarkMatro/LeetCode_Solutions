def numDifferentIntegers(word: str) -> int:
    """
    ID: 1805
    Tags:   Hash Table, String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given a string word that consists of digits and lowercase English letters.

    You will replace every non-digit character with a space. For example, "a123bc34d8ef34" will
    become " 123  34 8  34". Notice that you are left with some integers that are separated by at
    least one space: "123", "34", "8", and "34".

    Return the number of different integers after performing the replacement operations on word.

    Two integers are considered different if their decimal representations without any leading zeros
    are different.

    Parameters
    ----------
    word: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> numDifferentIntegers('a123bc34d8ef34')
    3

    Explanation: The three different integers are "123", "34", and "8". Notice that "34" is only
    counted once.

    >>> numDifferentIntegers('leet1234code234')
    2

    >>> numDifferentIntegers('a1b01c001')
    1

    Explanation:  The three integers "1", "01", and "001" all represent the same integer because
    the leading zeros are ignored when comparing their decimal values.
    """
    nums = set()
    first = word[0]
    ns = first if first.isdigit() else ''
    for i, x in enumerate(word):
        if i == 0:
            continue
        if x.isdigit():
            ns += x
        elif ns:
            nums.add(int(ns))
            ns = ''
    else:
        if ns:
            nums.add(int(ns))
    return len(nums)
