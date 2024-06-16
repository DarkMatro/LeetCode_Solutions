def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
    """
    ID: 1880
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    The letter value of a letter is its position in the alphabet starting from 0
    (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).

    The numerical value of some string of lowercase English letters s is the concatenation of the
    letter values of each letter in s, which is then converted into an integer.

    For example, if s = "acb", we concatenate each letter's letter value, resulting in "021". After
    converting it, we get 21.
    You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase
    English letters 'a' through 'j' inclusive.

    Return true if the summation of the numerical values of firstWord and secondWord equals the
    numerical value of targetWord, or false otherwise.

    Parameters
    ----------
    firstWord: str

    secondWord: str

    targetWord: str

    Returns
    -------
    out: bool

    Examples
    --------
    >>> isSumEqual("acb", "cba", "cdb")
    True

    Explanation:
    The numerical value of firstWord is "acb" -> "021" -> 21.
    The numerical value of secondWord is "cba" -> "210" -> 210.
    The numerical value of targetWord is "cdb" -> "231" -> 231.
    We return true because 21 + 210 == 231.

    >>> isSumEqual("aaa", "a", "aab")
    False

    Explanation:
    The numerical value of firstWord is "aaa" -> "000" -> 0.
    The numerical value of secondWord is "a" -> "0" -> 0.
    The numerical value of targetWord is "aab" -> "001" -> 1.
    We return false because 0 + 0 != 1.

    >>> isSumEqual("aaa", "a", "aaaa")
    True

    Explanation:
    The numerical value of firstWord is "aaa" -> "000" -> 0.
    The numerical value of secondWord is "a" -> "0" -> 0.
    The numerical value of targetWord is "aaaa" -> "0000" -> 0.
    We return true because 0 + 0 == 0.
    """
    first_value = [str(ord(x) - 97) for x in firstWord]
    first_value = ''.join(first_value)
    first_value = int(first_value)
    second_value = [str(ord(x) - 97) for x in secondWord]
    second_value = ''.join(second_value)
    second_value = int(second_value)
    target_value = [str(ord(x) - 97) for x in targetWord]
    target_value = ''.join(target_value)
    target_value = int(target_value)
    return first_value + second_value == target_value
