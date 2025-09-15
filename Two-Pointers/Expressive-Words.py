from itertools import groupby


def expressiveWords(s: str, words: list[str]) -> int:
    """
    ID: 809
    Tags: Array, Two Pointers, String
    Time:   O(S+Sum(W))
    Memory: O(S+W)

    Task
    ----------
    Sometimes people repeat letters to represent extra feeling. For example:

    "hello" -> "heeellooo"
    "hi" -> "hiiii"
    In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll",
    "ooo".

    You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal
    to s by any number of applications of the following extension operation: choose a group consisting of characters c,
    and add some number of characters c to the group so that the size of the group is three or more.

    For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get
    "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll"
    to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two
    extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
    Return the number of query strings that are stretchy.

    Parameters
    ----------
    s: str

    words: list[str]

    Returns
    -------
    out : int

    Examples
    --------
    >>> expressiveWords("heeellooo", ["hello", "hi", "helo"])
    1

    Explanation: We can extend "e" and "o" in the word "hello" to get "heeellooo".
    We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.

    >>> expressiveWords("zzzzzyyyyy", ["zzyy","zy","zyy"])
    3
    """

    def is_expressive(s_group: list, w_group: list) -> bool:
        if len(s_group) != len(w_group):
            return False
        for (s_char, s_n), (w_char, w_n) in zip(sg, wg):
            if s_char != w_char or (3 > s_n != w_n) or (s_n == 3 and w_n > s_n):
                return False
        return True

    sg = [(char, len(list(gr))) for char, gr in groupby(s)]
    ans = 0
    for w in words:
        wg = [(char, len(list(gr))) for char, gr in groupby(w)]
        ans += 1 if is_expressive(sg, wg) else 0
    return ans
