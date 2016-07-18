"""
Reverse a LL in place

"""

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None


def reverse_ll_inplace(head):
    """Rerverses a linked list in place"""

    prev = head
    if head.next:
        curr = head.next
    else:
        raise Exception("List only has one node")
    head.next = None

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