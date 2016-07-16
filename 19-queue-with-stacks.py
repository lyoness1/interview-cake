"""Implement a queue with two stacks. Have enqueue and dequeue"""

class Q:
    def __init__(self):
        stack1 = []
        stack2 = []

    def nq(self, item):
        stack1.append(item)

    def dq(self):
        # remove all but first item from stack 1
        while len(stack1) > 1:
            stack2.append(stack1.pop())

        # get item to dq
        item = stack1.pop()
        
        # put items back on stack 1
        while stack2:
            stack1.append(stack2.pop())

        return item


# better solution
class Que:

    def __init__(self):
        in_stack = []
        out_stack = []

    def enq(self, item):
        in_stack.append(item)

    def deq(self):

        # if there's a pile in the in_stack, dig to the bottom of it
        if stack1:
            while len(stack1) > 1:
                stack2.append(stack1.pop())

            return stack1.pop()

        # if stack1 is empty, then next item to return is top of stack 2
        else:
            return stack2.pop()

# Analysis:
# first solution is O(m^2) if m is the number of calls to nq or dq 
# and the length of the number of things in the stacks. 

# second solution is O(m)
# why? Items only move from in stack to out stack ONCE in their lifetime. 
# look at cost for each item, not for each call of the method. 
# each item will be put on in_stack, then moved to out_stack (or just dq'ed)
# then returned. It doesn't got back and forth. This is O(1) for each item. 
# so the total runtime is just the number of THINGS that get queued, where
# each thing has constant nq/dq runtime. Total THINGS = m, runtime: O(m)