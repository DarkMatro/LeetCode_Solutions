def reformatNumber(number: str) -> str:
    """
    ID: 1694
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a phone number as a string number. number consists of digits, spaces ' ', and/or
    dashes '-'.

    You would like to reformat the phone number in a certain manner. Firstly, remove all spaces and
    dashes. Then, group the digits from left to right into blocks of length 3 until there are 4 or
    fewer digits. The final digits are then grouped as follows:

    2 digits: A single block of length 2.
    3 digits: A single block of length 3.
    4 digits: Two blocks of length 2 each.
    The blocks are then joined by dashes. Notice that the reformatting process should never produce
    any blocks of length 1 and produce at most two blocks of length 2.

    Return the phone number after formatting.

    Parameters
    ----------
    number: str

    Returns
    -------
    out: str

    Examples
    --------
    >>> reformatNumber("1-23-45 6")
    '123-456'

    Explanation: The digits are "123456".
    Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
    Step 2: There are 3 digits remaining, so put them in a single block of length 3. The 2nd block
    is "456".
    Joining the blocks gives "123-456".

    >>> reformatNumber("123 4-567")
    '123-45-67'

    Explanation: The digits are "1234567".
    Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
    Step 2: There are 4 digits left, so split them into two blocks of length 2. The blocks are "45"
    and "67".
    Joining the blocks gives "123-45-67".

    >>> reformatNumber("123 4-5678")
    '123-456-78'

    Explanation: The digits are "12345678".
    Step 1: The 1st block is "123".
    Step 2: The 2nd block is "456".
    Step 3: There are 2 digits left, so put them in a single block of length 2. The 3rd block is
    "78".
    Joining the blocks gives "123-456-78".
    """
    number = number.replace('-', '').replace(' ', '')
    ans = ''
    i = 0
    n = len(number)
    while i <= n:
        dif = n - i
        if dif > 4:
            if i != 0:
                ans += '-'
            ans += number[i:i + 3]
        elif dif == 4:
            if i != 0:
                ans += '-'
            ans += number[i:i + 2] + '-' + number[i + 2:i + 4]
        elif dif in [3, 2]:
            if i != 0:
                ans += '-'
            ans += number[i:i + dif]
        else:
            break
        i += dif if dif <= 4 else 3
    return ans
