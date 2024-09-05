def fizzBuzz(n: int) -> list[str]:
    """
    ID: 0412
    Tags:   Math, String, Simulation
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.

    Parameters
    ----------
    n : int

    Returns
    -------
    list[str]

    Examples
    --------
    >>> fizzBuzz(3)
    ['1', '2', 'Fizz']

    >>> fizzBuzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']

    >>> fizzBuzz(15)
    ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
    """
    res = [''] * n
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            ans = 'FizzBuzz'
        elif i % 3 == 0:
            ans = 'Fizz'
        elif i % 5 == 0:
            ans = 'Buzz'
        else:
            ans = str(i)
        res[i - 1] = ans
    return res

