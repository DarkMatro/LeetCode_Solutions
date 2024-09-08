from collections import Counter
from string import ascii_lowercase

def uniqueMorseRepresentations(words: list[str]) -> int:
    """
    ID: 804
    Tags:   Array, Hash Table, String
    Time:   O(NM)
    Memory: O(N)

    Task
    ----------
    International Morse Code defines a standard encoding where each letter is mapped to a series of
    dots and dashes, as follows:

    'a' maps to ".-",
    'b' maps to "-...",
    'c' maps to "-.-.", and so on.
    For convenience, the full table for the 26 letters of the English alphabet is given below:

    [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",
    ".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    Given an array of strings words where each word can be written as a concatenation of the Morse
    code of each letter.

    For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-",
    and "-...". We will call such a concatenation the transformation of a word.
    Return the number of different transformations among all words we have.

    Parameters
    ----------
    words: list[str]

    Returns
    -------
    out : int

    Examples
    --------
    >>> uniqueMorseRepresentations(["gin","zen","gig","msg"])
    2

    Explanation: The transformation of each word is:
    "gin" -> "--...-."
    "zen" -> "--...-."
    "gig" -> "--...--."
    "msg" -> "--...--."
    There are 2 different transformations: "--...-." and "--...--.".

    >>> uniqueMorseRepresentations(["a"])
    1
    """
    codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
             "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
             "-.--", "--.."]
    d = dict(zip(ascii_lowercase, codes))
    ans = []
    for w in words:
        new_w = ''
        for x in w:
            new_w += d[x]
        ans.append(new_w)
    return len(Counter(ans))
