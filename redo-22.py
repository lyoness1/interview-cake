"""

Delete a node from a SLL given only a variable pointing to that node.
The input could, for example, be the variable b below:

    >>> a = LinkedListNode('A')
    >>> b = LinkedListNode('B')
    >>> c = LinkedListNode('C')

    >>> a.next = b
    >>> b.next = c

    >>> delete_node(b)


"""


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def delete_node(node):

    # grab node after node to delete
    next_node = node.next

    # reset node to delete's value to next node's value
    # update pointer
    if next_node:
        node.value = next_node.value
        node.next = next_node.next

    # can't delete last node
    else:
        raise Exception("can't delete last node this way")









if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
