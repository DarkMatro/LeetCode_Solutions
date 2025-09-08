def shortestToChar(s: str, c: str) -> list[int]:
    """
    ID: 821
    Tags:   Array, Two Pointers, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given a string s and a character c that occurs in s, return an array of integers answer where
    answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

    The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

    Parameters
    ----------
    s: str
    c: str

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> shortestToChar("loveleetcode", 'e')
    [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

    Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
    The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
    The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
    For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same:
    abs(4 - 3) == abs(4 - 5) = 1.
    The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.

    >>> shortestToChar("aaab", 'b')
    [3, 2, 1, 0]
    """
    n = len(s)
    answer = [float('inf')] * n

    # Pass 1: left to right
    prev = float('-inf')
    for i in range(n):
        if s[i] == c:
            prev = i
        answer[i] = i - prev

    # Pass 2: right to left
    prev = float('inf')
    for i in range(n - 1, -1, -1):
        if s[i] == c:
            prev = i
        answer[i] = min(answer[i], prev - i)

    return answer
