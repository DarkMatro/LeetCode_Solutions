def devowel(word: str) -> str:
    return "".join('*' if c in 'aeiou' else c for c in word.lower())

def spellchecker(wordlist: list[str], queries: list[str]) -> list[str]:
    """
    ID: 966
    Tags: Array, Hash Table, String
    Time: O(N)
    Memory: O(N)

    Task
    ----------
    Given a wordlist, we want to implement a spellchecker that converts a query word into a correct
    word.

    For a given query word, the spell checker handles two categories of spelling mistakes:

    Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query
    word is returned with the same case as the case in the wordlist.
    Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
    Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
    Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
    Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any
    vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is
    returned with the same case as the match in the wordlist.
    Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
    Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
    Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
    In addition, the spell checker operates under the following precedence rules:

    When the query exactly matches a word in the wordlist (case-sensitive), you should return the
    same word back.
    When the query matches a word up to capitlization, you should return the first such match in the
    wordlist.
    When the query matches a word up to vowel errors, you should return the first such match in the
    wordlist.
    If the query has no matches in the wordlist, you should return the empty string.
    Given some queries, return a list of words answer, where answer[i] is the correct word for
    query = queries[i].

    Parameters
    ----------
    wordlist: list[str]

    queries: list[str]

    Returns
    -------
    list[str]

    Examples
    --------
    >>> spellchecker(["KiTe","kite","hare","Hare"], ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"])
    ['kite', 'KiTe', 'KiTe', 'Hare', 'hare', '', '', 'KiTe', '', 'KiTe']


    >>> spellchecker(["yellow"], ["YellOw"])
    ['yellow']
    """
    word_set = set(wordlist)  # Exact match set
    cap_map = {}  # Case-insensitive map
    vowel_map = {}  # Vowel error map

    for word in wordlist:
        cap_map.setdefault(word.lower(), word)  # Store first occurrence of lowercase match
        vowel_map.setdefault(devowel(word), word)  # Store first occurrence of vowel-removed match

    result = []
    for query in queries:
        if query in word_set:
            result.append(query)  # Exact match
        elif query.lower() in cap_map:
            result.append(cap_map[query.lower()])  # Case-insensitive match
        elif devowel(query) in vowel_map:
            result.append(vowel_map[devowel(query)])  # Vowel error match
        else:
            result.append("")  # No match

    return result
