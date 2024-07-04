from string import punctuation


def strongPasswordCheckerII(password: str) -> bool:
    """
    ID: 2299
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    A password is said to be strong if it satisfies all the following criteria:

    It has at least 8 characters.
    It contains at least one lowercase letter.
    It contains at least one uppercase letter.
    It contains at least one digit.
    It contains at least one special character. The special characters are the characters in the
    following string: "!@#$%^&*()-+".
    It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this
    condition, but "aba" does not).
    Given a string password, return true if it is a strong password. Otherwise, return false.

    Parameters
    ----------
    password: str

    Returns
    -------
    out: bool

    Examples
    --------
    >>> strongPasswordCheckerII("IloveLe3tcode!")
    True

    Explanation: The password meets all the requirements. Therefore, we return true.

    >>> strongPasswordCheckerII("Me+You--IsMyDream")
    False

    Explanation: The password does not contain a digit and also contains 2 of the same character in
    adjacent positions. Therefore, we return false.

    >>> strongPasswordCheckerII("1aB!")
    False

    Explanation: The password does not meet the length requirement. Therefore, we return false.
    """
    has_lower = False
    has_upper = False
    has_digit = False
    has_punc = False
    has_adjacent = False
    punc = set(punctuation)
    prev = ''
    for i, x in enumerate(password):
        if x.islower():
            has_lower = True
        if x.isupper():
            has_upper = True
        if x.isdigit():
            has_digit = True
        if x in punc:
            has_punc = True
        if i > 0 and x == prev:
            has_adjacent = True
        prev = x
    return len(
        password) >= 8 and has_lower and has_upper and has_digit and has_punc and not has_adjacent
