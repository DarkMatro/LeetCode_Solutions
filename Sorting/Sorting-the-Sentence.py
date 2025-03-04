def sortSentence(s: str) -> str:
    """
    ID: 1859
    Tags:   String, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    A sentence is a list of words that are separated by a single space with no leading or trailing
    spaces. Each word consists of lowercase and uppercase English letters.

    A sentence can be shuffled by appending the 1-indexed word position to each word then
    rearranging the words in the sentence.

    For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or
    "is2 sentence4 This1 a3".
    Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original
    sentence.

    Parameters
    ----------
    s: str

    Returns
    -------
    str

    Examples
    --------
    >>> sortSentence("is2 sentence4 This1 a3")
    'This is a sentence'

    Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4",
    remove the numbers.

    >>> sortSentence("Myself2 Me1 I4 and3")
    'Me Myself and I'

    Explanation: Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove
    the numbers.
    """
    d = {x[-1]: x[:-1] for x in s.split(' ')}
    return ' '.join([d[x] for x in sorted(d.keys())])
