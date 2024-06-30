def findOcurrences(text: str, first: str, second: str) -> list[str]:
    """
    ID: 1078
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given two strings first and second, consider occurrences in some text of the form "first second
    third", where second comes immediately after first, and third comes immediately after second.

    Return an array of all the words third for each occurrence of "first second third".

    Parameters
    ----------
    text: str

    first: str

    second: str

    Returns
    -------
    out: list[str]

    Examples
    --------
    >>> findOcurrences("alice is a good girl she is a good student", "a", "good")
    ['girl', 'student']

    >>> findOcurrences("we will we will rock you", "we", "will")
    ['we', 'rock']
    """
    words = text.split(' ')
    ans = []
    prev_prev = words[0]
    prev = words[1]
    for i in range(2, len(words)):
        word = words[i]
        if prev_prev == first and prev == second:
            ans.append(word)
        prev, prev_prev = word, prev
    return ans
