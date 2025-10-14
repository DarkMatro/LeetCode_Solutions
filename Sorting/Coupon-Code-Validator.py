from collections import defaultdict


def validateCoupons(code: list[str], businessLine: list[str], isActive: list[bool]) -> list[str]:
    """
    ID: 3606
    Tags:   Array, Hash Table, String, Sorting
    Time:   O(N∗M+Klogk)
    Memory: O(N)

    Task
    ----------
    You are given three arrays of length n that describe the properties of n coupons: code, businessLine, and isActive.
    The ith coupon has:

    code[i]: a string representing the coupon identifier.
    businessLine[i]: a string denoting the business category of the coupon.
    isActive[i]: a boolean indicating whether the coupon is currently active.
    A coupon is considered valid if all of the following conditions hold:

    code[i] is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
    businessLine[i] is one of the following four categories: "electronics", "grocery", "pharmacy", "restaurant".
    isActive[i] is true.
    Return an array of the codes of all valid coupons, sorted first by their businessLine in the order: "electronics",
    "grocery", "pharmacy", "restaurant", and then by code in lexicographical (ascending) order within each category.

    Parameters
    ----------
    code: list[str]

    businessLine: list[str]

    isActive: list[bool]

    Returns
    -------
    list[str]

    Examples
    --------
    >>> validateCoupons(["SAVE20","","PHARMA5","SAVE@20"], ["restaurant","grocery","pharmacy","restaurant"], [True,True,True,True])
    ['PHARMA5', 'SAVE20']

    Explanation:
    First coupon is valid.
    Second coupon has empty code (invalid).
    Third coupon is valid.
    Fourth coupon has special character @ (invalid).

    >>> validateCoupons(["GROCERY15","ELECTRONICS_50","DISCOUNT10"], ["grocery","electronics","invalid"], [False,True,True])
    ['ELECTRONICS_50']

    Explanation:
    First coupon is inactive (invalid).
    Second coupon is valid.
    Third coupon has invalid business line (invalid).
    """
    valid_codes = defaultdict(list)
    correct_bl = {"electronics", "grocery", "pharmacy", "restaurant"}
    for cd, bl, is_active in zip(code, businessLine, isActive):
        if not is_active:
            continue
        if not bl in correct_bl:
            continue
        if not cd or not all([1 if x.isalnum() or x == '_' else 0 for x in cd]):
            continue
        valid_codes[bl].append(cd)
    ans = []
    for k in ["electronics", "grocery", "pharmacy", "restaurant"]:
        ans.extend(sorted(valid_codes[k]))
    return ans
