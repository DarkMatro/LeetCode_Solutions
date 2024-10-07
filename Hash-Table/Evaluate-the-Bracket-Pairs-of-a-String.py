def evaluate(s: str, knowledge: list[list[str]]) -> str:
    """
    ID: 1807
    Tags:   Array, Hash Table, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a string s that contains some bracket pairs, with each pair containing a non-empty
    key.

    For example, in the string "(name)is(age)yearsold", there are two bracket pairs that contain the
    keys "name" and "age".
    You know the values of a wide range of keys. This is represented by a 2D string array knowledge
    where each knowledge[i] = [keyi, valuei] indicates that key keyi has a value of valuei.

    You are tasked to evaluate all of the bracket pairs. When you evaluate a bracket pair that
    contains some key keyi, you will:

    Replace keyi and the bracket pair with the key's corresponding valuei.
    If you do not know the value of the key, you will replace keyi and the bracket pair with a
    question mark "?" (without the quotation marks).
    Each key will appear at most once in your knowledge. There will not be any nested brackets in s.

    Return the resulting string after evaluating all of the bracket pairs.

    Parameters
    ----------
    s: str

    knowledge: list[list[str]]

    Returns
    -------
    out : str

    Examples
    --------
    >>> evaluate("(name)is(age)yearsold", [["name","bob"],["age","two"]])
    'bobistwoyearsold'

    Explanation:
    The key "name" has a value of "bob", so replace "(name)" with "bob".
    The key "age" has a value of "two", so replace "(age)" with "two".

    >>> evaluate("hi(name)", [["a","b"]])
    'hi?'

    Explanation: As you do not know the value of the key "name", replace "(name)" with "?".

    >>> evaluate("(a)(a)(a)aaa", [["a","yes"]])
    'yesyesyesaaa'

    Explanation: The same key can appear multiple times.
    The key "a" has a value of "yes", so replace all occurrences of "(a)" with "yes".
    Notice that the "a"s not in a bracket pair are not evaluated.
    """
    kn = {x[0]: x[1] for x in knowledge}
    ans = ''
    k = ''
    is_key = False
    for x in s:
        if x == '(':
            is_key = True
            continue
        if x == ')':
            is_key = False
            ans += kn.get(k, '?')
            k = ''
            continue
        if is_key:
            k += x
        else:
            ans += x
    return ans
