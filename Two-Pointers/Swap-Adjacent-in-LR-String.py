def canTransform(start: str, result: str) -> bool:
    """
    ID: 777
    Tags: Two Pointers, String
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one
    occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and
    the ending string result, return True if and only if there exists a sequence of moves to transform start to result.

    Parameters
    ----------
    start: str

    result: str

    Returns
    -------
    out : bool

    Examples
    --------
    >>> canTransform("RXXLRXRXL", "XRLXXRRLX")
    True

    Explanation: We can transform start to result following these steps:
    RXXLRXRXL ->
    XRXLRXRXL ->
    XRLXRXRXL ->
    XRLXXRRXL ->
    XRLXXRRLX

    >>> canTransform("X", "L")
    False
    """
    if len(start) != len(result):
        return False

    n = len(start)

    # убираем 'X', сравниваем порядок L и R
    s_no_x = [c for c in start if c != 'X']
    r_no_x = [c for c in result if c != 'X']
    if s_no_x != r_no_x:
        return False

    # проверяем позиции L и R
    i = j = 0
    while i < n and j < n:
        # пропускаем X
        while i < n and start[i] == 'X':
            i += 1
        while j < n and result[j] == 'X':
            j += 1
        if i == n or j == n:
            break

        if start[i] != result[j]:
            return False

        if start[i] == 'L' and j > i:
            return False  # L не может двигаться вправо
        if start[i] == 'R' and j < i:
            return False  # R не может двигаться влево

        i += 1
        j += 1

    return True
