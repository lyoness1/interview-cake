# 24: Reverse LL in place
# Runtime: O(n)
# Space: O)1
# Edge cases: empty list, one node

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

def reverse_ll(head):
    """Reverses LL in place, returns new head"""

    if not head:
        return "List is empty"

    if not head.next:
        return head

    prev = head
    curr = head.next
    
    # update pointer for old head to None as new tail
    prev.next = None

    while curr.next:
        # grab next node
        nxt = curr.next
        # reset curr's pointer backward
        curr.next = prev
        # update prev
        prev = curr
        # update curr
        curr = nxt

    # when curr.next == None, curr will be new head
    return curr
