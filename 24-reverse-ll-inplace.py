"""
Reverse a LL in place

"""

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None


def reverse_ll_inplace(head):
    """Rerverses a linked list in place"""

    # catches edge case of list being empty
    if not head:
        return "List is empty"

    # catches edge case of list having one element
    if not head.next:
        return head

    prev = None
    curr = head

    while curr:
        # get next node
        next = curr.next
        # reassign current pointer back to prev
        curr.next = prev
        # update prev to current (moving forward)
        prev = curr
        # update current to next (moving forward)
        curr = next

    # while loop breaks when next is None. So what's the new head? Prev.
    return prev