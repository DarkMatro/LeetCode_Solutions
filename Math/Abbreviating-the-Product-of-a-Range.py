import math

def abbreviateProduct(left: int, right: int) -> str:
    """
    ID: 2117
    Tags:   Math
    Time:   O(NlogN)
    Memory: O(1)

    Task
    ----------
    You are given two positive integers left and right with left <= right. Calculate the product oF
    all integers in the inclusive range [left, right].

    Since the product may be very large, you will abbreviate it following these steps:

    Count all trailing zeros in the product and remove them. Let us denote this count as C.
    For example, there are 3 trailing zeros in 1000, and there are 0 trailing zeros in 546.
    Denote the remaining number of digits in the product as d. If d > 10, then express the product
    as <pre>...<suf> where <pre> denotes the first 5 digits of the product, and <suf> denotes the
    last 5 digits of the product after removing all trailing zeros. If d <= 10, we keep it
    unchanged.
    For example, we express 1234567654321 as 12345...54321, but 1234567 is represented as 1234567.
    Finally, represent the product as a string "<pre>...<suf>eC".
    For example, 12345678987600000 will be represented as "12345...89876e5".
    Return a string denoting the abbreviated product of all integers in the inclusive range [left,
    right].

    Parameters
    ----------
    left: int

    right: int

    Returns
    -------
    out : str

    Examples
    --------
    >>> abbreviateProduct(1, 4)
    '24e0'

    Explanation: The product is 1 × 2 × 3 × 4 = 24.
    There are no trailing zeros, so 24 remains the same. The abbreviation will end with "e0".
    Since the number of digits is 2, which is less than 10, we do not have to abbreviate it further.
    Thus, the final representation is "24e0".

    >>> abbreviateProduct(2, 11)
    '399168e2'

    Explanation: The product is 39916800.
    There are 2 trailing zeros, which we remove to get 399168. The abbreviation will end with "e2".
    The number of digits after removing the trailing zeros is 6, so we do not abbreviate it further.
    Hence, the abbreviated product is "399168e2"..

    >>> abbreviateProduct(371, 375)
    '7219856259e3'

    Explanation: The product is 7219856259000.
    """
    last = 1
    modulo = 10 ** 5

    twosCount = 0
    fivesCount = 0

    sumLog10 = 0
    maxBufferValue = 10 ** 1200
    bufferProduct = 1

    for x in range(left, right + 1):
        bufferProduct *= x

        if bufferProduct > maxBufferValue:
            sumLog10 += math.log10(bufferProduct)
            bufferProduct = 1

        while x % 2 == 0:
            twosCount += 1
            x //= 2

        while x % 5 == 0:
            fivesCount += 1
            x //= 5

        last = (last * x) % modulo

    sumLog10 += math.log10(bufferProduct)
    zerosCount = min(twosCount, fivesCount)

    if sumLog10 < 10 + zerosCount:
        productString = str(bufferProduct)
        return productString[:len(productString) - zerosCount] + 'e' + str(zerosCount)

    twosCount -= zerosCount
    fivesCount -= zerosCount

    last = (last * pow(2, twosCount, modulo)) % modulo
    last = (last * pow(5, fivesCount, modulo)) % modulo

    first = int(pow(10, sumLog10 % 1 + 4.0))

    return str(first) + '...' + str(last).zfill(5) + 'e' + str(zerosCount)
