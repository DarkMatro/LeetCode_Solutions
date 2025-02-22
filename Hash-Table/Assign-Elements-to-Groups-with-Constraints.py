def assignElements(groups: list[int], elements: list[int]) -> list[int]:
    """
    ID: 3447
    Tags:   Array, Hash Table
    Time:   O(N*sqrt(N))
    Memory: O(N)

    Task
    ----------
    You are given an integer array groups, where groups[i] represents the size of the ith group.
    You are also given an integer array elements.

    Your task is to assign one element to each group based on the following rules:

    An element at index j can be assigned to a group i if groups[i] is divisible by elements[j].
    If there are multiple elements that can be assigned, assign the element with the smallest
    index j.
    If no element satisfies the condition for a group, assign -1 to that group.
    Return an integer array assigned, where assigned[i] is the index of the element chosen for group
    i, or -1 if no suitable element exists.

    Note: An element may be assigned to more than one group.

    Parameters
    ----------
    groups: list[int]

    elements: list[int]

    Returns
    -------
    list[int]

    Examples
    --------
    >>> assignElements([8,4,3,2,4], [4,2])
    [0, 0, -1, 1, 0]

    Explanation:
    elements[0] = 4 is assigned to groups 0, 1, and 4.
    elements[1] = 2 is assigned to group 3.
    Group 2 cannot be assigned any element.

    >>> assignElements([2,3,5,7], [5,3,3])
    [-1, 1, 0, -1]

    Explanation:
    elements[1] = 3 is assigned to group 1.
    elements[0] = 5 is assigned to group 2.
    Groups 0 and 3 cannot be assigned any element.

    >>> assignElements([10,21,30,41], [2,1])
    [0, 1, 0, 1]

    Explanation:
    elements[0] = 2 is assigned to the groups with even values, and elements[1] = 1 is assigned to
    the groups with odd values.
    """
    ans = [-1] * len(groups)
    el_idx = {}
    for i, e in enumerate(elements):
        if e not in el_idx:
            el_idx[e] = i

    for i, g in enumerate(groups):
        divisors = find_divisors(g)
        ass_divs = divisors & el_idx.keys()
        if ass_divs:
            ans[i] = min(el_idx[k] for k in ass_divs & el_idx.keys())
    return ans


def find_divisors(n: int) -> set:
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors