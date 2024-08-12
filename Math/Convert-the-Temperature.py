def convertTemperature(celsius: float) -> list[float]:
    """
    ID: 2469
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    You are given a non-negative floating point number rounded to two decimal places celsius, that
    denotes the temperature in Celsius.

    You should convert Celsius into Kelvin and Fahrenheit and return it as an array
    ans = [kelvin, fahrenheit].

    Return the array ans. Answers within 10-5 of the actual answer will be accepted.

    Note that:

    Kelvin = Celsius + 273.15
    Fahrenheit = Celsius * 1.80 + 32.00

    Parameters
    ----------
    celsius: float

    Returns
    -------
    out : list[float]

    Examples
    --------
    >>> convertTemperature(36.50)
    [309.65, 97.7]

    Explanation: Temperature at 36.50 Celsius converted in Kelvin is 309.65 and converted in
    Fahrenheit is 97.70.

    >>> convertTemperature(122.11)
    [395.26, 251.798]

    Explanation: Temperature at 122.11 Celsius converted in Kelvin is 395.26 and converted in
    Fahrenheit is 251.798.

    """
    return [celsius + 273.15, celsius * 1.8 + 32.]
