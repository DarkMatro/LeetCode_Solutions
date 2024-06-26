def areNumbersAscending(s: str) -> bool:
    """
    ID: 2042
    Tags:   String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    A sentence is a list of tokens separated by a single space with no leading or trailing spaces.
    Every token is either a positive number consisting of digits 0-9 with no leading zeros, or a
    word consisting of lowercase English letters.

    For example, "a puppy has 2 eyes 4 legs" is a sentence with seven tokens: "2" and "4" are
    numbers and the other tokens such as "puppy" are words.
    Given a string s representing a sentence, you need to check if all the numbers in s are strictly
    increasing from left to right (i.e., other than the last number, each number is strictly smaller
    than the number on its right in s).

    Return true if so, or false otherwise.

    Parameters
    ----------
    s: str

    Returns
    -------
    out: bool

    Examples
    --------
    >>> areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles")
    True

    Explanation:
    The numbers in s are: 1, 3, 4, 6, 12.
    They are strictly increasing from left to right: 1 < 3 < 4 < 6 < 12.

    >>> areNumbersAscending("hello world 5 x 5")
    False

    Explanation:
    The numbers in s are: 5, 5. They are not strictly increasing.

    >>> areNumbersAscending("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s")
    False

    Explanation:
    The numbers in s are: 7, 51, 50, 60. They are not strictly increasing.
    """
    nums = [int(x) for x in s.split(' ') if x.isnumeric()]
    ans = True
    prev = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        if num <= prev:
            ans = False
            break
        prev = num
    return ans
