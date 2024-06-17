def vowelStrings(words: list[str], left: int, right: int) -> int:
    """
    ID: 2586
    Tags:   Array, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a 0-indexed array of string words and two integers left and right.

    A string is called a vowel string if it starts with a vowel character and ends with a vowel
    character where vowel characters are 'a', 'e', 'i', 'o', and 'u'.

    Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right].

    Parameters
    ----------
    words: list[str]

    left: int

    right: int

    Returns
    -------
    out: int

    Examples
    --------
    >>> vowelStrings(["are","amy","u"], 0, 2)
    2

    Explanation:
    - "are" is a vowel string because it starts with 'a' and ends with 'e'.
    - "amy" is not a vowel string because it does not end with a vowel.
    - "u" is a vowel string because it starts with 'u' and ends with 'u'.
    The number of vowel strings in the mentioned range is 2.

    >>> vowelStrings(["hey","aeo","mu","ooo","artro"], 1, 4)
    3

    Explanation:
    - "aeo" is a vowel string because it starts with 'a' and ends with 'o'.
    - "mu" is not a vowel string because it does not start with a vowel.
    - "ooo" is a vowel string because it starts with 'o' and ends with 'o'.
    - "artro" is a vowel string because it starts with 'a' and ends with 'o'.
    The number of vowel strings in the mentioned range is 3.
    """
    vowel_letters = {'a', 'e', 'i', 'o', 'u'}
    ans = 0
    for i in range(left, right + 1):
        word = words[i]
        if word[0] in vowel_letters and word[-1] in vowel_letters:
            ans += 1
    return ans
