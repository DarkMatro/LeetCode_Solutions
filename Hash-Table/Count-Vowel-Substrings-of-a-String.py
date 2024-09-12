def countVowelSubstrings(word: str) -> int:
    """
    ID: 2062
    Tags:   Hash Table, String
    Time:   O(N^2)
    Memory: O(1)

    Task
    ----------
    A substring is a contiguous (non-empty) sequence of characters within a string.

    A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and
    has all five vowels present in it.

    Given a string word, return the number of vowel substrings in word.

    Parameters
    ----------
    word: str

    Returns
    -------
    out : int

    Examples
    --------
    >>> countVowelSubstrings('aeiouu')
    2

    Explanation:
    The vowel substrings of word are as follows (underlined):
    - "aeiou_u"
    - "aeiouu"

    >>> countVowelSubstrings('unicornarihan')
    0

    Explanation: Not all 5 vowels are present, so there are no vowel substrings.

    >>> countVowelSubstrings('cuaieuouac')
    7

    Explanation: The vowel substrings of word are as follows (underlined):
    - "c_uaieuo_uac"
    - "c_uaieuou_ac"
    - "c_uaieuoua_c"
    - "cu_aieuo_uac"
    - "cu_aieuou_ac"
    - "cu_aieuoua_c"
    - "cua_ieuoua_c"
    """
    vowels = set('aeiou')
    total_count = 0

    # Loop through each starting index of the string
    for i in range(len(word)):
        seen_vowels = set()

        # Try to build substrings starting from index i
        for j in range(i, len(word)):
            # If the character is a vowel, add it to the seen_vowels set
            if word[j] in vowels:
                seen_vowels.add(word[j])

                # If all five vowels are in the set, increment the count
                if len(seen_vowels) == 5:
                    total_count += 1
            else:
                # If a consonant is encountered, stop searching this substring
                break

    return total_count
