from collections import Counter

def oddString(words: list[str]) -> str:
    """
    ID: 2451
    Tags:   Array, Hash Table, String
    Time:   O(Nn)
    Memory: O(M)

    Task
    ----------
    You are given an array of equal-length strings words. Assume that the length of each string is
    n.

    Each string words[i] can be converted into a difference integer array difference[i] of length
    n - 1 where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2. Note that the
    difference between two letters is the difference between their positions in the alphabet i.e.
    the position of 'a' is 0, 'b' is 1, and 'z' is 25.

    For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].
    All the strings in words have the same difference integer array, except one. You should find
    that string.

    Return the string in words that has different difference integer array.

    Parameters
    ----------
    words: list[str]

    Returns
    -------
    out : str

    Examples
    --------
    >>> oddString(["adc","wzy","abc"])
    'abc'

    Explanation:
    - The difference integer array of "adc" is [3 - 0, 2 - 3] = [3, -1].
    - The difference integer array of "wzy" is [25 - 22, 24 - 25]= [3, -1].
    - The difference integer array of "abc" is [1 - 0, 2 - 1] = [1, 1].
    The odd array out is [1, 1], so we return the corresponding string, "abc".

    >>> oddString(["aaa","bob","ccc","ddd"])
    'bob'

    Explanation:
    All the integer arrays are [0, 0] except for "bob", which corresponds to [13, -13].
    """

    # Функция для вычисления разностного массива в виде кортежа
    def getDifferenceArray(word: str) -> tuple[int]:
        return tuple(ord(word[j + 1]) - ord(word[j]) for j in range(len(word) - 1))

    dif = [getDifferenceArray(w) for w in words]
    diff_count = Counter(dif)
    min(diff_count, key=diff_count.get)
    idx = dif.index(min(diff_count, key=diff_count.get))

    return words[idx] if idx != -1 else ''
