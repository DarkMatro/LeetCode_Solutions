def toGoatLatin(sentence: str) -> str:
    """
    ID: 0824
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a string sentence that consist of words separated by spaces. Each word consists of
    lowercase and uppercase letters only.

    We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
    The rules of Goat Latin are as follows:

    If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
    For example, the word "apple" becomes "applema".
    If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to
    the end, then add "ma".
    For example, the word "goat" becomes "oatgma".
    Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
    For example, the first word gets "a" added to the end, the second word gets "aa" added to the
    end, and so on.
    Return the final sentence representing the conversion from sentence to Goat Latin.

    Parameters
    ----------
    sentence: str

    Returns
    -------
    out: str

    Examples
    --------
    >>> toGoatLatin("I speak Goat Latin")
    'Imaa peaksmaaa oatGmaaaa atinLmaaaaa'

    >>> toGoatLatin("The quick brown fox jumped over the lazy dog")
    'heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa'
    """
    words = sentence.split(' ')
    ans = ''
    for i, w in enumerate(words):
        if w[0].lower() not in ['a', 'e', 'i', 'o', 'u']:
            w = w[1:] + w[0]
        w += 'ma'
        ans += w + 'a' * (i + 1) + ' '
    return ans.rstrip()
