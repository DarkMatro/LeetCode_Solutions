def peopleIndexes(favoriteCompanies: list[list[str]]) -> list[int]:
    """
    ID: 1452
    Tags:   Array, Hash Table, String
    Time:   O(M*N^2)
    Memory: O(N)

    Task
    ----------
    Given the array favoriteCompanies where favoriteCompanies[i] is the list of favorites companies
    for the ith person (indexed from 0).

    Return the indices of people whose list of favorite companies is not a subset of any other list
    of favorites companies. You must return the indices in increasing order.

    Parameters
    ----------
    favoriteCompanies: list[list[str]]

    Returns
    -------
    out : list[int]

    Examples
    --------
    >>> peopleIndexes([["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]])
    [0, 1, 4]

    Explanation:
    Person with index=2 has favoriteCompanies[2]=["google","facebook"] which is a subset of
    favoriteCompanies[0]=["leetcode","google","facebook"] corresponding to the person with index 0.
    Person with index=3 has favoriteCompanies[3]=["google"] which is a subset of
    favoriteCompanies[0]=["leetcode","google","facebook"] and
    favoriteCompanies[1]=["google","microsoft"].
    Other lists of favorite companies are not a subset of another list, therefore, the answer is
    [0,1,4].

    >>> peopleIndexes([["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]])
    [0, 1]

    Explanation:
    In this case favoriteCompanies[2]=["facebook","google"] is a subset of
    favoriteCompanies[0]=["leetcode","google","facebook"], therefore, the answer is [0,1].

    >>> peopleIndexes([["leetcode"],["google"],["facebook"],["amazon"]])
    [0, 1, 2, 3]
    """
    favoriteCompanies = [set(companyList) for companyList in favoriteCompanies]

    ans = []

    for i, fav_i in enumerate(favoriteCompanies):
        is_subset = False
        for j, fav_j in enumerate(favoriteCompanies):
            if i != j and fav_i.issubset(fav_j):
                is_subset = True
                break
        if not is_subset:
            ans.append(i)
    return ans
