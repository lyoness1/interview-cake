"""
Write a function to find the 2nd largest element in a bianary search tree

    >>> a = BinaryTreeNode(50)
    >>> b = BinaryTreeNode(30)
    >>> c = BinaryTreeNode(70)
    >>> a.insert_left(b)
    >>> a.insert_right(c)
    >>> d = BinaryTreeNode(60)
    >>> e = BinaryTreeNode(80)
    >>> c.insert_left(d)
    >>> c.insert_right(e)
    >>> a.get_second_largest()
    70

    >>> a = BinaryTreeNode(50)
    >>> b = BinaryTreeNode(30)
    >>> c = BinaryTreeNode(70)
    >>> a.insert_left(b)
    >>> a.insert_right(c)
    >>> d = BinaryTreeNode(60)
    >>> c.insert_left(d)
    >>> e = BinaryTreeNode(55)
    >>> f = BinaryTreeNode(65)
    >>> d.insert_right(f)
    >>> d.insert_left(e)
    >>> a.get_second_largest()
    65

"""

class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None
        self.parent = None

    def insert_left(self, node):
        self.left = node
        node.parent = self

    def insert_right(self, node):
        self.right = node
        node.parent = self

    def get_second_largest(self):
        """Returns the second largest node in tree if called on root"""

        # fail fast: not enough nodes
        if not self.left and not self.right:
            return "There must be at least two elements in tree!"

        def find_largest(self):
            """Returns the largest node in the tree (or subtree)"""

            # initialize largest as root/self
            largest = self

            # go as far right as possible
            while largest:
                if not largest.right:
                    return largest
                largest = largest.right

        # first find the largest node
        largest = find_largest(self)

        # two cases:
        # case 1: largest is a leaf
        if not largest.left:
            second_largest = largest.parent
            return second_largest.value

        # case 2: largest has a left branch
        else: 
            second_largest = largest.left

            # the second largest in the original tree will be the largest in the 
            # subtree of the largest node
            second_largest = find_largest(second_largest)
            return second_largest.value


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
