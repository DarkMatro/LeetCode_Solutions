from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    ID: 0206
    Tags:   Linked List, Recursion
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given the head of a singly linked list, reverse the list, and return the reversed list.

    Parameters
    ----------
    head : Optional[ListNode]

    Returns
    -------
    out : Optional[ListNode]
    """
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

