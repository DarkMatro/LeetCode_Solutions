def removeAnagrams(words: list[str]) -> list[str]:
    """
    ID: 2273
    Tags:   Array, Hash Table, String, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    You are given a 0-indexed string array words, where words[i] consists of lowercase English
    letters.

    In one operation, select any index i such that 0 < i < words.length and words[i - 1] and
    words[i] are anagrams, and delete words[i] from words. Keep performing this operation as long as
    you can select an index that satisfies the conditions.

    Return words after performing all operations. It can be shown that selecting the indices for
    each operation in any arbitrary order will lead to the same result.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase
    using all the original letters exactly once. For example, "dacb" is an anagram of "abdc".

    Parameters
    ----------
    words: list[str]

    Returns
    -------
    list[str]

    Examples
    --------
    >>> removeAnagrams(["abba","baba","bbaa","cd","cd"])
    ['abba', 'cd']

    Explanation: One of the ways we can obtain the resultant array is by using the following
    operations:
    - Since words[2] = "bbaa" and words[1] = "baba" are anagrams, we choose index 2 and delete
     words[2].
      Now words = ["abba","baba","cd","cd"].
    - Since words[1] = "baba" and words[0] = "abba" are anagrams, we choose index 1 and delete
     words[1].
      Now words = ["abba","cd","cd"].
    - Since words[2] = "cd" and words[1] = "cd" are anagrams, we choose index 2 and delete words[2].
      Now words = ["abba","cd"].
    We can no longer perform any operations, so ["abba","cd"] is the final answer.

    >>> removeAnagrams(["a","b","c","d","e"])
    ['a', 'b', 'c', 'd', 'e']

    Explanation: No two adjacent strings in words are anagrams of each other, so no operations are
    performed.
    """
    return [words[i] for i in range(0, len(words)) if
            i == 0 or sorted(words[i]) != sorted(words[i - 1])]