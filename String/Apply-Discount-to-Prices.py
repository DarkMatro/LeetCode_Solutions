def discountPrices(sentence: str, discount: int) -> str:
    """
    ID: 2288
    Tags:   String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    A sentence is a string of single-space separated words where each word can contain digits,
    lowercase letters, and the dollar sign '$'. A word represents a price if it is a sequence of
    digits preceded by a dollar sign.

    For example, "$100", "$23", and "$6" represent prices while "100", "$", and "$1e5" do not.
    You are given a string sentence representing a sentence and an integer discount. For each word
    representing a price, apply a discount of discount% on the price and update the word in the
    sentence. All updated prices should be represented with exactly two decimal places.

    Return a string representing the modified sentence.

    Note that all prices will contain at most 10 digits.

    Parameters
    ----------
    sentence: str

    discount: int

    Returns
    -------
    out : str

    Examples
    --------
    >>> discountPrices('there are $1 $2 and 5$ candies in the shop', 50)
    'there are $0.50 $1.00 and 5$ candies in the shop'

    Explanation: The words which represent prices are "$1" and "$2".
    - A 50% discount on "$1" yields "$0.50", so "$1" is replaced by "$0.50".
    - A 50% discount on "$2" yields "$1". Since we need to have exactly 2 decimal places after a
    price, we replace "$2" with "$1.00".

    >>> discountPrices('1 2 $3 4 $5 $6 7 8$ $9 $10$', 100)
    '1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$'

    Explanation: Applying a 100% discount on any price will result in 0.
    The words representing prices are "$3", "$5", "$6", and "$9".
    Each of them is replaced by "$0.00".
    """
    ans = []
    for x in sentence.split(' '):
        if x[0] == '$' and x[1:].isdigit():
            d = float(x[1:])
            d -= d * discount / 100
            x = f'${d:.2f}'
        ans.append(x)
    x  =5
    if x > 255 or x < 0:
        print()
    return ' '.join(ans)
