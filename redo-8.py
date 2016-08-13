# 8: Superbalanced
"""
A tree is "superbalanced" if the difference between the depths of any two 
leaf nodes is no greater than one.

    >>> a = BinaryTreeNode('a')
    >>> b = BinaryTreeNode('b')
    >>> c = BinaryTreeNode('c')
    >>> d = BinaryTreeNode('d')
    >>> e = BinaryTreeNode('e')
    >>> a.insert_left(b)
    >>> b.insert_left(c)
    >>> c.insert_left(d)
    >>> c.insert_right(e)
    >>> a.is_super()
    True

    >>> a = BinaryTreeNode('a')
    >>> b = BinaryTreeNode('b')
    >>> c = BinaryTreeNode('c')
    >>> d = BinaryTreeNode('d')
    >>> e = BinaryTreeNode('e')
    >>> a.insert_left(b)
    >>> a.insert_right(c)
    >>> b.insert_left(d)
    >>> d.insert_left(e)
    >>> a.is_super()
    False


"""

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, node):
        self.left = node

    def insert_right(self, node):
        self.right = node

    def is_super(self):
        
        min_depth = None
        max_depth = 0

        # iterative depth-first traversal
        stack = [(self, 0)]
        while stack: 

            node, curr_depth = stack.pop()

            # found leaf, assess depth
            if not node.right and not node.left:
                # min depth has to be established before comparison
                if not min_depth:
                    min_depth = curr_depth
                else:
                    min_depth = min(min_depth, curr_depth)
                # track max depth
                max_depth = max(max_depth, curr_depth)

            # not leaf, continue traversal
            if node.right: 
                stack.append((node.right, curr_depth + 1))
            if node.left:
                stack.append((node.left, curr_depth + 1))

        if (max_depth - min_depth) > 1:
            return False

        return True
        















if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"