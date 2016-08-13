"""
Write a function to check that a binary tree is a valid binary search tree.

Conditions:
1) Each node has at most 2 children (won't be issue w/ given structure)
2) left.value < self.value
3) right.value > self.value

    >>> a = BinaryTreeNode(5)
    >>> b = BinaryTreeNode(4)
    >>> c = BinaryTreeNode(6)
    >>> d = BinaryTreeNode(2)
    >>> e = BinaryTreeNode(1)
    >>> f = BinaryTreeNode(3)
    >>> a.insert_left(b)
    >>> a.insert_right(c)
    >>> b.insert_left(d)
    >>> d.insert_right(f)
    >>> d.insert_left(e)
    >>> a.is_binary_search_tree()
    True

    >>> a = BinaryTreeNode(5)
    >>> b = BinaryTreeNode(4)
    >>> c = BinaryTreeNode(6)
    >>> d = BinaryTreeNode(2)
    >>> e = BinaryTreeNode(1)
    >>> a.insert_left(b)
    >>> a.insert_right(c)
    >>> b.insert_left(d)
    >>> b.insert_right(e)
    >>> a.is_binary_search_tree()
    False

    >>> a = BinaryTreeNode(50)
    >>> b = BinaryTreeNode(30)
    >>> c = BinaryTreeNode(80)
    >>> a.insert_left(b)
    >>> a.insert_right(c)
    >>> d = BinaryTreeNode(20)
    >>> e = BinaryTreeNode(60)
    >>> b.insert_left(d)
    >>> b.insert_right(e)
    >>> a.is_binary_search_tree()
    False

"""

class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, node):
        self.left = node

    def insert_right(self, node):
        self.right = node

    def is_binary_search_tree(self):

        stack = [(self, -float('inf'), float('inf'))]

        while stack:

            node, low_bound, up_bound = stack.pop()

            if (node.value < low_bound) or (node.value > up_bound):
                return False

            # go left (current value becomes upper bound)
            if node.left:
                stack.append((node.left, low_bound, node.value))

            # go right (current value becomes lower bound)
            if node.right: 
                stack.append((node.right, node.value, up_bound))

        return True







if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"

