from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    ID: 0876
    Tags:   Linked list, Two Pointers
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given the head of a singly linked list, return the middle node of the linked list.

    If there are two middle nodes, return the second middle node.

    Parameters
    ----------
    head : Optional[ListNode]

    Returns
    -------
    out : Optional[ListNode]
    """
    mid = head
    end = head
    while end and end.next:
        mid = mid.next
        end = end.next.next
    return mid
