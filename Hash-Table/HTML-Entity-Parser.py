def entityParser(text: str) -> str:
    """
    ID: 1410
    Tags:   Hash Table, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    HTML entity parser is the parser that takes HTML code as input and replace all the entities of
    the special characters by the characters itself.

    The special characters and their entities for HTML are:

    Quotation Mark: the entity is &quot; and symbol character is ".
    Single Quote Mark: the entity is &apos; and symbol character is '.
    Ampersand: the entity is &amp; and symbol character is &.
    Greater Than Sign: the entity is &gt; and symbol character is >.
    Less Than Sign: the entity is &lt; and symbol character is <.
    Slash: the entity is &frasl; and symbol character is /.
    Given the input text string to the HTML parser, you have to implement the entity parser.

    Return the text after replacing the entities by the special characters.

    Parameters
    ----------
    text: str

    Returns
    -------
    out : str

    Examples
    --------
    >>> entityParser("&amp; is an HTML entity but &ambassador; is not.")
    '& is an HTML entity but &ambassador; is not.'

    Explanation: The parser will replace the &amp; entity by &

    >>> entityParser("and I quote: &quot;...&quot;")
    'and I quote: \"...\"'
    """
    d = {'&quot;': '\"', '&apos;': '\'', '&gt;': '>', '&lt;': '<', '&frasl;': '/', '&amp;': '&'}
    for k, v in d.items():
        text = text.replace(k, v)
    return text
