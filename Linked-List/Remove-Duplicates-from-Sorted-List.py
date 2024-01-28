from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    ID: 0083
    Tags:   Linked List
    Time:   O(N)
    Memory: O(1)

    Parameters
    ----------
    head : Optional[ListNode]

    Returns
    -------
    out : Optional[ListNode]
    """
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head
