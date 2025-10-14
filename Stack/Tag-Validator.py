def isValid(code: str) -> bool:
    """
    ID: 591
    Tags:   String, Stack
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given a string representing a code snippet, implement a tag validator to parse the code and return whether it is
    valid.

    A code snippet is valid if all the following rules hold:

    The code must be wrapped in a valid closed tag. Otherwise, the code is invalid.
    A closed tag (not necessarily valid) has exactly the following format : <TAG_NAME>TAG_CONTENT</TAG_NAME>. Among
    them, <TAG_NAME> is the start tag, and </TAG_NAME> is the end tag. The TAG_NAME in start and end tags should be the
    same. A closed tag is valid if and only if the TAG_NAME and TAG_CONTENT are valid.
    A valid TAG_NAME only contain upper-case letters, and has length in range [1,9]. Otherwise, the TAG_NAME is invalid.
    A valid TAG_CONTENT may contain other valid closed tags, cdata and any characters (see note1) EXCEPT unmatched <,
    unmatched start and end tag, and unmatched or closed tags with invalid TAG_NAME. Otherwise, the TAG_CONTENT is
    invalid.
    A start tag is unmatched if no end tag exists with the same TAG_NAME, and vice versa. However, you also need to
    consider the issue of unbalanced when tags are nested.
    A < is unmatched if you cannot find a subsequent >. And when you find a < or </, all the subsequent characters until
    the next > should be parsed as TAG_NAME (not necessarily valid).
    The cdata has the following format : <![CDATA[CDATA_CONTENT]]>. The range of CDATA_CONTENT is defined as the
    characters between <![CDATA[ and the first subsequent ]]>.
    CDATA_CONTENT may contain any characters. The function of cdata is to forbid the validator to parse CDATA_CONTENT,
    so even it has some characters that can be parsed as tag (no matter valid or invalid), you should treat it as
    regular characters.

    Parameters
    ----------
    code: str

    Returns
    -------
    bool

    Examples
    --------
    >>> isValid("<DIV>This is the first line <![CDATA[<div>]]></DIV>")
    True

    Explanation:
    The code is wrapped in a closed tag : <DIV> and </DIV>.
    The TAG_NAME is valid, the TAG_CONTENT consists of some characters and cdata.
    Although CDATA_CONTENT has an unmatched start tag with invalid TAG_NAME, it should be considered as plain text, not parsed as a tag.
    So TAG_CONTENT is valid, and then the code is valid. Thus return true.

    >>> isValid("<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>")
    True

    Explanation:
    We first separate the code into : start_tag|tag_content|end_tag.
    start_tag -> "<DIV>"
    end_tag -> "</DIV>"
    tag_content could also be separated into : text1|cdata|text2.
    text1 -> ">>  ![cdata[]] "
    cdata -> "<![CDATA[<div>]>]]>", where the CDATA_CONTENT is "<div>]>"
    text2 -> "]]>>]"
    The reason why start_tag is NOT "<DIV>>>" is because of the rule 6.
    The reason why cdata is NOT "<![CDATA[<div>]>]]>]]>" is because of the rule 7.

    >>> isValid("<A>  <B> </A>   </B>")
    False

    Explanation: Unbalanced. If "<A>" is closed, then "<B>" must be unmatched, and vice versa.
    """
    stack = []
    i, n = 0, len(code)

    while i < n:
        if i > 0 and not stack:
            # Anything outside the outermost tag is invalid
            return False

        if code.startswith("<![CDATA[", i):
            # CDATA must be inside a valid tag
            if not stack:
                return False
            j = code.find("]]>", i)
            if j == -1:
                return False
            i = j + 3

        elif code.startswith("</", i):
            # End tag
            j = code.find(">", i)
            if j == -1:
                return False
            tag = code[i + 2:j]
            # Validate tag name strictly
            if not (1 <= len(tag) <= 9 and tag.isupper() and tag.isalpha()):
                return False
            if not stack or stack[-1] != tag:
                return False
            stack.pop()
            i = j + 1

        elif code.startswith("<", i):
            # Start tag
            j = code.find(">", i)
            if j == -1:
                return False
            tag = code[i + 1:j]
            # Invalid if it contains nested '<'
            if '<' in tag:
                return False
            # Strictly uppercase A–Z letters only
            if not (1 <= len(tag) <= 9 and tag.isupper() and tag.isalpha()):
                return False
            stack.append(tag)
            i = j + 1

        else:
            i += 1  # plain text inside tag

    return not stack
