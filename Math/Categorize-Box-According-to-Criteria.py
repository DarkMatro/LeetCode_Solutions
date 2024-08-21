def categorizeBox(length: int, width: int, height: int, mass: int) -> str:
    """
    ID: 2525
    Tags:   Math
    Time:   O(1)
    Memory: O(1)

    Task
    ----------
    Given four integers length, width, height, and mass, representing the dimensions and mass of a
    box, respectively, return a string representing the category of the box.

    The box is "Bulky" if:
    Any of the dimensions of the box is greater or equal to 104.
    Or, the volume of the box is greater or equal to 109.
    If the mass of the box is greater or equal to 100, it is "Heavy".
    If the box is both "Bulky" and "Heavy", then its category is "Both".
    If the box is neither "Bulky" nor "Heavy", then its category is "Neither".
    If the box is "Bulky" but not "Heavy", then its category is "Bulky".
    If the box is "Heavy" but not "Bulky", then its category is "Heavy".
    Note that the volume of the box is the product of its length, width and height.

    Parameters
    ----------
    length: int

    width: int

    height: int

    mass: int

    Returns
    -------
    out : str

    Examples
    --------
    >>> categorizeBox(1000, 35, 700, 300)
    'Heavy'

    Explanation:
    None of the dimensions of the box is greater or equal to 104.
    Its volume = 24500000 <= 109. So it cannot be categorized as "Bulky".
    However, mass >= 100, so the box is "Heavy".
    Since the box is not "Bulky" but "Heavy", we return "Heavy".

    >>> categorizeBox(200, 50, 800, 50)
    'Neither'

    Explanation:
    None of the dimensions of the box is greater or equal to 104.
    Its volume = 8 * 106 <= 109. So it cannot be categorized as "Bulky".
    Its mass is also less than 100, so it cannot be categorized as "Heavy" either.
    Since its neither of the two above categories, we return "Neither".
    """
    categories = []
    if length >= 10_000 or width >= 10_000 or height >= 10_000 or length * width * height >= 1e9:
        categories.append('Bulky')
    if mass >= 100:
        categories.append('Heavy')
    if len(categories) == 2:
        return 'Both'
    if not categories:
        return 'Neither'
    return categories[0]
