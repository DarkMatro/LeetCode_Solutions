def mostWordsFound(sentences: list[str]) -> int:
    """
    ID: 2114
    Tags:   Array, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

    You are given an array of strings sentences, where each sentences[i] represents a single sentence.

    Return the maximum number of words that appear in a single sentence.


    Parameters
    ----------
    sentences: list[str]

    Returns
    -------
    max_k : int

    Examples
    --------
    >>> mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])
    6

    Explanation:
    - The first sentence, "alice and bob love leetcode", has 5 words in total.
    - The second sentence, "i think so too", has 4 words in total.
    - The third sentence, "this is great thanks very much", has 6 words in total.
    Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.

    >>> mostWordsFound(["please wait", "continue to fight", "continue to win"])
    3

    Explanation: It is possible that multiple sentences contain the same number of words.
    In this example, the second and third sentences (underlined) have the same number of words.
    """
    max_k = 0
    for i in sentences:
        max_k = max(max_k, i.count(' ') + 1)
    return max_k
