def areSentencesSimilar(sentence1: str, sentence2: str) -> bool:
    """
    ID: 1813
    Tags: Array, Two Pointers, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given two strings sentence1 and sentence2, each representing a sentence composed of words. A sentence is a
    list of words that are separated by a single space with no leading or trailing spaces. Each word consists of only
    uppercase and lowercase English characters.

    Two sentences s1 and s2 are considered similar if it is possible to insert an arbitrary sentence (possibly empty)
    inside one of these sentences such that the two sentences become equal. Note that the inserted sentence must be
    separated from existing words by spaces.

    For example,

    s1 = "Hello Jane" and s2 = "Hello my name is Jane" can be made equal by inserting "my name is" between "Hello" and
    "Jane" in s1.
    s1 = "Frog cool" and s2 = "Frogs are cool" are not similar, since although there is a sentence "s are" inserted
    into s1, it is not separated from "Frog" by a space.
    Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return
    false.

    Parameters
    ----------
    sentence1: str

    sentence2: str

    Returns
    -------
    out : bool

    Examples
    --------
    >>> areSentencesSimilar("My name is Haley", "My Haley")
    True

    Explanation: sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".

    >>> areSentencesSimilar("of", "A lot of words")
    False

    Explanation: No single sentence can be inserted inside one of the sentences to make it equal to the other.

    >>> areSentencesSimilar("Eating right now", "Eating")
    True

    Explanation: sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.
    """
    w1, w2 = sentence1.split(), sentence2.split()
    n1, n2 = len(w1), len(w2)

    # match prefix
    i = 0
    while i < n1 and i < n2 and w1[i] == w2[i]:
        i += 1

    # match suffix
    j = 0
    while j < n1 - i and j < n2 - i and w1[-1 - j] == w2[-1 - j]:
        j += 1

    # If matched words cover all words of the smaller sentence
    return i + j >= min(n1, n2)
