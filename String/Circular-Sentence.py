def isCircularSentence(sentence: str) -> bool:
    """
    ID: 2490
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    A sentence is a list of words that are separated by a single space with no leading or trailing
    spaces.

    For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
    Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English
    letters are considered different.

    A sentence is circular if:

    The last character of a word is equal to the first character of the next word.
    The last character of the last word is equal to the first character of the first word.
    For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all
    circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and
    "I like Leetcode" are not circular sentences.

    Given a string sentence, return true if it is circular. Otherwise, return false.

    Parameters
    ----------
    sentence: str

    Returns
    -------
    out: bool

    Examples
    --------
    >>> isCircularSentence("leetcode exercises sound delightful")
    True

    Explanation: The words in sentence are ["leetcode", "exercises", "sound", "delightful"].
    - leetcode's last character is equal to exercises's first character.
    - exercises's last character is equal to sound's first character.
    - sound's last character is equal to delightful's first character.
    - delightful's last character is equal to leetcode's first character.
    The sentence is circular.

    >>> isCircularSentence("eetcode")
    True

    Explanation: The words in sentence are ["eetcode"].
    - eetcode's last character is equal to eetcode's first character.
    The sentence is circular.

    >>> isCircularSentence("Leetcode is cool")
    False

    Explanation: The words in sentence are ["Leetcode", "is", "cool"].
    - Leetcode's last character is not equal to is's first character.
    The sentence is not circular.
    """
    words = sentence.split(' ')
    if words[0][0] != words[-1][-1]:
        return False
    prev = words[0]
    for i in range(1, len(words)):
        word = words[i]
        if word[0] != prev[-1]:
            return False
        prev = word
    return True
