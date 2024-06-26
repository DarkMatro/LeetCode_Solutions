def largestGoodInteger(num: str) -> str:
    """
    ID: 2264
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a string num representing a large integer. An integer is good if it meets the
    following conditions:

    It is a substring of num with length 3.
    It consists of only one unique digit.
    Return the maximum good integer as a string or an empty string "" if no such integer exists.

    Note:

    A substring is a contiguous sequence of characters within a string.
    There may be leading zeroes in num or a good integer.

    Parameters
    ----------
    num: str

    Returns
    -------
    out: str

    Examples
    --------
    >>> largestGoodInteger("6777133339")
    '777'

    Explanation:
    There are two distinct good integers: "777" and "333".
    "777" is the largest, so we return "777".

    >>> largestGoodInteger("2300019")
    '000'

    Explanation: "000" is the only good integer.

    >>> largestGoodInteger("42352338")
    ''

    Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no
    good integers.
    """
    ans = ''
    for i in range(9, -1, -1):
        substr = f"{i}{i}{i}"
        if num.find(substr) != -1:
            ans = substr
            break
    return ans
