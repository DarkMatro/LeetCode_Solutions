def nearestPalindromic(n: str) -> str:
    """
    ID: 564
    Tags:   Math, String
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Given a string n representing an integer, return the closest integer (not including itself),
    which is a palindrome. If there is a tie, return the smaller one.

    The closest is defined as the absolute difference minimized between two integers.

    Parameters
    ----------
    n: str

    Returns
    -------
    out : str

    Examples
    --------
    >>> nearestPalindromic('123')
    '121'

    >>> nearestPalindromic('1')
    '0'

    Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
    """
    length = len(n)
    candidates = set()

    # Handle the edge cases where the number length changes
    candidates.add(str(10 ** (length - 1) - 1))  # Edge case: 999 -> 1001, so consider 999
    candidates.add(str(10 ** length + 1))  # Edge case: 1000 -> 999, so consider 1001

    # Generate the base candidate by mirroring the left half
    prefix = n[:(length + 1) // 2]
    prefix_num = int(prefix)

    for i in [-1, 0, 1]:
        new_prefix = str(prefix_num + i)
        if length % 2 == 0:
            candidate = new_prefix + new_prefix[::-1]
        else:
            candidate = new_prefix + new_prefix[-2::-1]
        candidates.add(candidate)

    candidates.discard(n)  # Remove the original number itself

    # Find the closest palindrome
    closest = None
    min_diff = float('inf')

    original_num = int(n)

    for candidate in candidates:
        candidate_num = int(candidate)
        diff = abs(candidate_num - original_num)
        if diff < min_diff or (diff == min_diff and candidate_num < int(closest)):
            closest = candidate
            min_diff = diff

    return closest