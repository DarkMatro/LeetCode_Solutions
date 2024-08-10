def is_palindrome(s: str) -> bool:
    """
    ID: 0125
    Tags:   Two Pointers, String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
     non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters
      and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.


    Parameters
    ----------
    s : str

    Returns
    -------
    out : bool

    Examples
    --------
    >>> is_palindrome("A man, a plan, a canal: Panama")
    True

    Explanation: "amanaplanacanalpanama" is a palindrome.

    >>> is_palindrome("race a car")
    False

    Explanation: "raceacar" is not a palindrome.

    >>> is_palindrome(" ")
    True

    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

    """
    s = [i for i in s.lower() if i.isalnum()]
    return s == s[::-1]
