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
    >>> a.is_binary_search_tree_improved()
    False

"""

# Solution 1: O(n) space and time - must check every node once
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
        """Determines if tree is proper binary search tree
        Problem: only checks against immediate parents, not all anscestors. 
        """

        # base case: leaf
        if not self.left and not self.right:
            return True

        # base case: values fail
        if self.left and self.left.value > self.value:
            return False
        if self.right and self.right.value < self.value:
            return False

        # progress recursively, returning True or False from call
        return self.left.is_binary_search_tree()
        return self.right.is_binary_search_tree()

    # Analysis: O(n) runtime for every node (worst case)
    # Space: O(n) if anscestors set gets full, O(lg(n)) if balanced
    # (depth of balanced tree is lg(n) compared to breadth of n). 
    def is_binary_search_tree_improved(self):
        """Keeps track of anscestors"""

        anscestors = set()

        def recurser(self, anscestors):
            """Helper recurser fn"""

            # base case: leaf
            if not self.left and not self.right:
                # remove self from anscestors list before going back up stack
                anscestors.remove(self.value)
                return True

            # base case: values fail against any anscestor
            # instead of using a set, space could be improved by using 
            # just an upper and lower bound variable of what's been seen. 
            if (self.left and anscestors) and (self.left.value >=
                                                    min(anscestors)):
                return False
            if (self.right and anscestors) and (self.right.value >=
                                                    max(anscestors)):
                return False

            # add self to anscestors set
            anscestors.add(self.value)

            # progress recursively, returning True or False from call
            return recurser(self.left, anscestors)
            return recurser(self.right, anscestors)

        return recurser(self, anscestors)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
