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

# Solution 1:
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
        """Returns True if tree is superbalanced"""

        # initialize dictionary to store depths of leaves
        leaf_depths = {}
        # initalize starting depth of root node
        depth = 0

        # use recursion to make sure of callstack to keep track of depth
        def is_super_recurser(self, leaf_depths, depth):
            """Helper fn to keep track of depth"""

            # base case: found leaf
            if not self.left and not self.right:
                # if depth already has a node, add this one
                if depth in leaf_depths:
                    leaf_depths[depth].append(self)
                # if dict[current_depth] is empty, initialize a list with self
                else:
                    leaf_depths[depth] = [self]
                # return the dictionary
                return leaf_depths

            # else, increment depth, and check down one level for more leaves
            depth += 1
            if self.left:
                is_super_recurser(self.left, leaf_depths, depth)
            if self.right:
                is_super_recurser(self.right, leaf_depths, depth)

            return leaf_depths

        # call recursive helper fn
        is_super_recurser(self, leaf_depths, depth)

        # check depth of all leaves of tree
        # if there are more than two depths recorded, the max difference > 1
        if len(leaf_depths.keys()) > 2:
            return False

        # if only one leaf depth, root is only node in tree, which is superbal.
        elif len(leaf_depths.keys()) == 1:
            return True

        # else, check the difference
        if abs(leaf_depths.keys()[0] - leaf_depths.keys()[1]) <= 1:
            return True

        return False



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
