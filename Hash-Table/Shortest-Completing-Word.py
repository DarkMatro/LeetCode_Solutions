from collections import Counter


def shortestCompletingWord(licensePlate: str, words: list[str]) -> str:
    """
    ID: 748
    Tags:   Array, Hash Table, String
    Time:   O(NM)
    Memory: O(M)

    Task
    ----------
    Given a string licensePlate and an array of strings words, find the shortest completing word in
    words.

    A completing word is a word that contains all the letters in licensePlate. Ignore numbers and
    spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than
    once in licensePlate, then it must appear in the word the same number of times or more.

    For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and
    'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

    Return the shortest completing word in words. It is guaranteed an answer exists. If there are
    multiple shortest completing words, return the first one that occurs in words.

    Parameters
    ----------
    licensePlate: str

    words: list[str]

    Returns
    -------
    out : str

    Examples
    --------
    >>> shortestCompletingWord('1s3 PSt', ["step","steps","stripe","stepple"])
    'steps'

    Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
    "step" contains 't' and 'p', but only contains 1 's'.
    "steps" contains 't', 'p', and both 's' characters.
    "stripe" is missing an 's'.
    "stepple" is missing an 's'.
    Since "steps" is the only word containing all the letters, that is the answer.

    >>> shortestCompletingWord('1s3 456', ["looks","pest","stew","show"])
    'pest'

    Explanation: licensePlate only contains the letter 's'. All the words contain 's', but among
    these "pest", "stew", and "show" are shortest. The answer is "pest" because it is the word that
    appears earliest of the 3.
    """
    required_letters = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
    return min((word for word in words if not required_letters - Counter(word)), key=len)
