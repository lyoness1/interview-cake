# 23: Find Cycle in SLL


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

# Runtime: O(n)
# Space: O(n)
# Edge cases:
def find_cycle(head):
    """Returns a boolean indicating a cycle"""

    seen = set()

    curr = head

    while curr.next:
        if curr in seen:
            return True
        else:
            seen.add(curr)
            curr = curr.next

    return False

# Runtime: O(n)
# Space: O(1)
# Edge cases:
def find_cycle_better(head):
    """Returns a boolean to indicate cycle"""

    runner1 = head
    runner2 = head

    while runner1.next and runner2.next:
        runner1 = runner1.next.next
        runner2 = runner2.next
        if runner1 == runner2:
            return True

    return False