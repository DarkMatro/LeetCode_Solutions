def canChange(start: str, target: str) -> bool:
    """
    ID: 2337
    Tags:   Two Pointers, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R',
    and '_' where:

    The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space
    directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
    The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
    Return true if it is possible to obtain the string target by moving the pieces of the string start any number of
    times. Otherwise, return false.

    Parameters
    ----------
    start: str

    target: str

    Returns
    -------
    out : bool

    Examples
    --------
    >>> canChange("_L__R__R_", "L______RR")
    True

    Explanation: We can obtain the string target from start by doing the following moves:
    - Move the first piece one step to the left, start becomes equal to "L___R__R_".
    - Move the last piece one step to the right, start becomes equal to "L___R___R".
    - Move the second piece three steps to the right, start becomes equal to "L______RR".
    Since it is possible to get the string target from start, we return true.

    >>> canChange("R_L_", "__LR")
    False

    Explanation: The 'R' piece in the string start can move one step to the right to obtain "_RL_".
    After that, no pieces can move anymore, so it is impossible to obtain the string target from start.

    >>> canChange("_R", "R_")
    False

    Explanation: The piece in the string start can move only to the right, so it is impossible to obtain the string
    target from start.
    """
    start_length = len(start)
    # pointers for start string and target string
    start_index, target_index = (0, 0)

    while start_index < start_length or target_index < start_length:
        # skip underscores in start
        while start_index < start_length and start[start_index] == "_":
            start_index += 1

        # skip underscores in target
        while target_index < start_length and target[target_index] == "_":
            target_index += 1

        # if one string exhausted, both strings should be exhausted
        if start_index == start_length or target_index == start_length:
            return (
                    start_index == start_length and target_index == start_length
            )

        # check if the pieces match and follow movement rules
        if (
                start[start_index] != target[target_index]
                or (start[start_index] == "L" and start_index < target_index)
                or (start[start_index] == "R" and start_index > target_index)
        ):
            return False

        start_index += 1
        target_index += 1

    # if all conditions satisfied, return true
    return True
