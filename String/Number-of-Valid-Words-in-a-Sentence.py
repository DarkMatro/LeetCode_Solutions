def countValidWords(sentence: str) -> int:
    """
    ID: 2047
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'),
    punctuation marks ('!', '.', and ','), and spaces (' ') only. Each sentence can be broken down
    into one or more tokens separated by one or more spaces ' '.

    A token is a valid word if all three of the following are true:

    It only contains lowercase letters, hyphens, and/or punctuation (no digits).
    There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters
    ("a-b" is valid, but "-ab" and "ab-" are not valid).
    There is at most one punctuation mark. If present, it must be at the end of the token
    ("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not valid).
    Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".

    Given a string sentence, return the number of valid words in sentence.

    Parameters
    ----------
    sentence : str

    Returns
    -------
    out : int

    Examples
    --------
    >>> countValidWords("cat and  dog")
    3

    >>> countValidWords("!this  1-s b8d!")
    0

    >>> countValidWords("alice and  bob are playing stone-game10")
    5
    """
    tokens = [x for x in sentence.split(' ') if x]
    punc = {',', '.', '!'}
    n_valid = 0
    for token in tokens:
        if any((x.isdigit() for x in token)):
            continue
        n_hyphens = token.count('-')
        if n_hyphens > 1:
            continue
        if n_hyphens == 1:
            idx = token.index('-')
            if idx in [0, len(token) - 1] or not token[idx - 1].isalpha() or not token[
                idx + 1].isalpha():
                continue
        if len(punc & set(token)) > 1:
            continue
        if any([x for x in punc if x in token and token.index(x) != len(token) - 1]):
            continue
        n_valid += 1
    return n_valid
