def isAcronym(words: list[str], s: str) -> bool:
    """
    ID: 2828
    Tags:   Array, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a string s, return the string after replacing every uppercase letter with the same
    lowercase letter.

    Parameters
    ----------
    words: list[str]

    s: str

    Returns
    -------
    bool

    Examples
    --------
    >>> isAcronym(["alice","bob","charlie"], "abc")
    True

    Explanation: The first character in the words "alice", "bob", and "charlie" are 'a', 'b', and
    'c', respectively. Hence, s = "abc" is the acronym.

    >>> isAcronym(["an","apple"], "a")
    False

    Explanation: The first character in the words "an" and "apple" are 'a' and 'a', respectively.
    The acronym formed by concatenating these characters is "aa".
    Hence, s = "a" is not the acronym.

    >>> isAcronym(["never","gonna","give","up","on","you"], "ngguoy")
    True

    Explanation: Explanation: By concatenating the first character of the words in the array, we
    get the string "ngguoy".
    Hence, s = "ngguoy" is the acronym.

    """
    n_s = len(s)
    n_w = len(words)
    if n_w != n_s:
        return False
    for i in range(len(s)):
        if words[i][0] != s[i]:
            return False
    return True
