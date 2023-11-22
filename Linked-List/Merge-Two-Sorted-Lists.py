from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    ID: 0021
    Tags:   Linked list, Recursion
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two
    lists.

    Return the head of the merged linked list.

    Parameters
    ----------
    list1 : Optional[ListNode]
    list2 : Optional[ListNode]

    Returns
    -------
    out : Optional[ListNode]
    """
    if not list1 and not list2:
        return list1
    if not list1:
        return list2
    if not list2:
        return list1
    seek, target = (list1, list2) if list1.val < list2.val else (list2, list1)
    head = seek
    while seek and target:
        while seek.next and seek.next.val < target.val:
            seek = seek.next
        seek.next, target = target, seek.next
        seek = seek.next
    return head
