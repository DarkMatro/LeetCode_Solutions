def maxBuilding(n: int, restrictions: list[list[int]]) -> int:
    """
    ID: 1840
    Tags:   Array, Math, Sorting
    Time:   O(NlogN)
    Memory: O(N)

    Task
    ----------
    You want to build n new buildings in a city. The new buildings will be built in a line and are
    labeled from 1 to n.

    However, there are city restrictions on the heights of the new buildings:

    The height of each building must be a non-negative integer.
    The height of the first building must be 0.
    The height difference between any two adjacent buildings cannot exceed 1.
    Additionally, there are city restrictions on the maximum height of specific buildings. These
    restrictions are given as a 2D integer array restrictions where
    restrictions[i] = [idi, maxHeighti] indicates that building idi must have a height less than or
    equal to maxHeighti.

    It is guaranteed that each building will appear at most once in restrictions, and building 1
    will not be in restrictions.

    Return the maximum possible height of the tallest building.

    Parameters
    ----------
    n: int

    restrictions: list[list[int]]

    Returns
    -------
    int

    Examples
    --------
    >>> maxBuilding(5, [[2,1],[4,1]])
    2

    Explanation: The green area in the image indicates the maximum allowed height for each building.
    We can build the buildings with heights [0,1,2,1,2], and the tallest building has a height of 2.

    >>> maxBuilding(6, [])
    5

    Explanation: The green area in the image indicates the maximum allowed height for each building.
    We can build the buildings with heights [0,1,2,3,4,5], and the tallest building has a height of
    5.

    >>> maxBuilding(10, [[5,3],[2,5],[7,4],[10,3]])
    5

    Explanation: The green area in the image indicates the maximum allowed height for each building.
    We can build the buildings with heights [0,1,2,3,3,4,4,5,4,3], and the tallest building has a
    height of 5.
    """
    # Step 1: Include (n, n-1) as a default restriction
    restrictions.append([1, 0])
    restrictions.append([n, n - 1])

    # Step 2: Sort restrictions by building index
    restrictions.sort()

    # Step 3: Left-to-Right Pass - Ensure valid heights based on increasing indices
    for i in range(1, len(restrictions)):
        idx1, h1 = restrictions[i - 1]
        idx2, h2 = restrictions[i]
        restrictions[i][1] = min(h2, h1 + (idx2 - idx1))

    # Step 4: Right-to-Left Pass - Ensure valid heights based on decreasing indices
    for i in range(len(restrictions) - 2, -1, -1):
        idx1, h1 = restrictions[i]
        idx2, h2 = restrictions[i + 1]
        restrictions[i][1] = min(h1, h2 + (idx2 - idx1))

    # Step 5: Compute the max possible building height
    max_height = 0
    for i in range(1, len(restrictions)):
        idx1, h1 = restrictions[i - 1]
        idx2, h2 = restrictions[i]
        # Maximum possible height between two restricted buildings
        peak = (h1 + h2 + (idx2 - idx1)) // 2
        max_height = max(max_height, peak)

    return max_height
