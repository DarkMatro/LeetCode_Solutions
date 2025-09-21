def circularArrayLoop(nums: list[int]) -> bool:
    """
    ID: 457
    Tags: Array, Hash Table, Two Pointers
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are playing a game involving a circular array of non-zero integers nums. Each nums[i] denotes the number of
    indices forward/backward you must move if you are located at index i:

    If nums[i] is positive, move nums[i] steps forward, and
    If nums[i] is negative, move nums[i] steps backward.
    Since the array is circular, you may assume that moving forward from the last element puts you on the first element,
    and moving backwards from the first element puts you on the last element.

    A cycle in the array consists of a sequence of indices seq of length k where:

    Following the movement rules above results in the repeating index sequence seq[0] -> seq[1] -> ... -> seq[k - 1] ->
    seq[0] -> ...
    Every nums[seq[j]] is either all positive or all negative.
    k > 1
    Return true if there is a cycle in nums, or false otherwise.

    Parameters
    ----------
    nums: list[int]

    Returns
    -------
    out : bool

    Examples
    --------
    >>> circularArrayLoop([2,-1,1,2,2])
    True

    Explanation: The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping
    backward.
    We can see the cycle 0 --> 2 --> 3 --> 0 --> ..., and all of its nodes are white (jumping in the same direction).

    >>> circularArrayLoop([-1,-2,-3,-4,-5,6])
    False

    Explanation: The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping
    backward.
    The only cycle is of size 1, so we return false.

    >>> circularArrayLoop([1,-1,5,1,4])
    True

    Explanation: The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping
    backward.
    We can see the cycle 0 --> 1 --> 0 --> ..., and while it is of size > 1, it has a node jumping forward and a node
    jumping backward, so it is not a cycle.
    We can see the cycle 3 --> 4 --> 3 --> ..., and all of its nodes are white (jumping in the same direction).
    """
    n = len(nums)

    def next_index(i):
        return (i + nums[i]) % n

    for i in range(n):
        if nums[i] == 0:
            continue  # already visited

        slow, fast = i, i
        direction = nums[i] > 0  # True = positive direction

        while True:
            # Move slow pointer
            next_slow = next_index(slow)
            # Move fast pointer twice
            next_fast = next_index(fast)
            if nums[next_fast] * nums[fast] <= 0:  # direction mismatch
                break
            next_fast = next_index(next_fast)

            # Check direction consistency
            if nums[next_slow] * nums[slow] <= 0 or nums[next_fast] * nums[fast] <= 0:
                break

            slow, fast = next_slow, next_fast

            if slow == fast:
                # single-element cycle is invalid
                if slow == next_index(slow):
                    break
                return True

        # Mark all nodes in this path as visited
        marker = i
        while nums[marker] * (1 if direction else -1) > 0:
            nxt = next_index(marker)
            nums[marker] = 0
            marker = nxt

    return False
