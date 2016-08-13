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
        self.right = None
        self.left = None

    def insert_left(self, node):
        self.left = node

    def insert_right(self, node):
        self.right = node

    def get_second_largest(self):

        # must have at least two nodes to have a second largest
        if not self.right and not self.left:
            return "No second largest node in tree"

        node = self

        # step 1: find largest node (furthest right)
        while node.right:
            parent = node
            node = node.right

        # option 1: 2nd largest is parent of largest, if largest == leaf
        if not node.left:
            return parent.value

        # option 2: 2nd largest is right most child of left child of largest
        else: 
            # step a: go left once
            node = node.left
            # step b: find largest node in left subtree
            while node.right:
                node = node.right
            return node.value







if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"