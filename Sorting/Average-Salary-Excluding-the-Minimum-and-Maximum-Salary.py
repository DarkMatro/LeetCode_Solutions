def average(salary: list[int]) -> float:
    """
    ID: 1491
    Tags:   Array, Sorting
    Time:   O(NlogN)
    Memory: O(1)

    Task
    ----------
    You are given an array of unique integers salary where salary[i] is the salary of the ith
    employee.

    Return the average salary of employees excluding the minimum and maximum salary. Answers within
    10-5 of the actual answer will be accepted.

    Parameters
    ----------
    arr: list[int]

    Returns
    -------
    float

    Examples
    --------
    >>> average([4000,3000,1000,2000])
    2500.0

    Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
    Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

    >>> average([1000,2000,3000])
    2000.0

    Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
    Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
    """
    salary.sort()
    return sum(salary[1:-1]) / (len(salary) - 2)
