def colorTheArray(n: int, queries: list[list[int]]) -> list[int]:
    """
    ID: 2672
    Tags:   Array
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    There is a 0-indexed array nums of length n. Initially, all elements are uncolored (has a value of 0).

    You are given a 2D integer array queries where queries[i] = [indexi, colori].

    For each query, you color the index indexi with the color colori in the array nums.

    Return an array answer of the same length as queries where answer[i] is the number of adjacent elements with the
    same color after the ith query.

    More formally, answer[i] is the number of indices j, such that 0 <= j < n - 1 and nums[j] == nums[j + 1] and
    nums[j] != 0 after the ith query.

    Parameters
    ----------
    n: int

    queries: list[list[int]]

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> colorTheArray(4, [[0,2],[1,2],[3,1],[1,1],[2,1]])
    [0, 1, 1, 0, 2]

    Explanation: Initially array nums = [0,0,0,0], where 0 denotes uncolored elements of the array.
    - After the 1st query nums = [2,0,0,0]. The count of adjacent elements with the same color is 0.
    - After the 2nd query nums = [2,2,0,0]. The count of adjacent elements with the same color is 1.
    - After the 3rd query nums = [2,2,0,1]. The count of adjacent elements with the same color is 1.
    - After the 4th query nums = [2,1,0,1]. The count of adjacent elements with the same color is 0.
    - After the 5th query nums = [2,1,1,1]. The count of adjacent elements with the same color is 2.

    >>> colorTheArray(1, [[0,100000]])
    [0]

    Explanation: Initially array nums = [0], where 0 denotes uncolored elements of the array.
    - After the 1st query nums = [100000]. The count of adjacent elements with the same color is 0.

    >>> colorTheArray(8, [[6,2],[2,1],[0,6],[0,1],[0,4],[0,1],[5,7],[5,3],[7,6],[6,7],[0,4],[4,6],[4,2],[3,7],[4,4],[5,1]])
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    >>> colorTheArray(18, [[9,5],[14,15],[8,14],[0,4],[10,19],[13,11],[11,18],[8,15],[17,9],[10,1],[17,8],[9,13],[2,17],[0,10],[10,15],[10,19],[1,13],[7,1],[2,7],[13,16],[2,12],[1,19],[0,9],[4,1],[1,7],[3,18],[10,7],[13,2],[13,9],[0,17],[14,11],[12,7],[12,18],[16,15],[16,13],[7,12],[15,12],[7,18],[15,16],[15,6]])
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]

    >>> colorTheArray(17, [[11,3],[5,1],[16,2],[4,4],[5,1],[13,2],[15,1],[15,3],[8,1],[14,4],[1,3],[6,2],[8,2],[2,2],[3,4],[7,1],[10,2],[14,3],[6,5],[3,5],[5,5],[9,2],[2,3],[3,3],[4,1],[12,1],[0,4],[16,4],[8,1],[14,3],[15,3],[12,1],[11,5],[3,1],[2,4],[10,1],[14,5],[15,5],[5,2],[8,1],[6,5],[10,2]])
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 1, 2, 4, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 4, 3, 4, 3, 3, 3, 4]
    """
    adj = 0
    ans = []
    nums = [0] * n
    for q in queries:
        idx, new_color = q
        prev_color = nums[idx]
        if prev_color == new_color:
            ans.append(adj)
            continue
        nums[idx] = new_color
        # check right element
        if idx != n - 1:
            next_num = nums[idx + 1]
            if next_num == 0:
                pass
            elif prev_color == next_num and adj > 0:
                adj -= 1
            elif new_color == next_num:
                adj += 1
        # check left element
        if idx > 0:
            prev_num = nums[idx - 1]
            if prev_num == 0:
                pass
            elif prev_num == prev_color and adj > 0:
                adj -= 1
            elif new_color == prev_num:
                adj += 1
        ans.append(adj)
    return ans
