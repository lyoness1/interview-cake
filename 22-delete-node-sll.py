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
    # copies the next node to current location, leaving the old next node del'ed
    if node.next:
        node.value = node.next.value
        node.next = node.next.next
    else:
        raise Exception("Can't delete last node with this function")




# Problems:
# Doesn't work for last node in list
# Any external references to node to be deleted will now raise errors
# Any external references to original next node will be dangling, 
# and leave the node unable to be garbage collected




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"