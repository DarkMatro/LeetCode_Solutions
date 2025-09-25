from itertools import accumulate


def longestCommonPrefix(words: list[str]) -> list[int]:
    """
    ID: 3598
    Tags:   Array, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given an array of strings words. For each index i in the range [0, words.length - 1], perform the following
    steps:

    Remove the element at index i from the words array.
    Compute the length of the longest common prefix among all adjacent pairs in the modified array.
    Return an array answer, where answer[i] is the length of the longest common prefix between the adjacent pairs after
    removing the element at index i. If no adjacent pairs remain or if none share a common prefix, then answer[i] should be 0.

    Parameters
    ----------
    words: list[str]

    Returns
    -------
    list[int]

    Examples
    --------
    >>> longestCommonPrefix(["jump","run","run","jump","run"])
    [3, 0, 0, 3, 3]

    Explanation:
    Removing index 0:
    words becomes ["run", "run", "jump", "run"]
    Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)
    Removing index 1:
    words becomes ["jump", "run", "jump", "run"]
    No adjacent pairs share a common prefix (length 0)
    Removing index 2:
    words becomes ["jump", "run", "jump", "run"]
    No adjacent pairs share a common prefix (length 0)
    Removing index 3:
    words becomes ["jump", "run", "run", "run"]
    Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)
    Removing index 4:
    words becomes ["jump", "run", "run", "jump"]
    Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)

    >>> longestCommonPrefix(["dog","racer","car"])
    [0, 0, 0]

    Explanation:
    Removing any index results in an answer of 0.
    """
    def longestCommonPrefix(a: str, b: str) -> int:
        """Return length of longest common prefix between two strings"""
        i = 0
        while i < len(a) and i < len(b) and a[i] == b[i]:
            i += 1
        return i

    n = len(words)
    if n == 1:
        return [0]

    # Step 1: compute lcp for each adjacent pair
    lcp_arr = [longestCommonPrefix(words[i], words[i + 1]) for i in range(n - 1)]

    # Step 2: prefix/suffix max
    prefix_max = list(accumulate(lcp_arr, func=max))
    suffix_max = list(accumulate(lcp_arr[::-1], func=max))[::-1]

    # Step 3: answer for each removal
    answer = [0] * n
    for i in range(n):
        best = 0
        # max from left side
        if i >= 2:
            best = max(best, prefix_max[i - 2])
        if i <= n - 3:
            best = max(best, suffix_max[i + 1])
        # new pair formed
        if 0 < i < n - 1:
            best = max(best, longestCommonPrefix(words[i - 1], words[i + 1]))
        answer[i] = best

    return answer
