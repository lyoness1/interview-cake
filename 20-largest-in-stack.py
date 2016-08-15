"""Write a class to get the second largest element in a stack"""
# Option 1: loop through items and find max (O(n) cost per call)
# Option 2: write a new push method, tracking largest attribute (O(1) cost)

# given this stack class: 
class Stack:

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):

        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items: return None

        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items: return None
        return self.items[len(self.items)-1]

# Use your Stack class to implement a new class MaxStack with a function 
# get_max() that returns the largest element in the stack. get_max() should not 
# remove the item.

# Your stacks will contain only integers.

class MaxStack(Stack):

    # initialize MaxStack as a subclass of Stack, but add 'largest' attribute
    def __init__(self):
        super(MaxStack, self).__init__()
        self.largest = None

    # re-make the push method to track largest upon each addition
    # constant runtime if each addition is a max
    def push(self, item):
        self.items.append(item)
        if item > self.largest:
            self.old_max = self.largest
            self.largest = item

    # re-make pop method to find new largest if current largest is popped
    # O(n) runtime if each remove is a max, O(1) if we track 'old_max'
    def pop(self):
        if not self.items:
            return None

        item = self.items.pop()

        if item == self.largest:
            self.largest = self.old_max

        return item


    def get_max(self):
        """returns a reference to the largest item in stack"""
        return self.largest


# Interview cake's answer
class MaxStack2:
    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()

    def push(self, item):
        self.stack.push(item)
        if item >= self.max_stack.peek():
            self.max_stack.push(item)

    def pop(self):
        item = self.stack.pop()
        if item == self.max_stack.peek():
            self.max_stack.pop()
        return item

    def get_max(self):
        return self.max_stack.peek()




