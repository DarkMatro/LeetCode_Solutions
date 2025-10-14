def simplifyPath(path: str) -> str:
    """
    ID: 71
    Tags:   String, Stack
    Time:   O(N)
    Memory: O(N)

    Task
    ----------
    You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to
    transform this absolute path into its simplified canonical path.

    The rules of a Unix-style file system are as follows:

    A single period '.' represents the current directory.
    A double period '..' represents the previous/parent directory.
    Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
    Any sequence of periods that does not match the rules above should be treated as a valid directory or file name.
    For example, '...' and '....' are valid directory or file names.
    The simplified canonical path should follow these rules:

    The path must start with a single slash '/'.
    Directories within the path must be separated by exactly one slash '/'.
    The path must not end with a slash '/', unless it is the root directory.
    The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
    Return the simplified canonical path.

    Parameters
    ----------
    path: str

    Returns
    -------
    out : str

    Examples
    --------
    >>> simplifyPath("/home/")
    '/home'

    Explanation: The trailing slash should be removed.

     >>> simplifyPath("/home//foo/")
    '/home/foo'

    Explanation: Multiple consecutive slashes are replaced by a single one.

     >>> simplifyPath("/home/user/Documents/../Pictures")
    '/home/user/Pictures'

    Explanation: A double period ".." refers to the directory up a level (the parent directory).

     >>> simplifyPath("/../")
    '/'

    Explanation: Going one level up from the root directory is not possible.

     >>> simplifyPath("/.../a/../b/c/../d/./")
    '/.../b/d'

    Explanation: "..." is a valid name for a directory in this problem.
    """
    stack = []
    for x in path.split('/'):
        if x == '..':
            if len(stack) >= 1:
                stack.pop()
        elif x == '' or x == '.':
            continue
        else:
            stack.append(x)
    ans = '/'
    for i, x in enumerate(stack):
        ans += x + '/' if i < len(stack) - 1 else x
    return ans
