from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    """
    ID: 0141
    Tags:   Hash Table, Linked List, Two Pointers
    Time:   O(N)
    Memory: O(1)

    Task
    ----------
    Given head, the head of a linked list, determine if the linked list has a cycle in it.

    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
    following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is
    connected to. Note that pos is not passed as a parameter.

    Return true if there is a cycle in the linked list. Otherwise, return false.

    Parameters
    ----------
    head : Optional[ListNode]

    Returns
    -------
    out : bool
    """
    nodes = {}

    while head:
        if head.next not in nodes:
            nodes[head.next] = 1
        else:
            return True
        head = head.next

    return False
