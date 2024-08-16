MOD = 10 ** 9 + 7


def numPrimeArrangements(n: int) -> int:
    """
    ID: 1175
    Tags:   Math
    Time:   O(Nsqrt(N))
    Memory: O(1)

    Task
    ----------
    Return the number of permutations of 1 to n so that prime numbers are at prime indices
    (1-indexed.)

    (Recall that an integer is prime if and only if it is greater than 1, and cannot be written as
    a product of two positive integers both smaller than it.)

    Since the answer may be large, return the answer modulo 10^9 + 7.

    Parameters
    ----------
    n: int

    Returns
    -------
    out : int

    Examples
    --------
    >>> numPrimeArrangements(5)
    12

    Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the
    prime number 5 is at index 1.

    >>> numPrimeArrangements(100)
    682289015
    """
    # Count the number of primes from 1 to n
    prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))

    # Non-prime count
    non_prime_count = n - prime_count

    # The result is the factorial of prime_count * factorial of non_prime_count
    return (factorial(prime_count) * factorial(non_prime_count)) % MOD


def is_prime(x):
    if x <= 1:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True


def factorial(x):
    result = 1
    for i in range(2, x + 1):
        result = (result * i) % MOD
    return result
