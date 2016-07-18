"""
Return the kth to last node in a SLL

    >>> a = LinkedListNode("Angel Food")
    >>> b = LinkedListNode("Bundt")
    >>> c = LinkedListNode("Cheese")
    >>> d = LinkedListNode("Devil's Food")
    >>> e = LinkedListNode("Eccles")

    >>> a.next = b
    >>> b.next = c
    >>> c.next = d
    >>> d.next = e

    >>> return_kth_to_last(2, a)
    "Devil's Food"

"""

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None


# Runtime: O(n)
# Space: O(1)
def return_kth_to_last(k, head):
    """Returns the node k elements from the end of lst with head"""

    curr = head

    # go through list to make sure it's at least k long
    for i in range(k):
        if curr.next:
            curr = curr.next
        else:
            raise Exception("List isn't long enough")

    # initialize kth to last at head
    kth_to_last = head

    # continue through list, updating k'th to last each step
    while curr:
        kth_to_last = kth_to_last.next
        curr = curr.next

    return kth_to_last.value






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"

