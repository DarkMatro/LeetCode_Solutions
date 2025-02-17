from collections import Counter


def originalDigits(s: str) -> str:
    """
    ID: 423
    Tags: Hash Table, Math, String
    Time: O(N)
    Memory: O(N)

    Task
    ----------
    Given a string s containing an out-of-order English representation of digits 0-9, return the
    digits in ascending order.

    Parameters
    ----------
    s: str

    Returns
    -------
    str

    Examples
    --------
    >>> originalDigits('owoztneoer')
    '012'


    >>> originalDigits('fviefuro')
    '45'
    """
    digits_map = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
                  '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
    digits_map = {k: Counter(v) for k, v in digits_map.items()}
    unique_chars = {'0': 'z', '2': 'w', '4': 'u', '6': 'x', '8': 'g'}
    c = Counter(s)
    ans = ''
    for digit, un_ch in unique_chars.items():
        while un_ch in c:
            c -= digits_map[digit]
            ans += digit

    for digit, cntr in digits_map.items():
        while cntr & c == cntr:
            c -= cntr
            ans += digit
    return ''.join(sorted(ans))