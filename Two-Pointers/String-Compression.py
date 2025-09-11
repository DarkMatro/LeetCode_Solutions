def compress(chars: list[str]) -> int:
    """
    ID: 443
    Tags:   Two Pointers, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an array of characters chars, compress it using the following algorithm:

    Begin with an empty string s. For each group of consecutive repeating characters in chars:

    If the group's length is 1, append the character to s.
    Otherwise, append the character followed by the group's length.
    The compressed string s should not be returned separately, but instead, be stored in the input character array
    chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

    After you are done modifying the input array, return the new length of the array.

    You must write an algorithm that uses only constant extra space.

    Note: The characters in the array beyond the returned length do not matter and should be ignored.

    Parameters
    ----------
    chars: list[str]

    Returns
    -------
    out : int

    Examples
    --------
    >>> compress(["a","a","b","b","c","c","c"])
    6

    Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
    Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

    >>> compress(["a"])
    1

    Output: Return 1, and the first character of the input array should be: ["a"]
    Explanation: The only group is "a", which remains uncompressed since it's a single character.

    >>> compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
    4

    Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
    Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
    """
    i = 0
    res = 0
    while i < len(chars):
        group_length = 1
        while (i + group_length < len(chars)
               and chars[i + group_length] == chars[i]):
            group_length += 1
        chars[res] = chars[i]
        res += 1
        if group_length > 1:
            str_repr = str(group_length)
            chars[res:res + len(str_repr)] = list(str_repr)
            res += len(str_repr)
        i += group_length
    return res
