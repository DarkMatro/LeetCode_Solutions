from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head: Optional[ListNode]) -> bool:
    """
    ID: 0234
    Tags:   Linked List, Two Pointers, Stack, Recursion
    Time:   O(N)
    Memory: O(N)

    Parameters
    ----------
    head : Optional[ListNode]

    Returns
    -------
    out : bool
    """
    a = []
    while head:
        a.append(head.val)
        head = head.next
    return a == a[::-1]

