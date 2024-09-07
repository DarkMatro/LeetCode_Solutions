from string import ascii_lowercase

def decodeMessage(key: str, message: str) -> str:
    """
    ID: 2325
    Tags:   Hash Table, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given the strings key and message, which represent a cipher key and a secret message,
    respectively. The steps to decode message are as follows:

    Use the first appearance of all 26 lowercase English letters in key as the order of the
    substitution table.
    Align the substitution table with the regular English alphabet.
    Each letter in message is then substituted using the table.
    Spaces ' ' are transformed to themselves.
    For example, given key = "happy boy" (actual key would have at least one instance of each letter
    in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c',
    'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
    Return the decoded message.

    Parameters
    ----------
    key: str

    message: str

    Returns
    -------
    out : str

    Examples
    --------
    >>> decodeMessage('the quick brown fox jumps over the lazy dog', 'vkbs bs t suepuv')
    'this is a secret'

    Explanation:
    The diagram above shows the substitution table.
    It is obtained by taking the first appearance of each letter in "the quick brown fox jumps over
    the lazy dog".

    >>> decodeMessage('eljuxhpwnyrdgtqkviszcfmabo', 'zwx hnfx lqantp mnoeius ycgk vcnjrdb')
    'the five boxing wizards jump quickly'

    Explanation:
    The diagram above shows the substitution table.
    It is obtained by taking the first appearance of each letter in "eljuxhpwnyrdgtqkviszcfmabo".
    """
    i = 0
    d = {}
    for k in key:
        if k == ' ':
            continue
        if k not in d:
            d[k] = ascii_lowercase[i]
            i += 1
    ans = ''
    for x in message:
        if x == ' ':
            ans += ' '
            continue
        ans += d[x]
    return ans
