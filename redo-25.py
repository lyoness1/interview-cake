# 25: Kth to last node in sll
# Runtime: O(n)
# Space: O(1)
# Edge cases: 

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None


def kth_to_last(k, head):
    """Returns the kth to last node in sll

    >>> a = LinkedListNode("Angel Food")
    >>> b = LinkedListNode("Bundt")
    >>> c = LinkedListNode("Cheese")
    >>> d = LinkedListNode("Devil's Food")
    >>> e = LinkedListNode("Eccles")

    >>> a.next = b
    >>> b.next = c
    >>> c.next = d
    >>> d.next = e

    >>> kth_to_last(2, a)
    "Devil's Food"

    """

    # runner1 goes forward k nodes
    runner1 = head
    for i in xrange(k-1):
        runner1 = runner1.next

    # runner2 follows, tracking k nodes back
    runner2 = head
    while runner1.next:
        runner1 = runner1.next
        runner2 = runner2.next

    return runner2.value


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
