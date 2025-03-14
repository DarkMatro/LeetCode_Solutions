from collections import Counter


def customSortString(order: str, s: str) -> str:
    """
    ID: 791
    Tags:   Hash Table, String, Sorting
    Time:   O(N+M)
    Memory: O(N+M)

    Task
    ----------
    You are given two strings order and s. All the characters of order are unique and were sorted in
    some custom order previously.

    Permute the characters of s so that they match the order that order was sorted. More
    specifically, if a character x occurs before a character y in order, then x should occur before
    y in the permuted string.

    Return any permutation of s that satisfies this property.

    Parameters
    ----------
    order: str

    s: str

    Returns
    -------
    str

    Examples
    --------
    >>> customSortString('cba', 'abcd')
    'cbad'

    Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b",
    and "a".

    Since "d" does not appear in order, it can be at any position in the returned string. "dcba",
    "cdba", "cbda" are also valid outputs.

    >>> customSortString('bcafg', 'abcd')
    'bcad'

    Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in
    s. The character "d" in s does not appear in order, so its position is flexible.

    Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b",
    "c", "a". "d" can be placed at any position since it's not in order. The output "bcad" correctly
    follows this rule. Other arrangements like "dbca" or "bcda" would also be valid, as long as "b",
    "c", "a" maintain their order.
    """
    order_d = {i: x for i, x in enumerate(order)}
    c = Counter(s)
    ans = ''
    for i in range(len(order)):
        ch = order_d[i]
        ans += ch * c[ch]
        del c[ch]
    for ch, cnt in c.items():
        ans += ch * cnt
    return ans
