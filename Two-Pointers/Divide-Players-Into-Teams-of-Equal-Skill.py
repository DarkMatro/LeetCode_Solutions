def dividePlayers(skill: list[int]) -> int:
    """
    ID: 2491
    Tags:   Array, Hash Table, Two Pointers, Sorting
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player.
    Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.

    The chemistry of a team is equal to the product of the skills of the players on that team.

    Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams
    such that the total skill of each team is equal.

    Parameters
    ----------
    skill : list[int]

    Returns
    -------
    out : int

    Examples
    --------
    >>> dividePlayers([3,2,5,1,3,4])
    22

    Explanation:
    Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
    The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.

    >>> dividePlayers([3,4])
    12

    Explanation:
    The two players form a team with a total skill of 7.
    The chemistry of the team is 3 * 4 = 12.

    >>> dividePlayers([1,1,2,3])
    -1

    Explanation:
    There is no way to divide the players into teams such that the total skill of each team is equal.
    """
    skill.sort()
    lp, rp = 0, len(skill) - 1
    ch = skill[0] + skill[-1]
    ans = 0
    while lp <= rp:
        lx, rx = skill[lp], skill[rp]
        s = lx + rx
        if s != ch:
            return -1
        ans += lx * rx
        lp += 1
        rp -= 1
    return ans