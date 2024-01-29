def countMatches(items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
    """
    ID: 1773
    Tags:   Array, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of
    the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

    The ith item is said to match the rule if one of the following is true:

    ruleKey == "type" and ruleValue == typei.
    ruleKey == "color" and ruleValue == colori.
    ruleKey == "name" and ruleValue == namei.
    Return the number of items that match the given rule.

    Parameters
    ----------
    strs : list[str]
        array of strings

    Returns
    -------
    and: str
        longest common prefix string amongst strs

    Examples
    --------
    >>> countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver")
    1

    Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].

    >>> countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type", "phone")
    2

    Explanation: There are only two items matching the given rule, which are ["phone","blue","pixel"]
    and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.

    """
    if ruleKey == 'type':
        idx = 0
    elif ruleKey == 'color':
        idx = 1
    else:
        idx = 2

    c = 0
    for i in items:
        if i[idx] == ruleValue:
            c += 1
    return c