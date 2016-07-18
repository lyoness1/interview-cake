"""
Returns a boolean to determine if SLL contains a cycle

"""

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, node):
        self.head = node

# O(n) runtime, O(n) space
def contains_cycle(head):
    """Returns true if sll contains cycle"""

    seen = set()
    current_node = head

    while current_node:
        if current_node in seen:
            return True
        else:
            seen.add(current_node)
            current_node = current_node.next

    return False


# O(n) runtime, O(1) space
def contains_cycle_better(head):
    """Returns true if sll contains cycle"""

    fast_location = head
    slow_location = head

    while fast_location.next:
        # fast moves forward two, slow moves forward one
        fast_location = fast_location.next.next
        slow_location = slow_location.next

        # if fast meets slow, slow has been "lapped" in the cycle
        if fast_location == slow_location:
            return True

    # if fast meets None, the list ends and no cycle exists
    return False









