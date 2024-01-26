from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getIntersectionNode(headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
    """
    ID: 0160
    Tags:   Hash Table, Linked List, Two Pointers
    Time:   O(m + n)
    Memory: O(1)

    Parameters
    ----------
    headA : Optional[ListNode]
    headB : Optional[ListNode]

    Returns
    -------
    out : Optional[ListNode]
    """
    cur_a = headA
    cur_b = headB

    while cur_a != cur_b:
        cur_a = headB if cur_a is None else cur_a.next
        cur_b = headA if cur_b is None else cur_b.next
    return cur_a

