def findRestaurant(list1: list[str], list2: list[str]) -> list[str]:
    """
    ID: 599
    Tags:   Array, Hash Table, String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given two arrays of strings list1 and list2, find the common strings with the least index sum.

    A common string is a string that appeared in both list1 and list2.

    A common string with the least index sum is a common string such that if it appeared at list1[i]
    and list2[j] then i + j should be the minimum value among all the other common strings.

    Return all the common strings with the least index sum. Return the answer in any order.

    Parameters
    ----------
    list1: list[str]

    list2: list[str]

    Returns
    -------
    out : list[str]

    Examples
    --------
    >>> findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"])
    ['Shogun']

    Explanation: The only common string is "Shogun".

    >>> findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"])
    ['Shogun']

    Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.

    >>> findRestaurant(["happy","sad","good"], ["sad","happy","good"])
    ['sad', 'happy']

    Explanation: There are three common strings:
    "happy" with index sum = (0 + 1) = 1.
    "sad" with index sum = (1 + 0) = 1.
    "good" with index sum = (2 + 2) = 4.
    The strings with the least index sum are "sad" and "happy".
    """
    d = {s: i for i, s in enumerate(list1)}
    intersect = {s: d[s] + i for i, s in enumerate(list2) if s in d}
    min_v = min(intersect.values())
    return [k for k, v in intersect.items() if v == min_v]
