def removeComments(source: list[str]) -> list[str]:
    """
    ID: 722
    Tags:   Array, String
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    Given a C++ program, remove comments from it. The program source is an array of strings source
    where source[i] is the ith line of the source code. This represents the result of splitting the
    original source code string by the newline character '\n'.

    In C++, there are two types of comments, line comments, and block comments.

    The string "//" denotes a line comment, which represents that it and the rest of the characters
    to the right of it in the same line should be ignored.
    The string "/*" denotes a block comment, which represents that all characters until the next
    (non-overlapping) occurrence of "*/" should be ignored. (Here, occurrences happen in reading
    order: line by line from left to right.) To be clear, the string "/*/" does not yet end the
    block comment, as the ending would be overlapping the beginning.
    The first effective comment takes precedence over others.

    For example, if the string "//" occurs in a block comment, it is ignored.
    Similarly, if the string "/*" occurs in a line or block comment, it is also ignored.
    If a certain line of code is empty after removing comments, you must not output that line: each
    string in the answer list will be non-empty.

    There will be no control characters, single quote, or double quote characters.

    For example, source = "string s = "/* Not a comment. */";" will not be a test case.
    Also, nothing else such as defines or macros will interfere with the comments.

    It is guaranteed that every open block comment will eventually be closed, so "/*" outside of a
    line or block comment always starts a new comment.

    Finally, implicit newline characters can be deleted by block comments. Please see the examples
    below for details.

    After removing the comments from the source code, return the source code in the same format.

    Parameters
    ----------
    source: list[str]

    Returns
    -------
    out : list[str]

    Examples
    --------
    >>> removeComments(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"])
    ['int main()', '{ ', '  ', 'int a, b, c;', 'a = b + c;', '}']

    Explanation: The line by line code is visualized as below:
    /*Test program */
    int main()
    {
      // variable declaration
    int a, b, c;
    /* This is a test
       multiline
       comment for
       testing */
    a = b + c;
    }
    The string /* denotes a block comment, including line 1 and lines 6-9. The string // denotes
        line 4 as comments.
    The line by line output code is visualized as below:
    int main()
    {

    int a, b, c;
    a = b + c;
    }
    Example

    >>> removeComments(["a/*comment", "line", "more_comment*/b"])
    ['ab']

    Explanation: The original source string is "a/*comment\nline\nmore_comment*/b", where we have
    bolded the newline characters.  After deletion, the implicit newline characters are deleted,
    leaving the string "ab", which when delimited by newline characters becomes ["ab"].
    """
    in_block_comment = False
    result = []
    new_line = []

    for line in source:
        i = 0
        if not in_block_comment:
            new_line = []

        while i < len(line):
            if not in_block_comment and i + 1 < len(line) and line[i:i + 2] == '/*':
                in_block_comment = True
                i += 1
            elif in_block_comment and i + 1 < len(line) and line[i:i + 2] == '*/':
                in_block_comment = False
                i += 1
            elif not in_block_comment and i + 1 < len(line) and line[i:i + 2] == '//':
                break  # Ignore the rest of the line
            elif not in_block_comment:
                new_line.append(line[i])
            i += 1

        if not in_block_comment and new_line:
            result.append("".join(new_line))

    return result
