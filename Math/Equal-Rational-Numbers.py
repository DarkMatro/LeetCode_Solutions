def isRationalEqual(s: str, t: str) -> bool:
    """
    ID: 972
    Tags:   Math, String
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Given two strings s and t, each of which represents a non-negative rational number, return true
    if and only if they represent the same number. The strings may use parentheses to denote the
    repeating part of the rational number.

    A rational number can be represented using up to three parts: <IntegerPart>, <NonRepeatingPart>,
    and a <RepeatingPart>. The number will be represented in one of the following three ways:

    <IntegerPart>
    For example, 12, 0, and 123.
    <IntegerPart><.><NonRepeatingPart>
    For example, 0.5, 1., 2.12, and 123.0001.
    <IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)>
    For example, 0.1(6), 1.(9), 123.00(1212).
    The repeating portion of a decimal expansion is conventionally denoted within a pair of round
    brackets. For example:

    1/6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66).

    Parameters
    ----------
    s: str
    t: str

    Returns
    -------
    out : bool

    Examples
    --------
    >>> isRationalEqual('0.(52)', '0.5(25)')
    True

    Explanation:
    Because "0.(52)" represents 0.52525252..., and "0.5(25)" represents 0.52525252525..... ,
    the strings represent the same number.

    >>> isRationalEqual('0.1666(6)', '0.166(66)')
    True

    >>> isRationalEqual('0.9(9)', '1.')
    True

    Explanation:
    Because "0.9(9)" represents 0.999999999... repeated forever, which equals 1.
    "1." represents the number 1, which is formed correctly: (IntegerPart) = "1" and
    (NonRepeatingPart) = "".

    """
    s_ = convert_str_to_float(s)
    t_ = convert_str_to_float(t)
    return s_ == t_

def convert_str_to_float(s: str) -> float:
    idx_s = s.find('(')
    if idx_s == -1:
        non_periodic_s = s
        per_s = ''
    else:
        non_periodic_s = s[:idx_s]
        per_s = s[idx_s + 1: -1]
    for i in range(20):
        non_periodic_s += per_s
    return float(non_periodic_s)
