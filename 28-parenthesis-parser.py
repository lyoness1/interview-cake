"""
I like parentheticals (a lot).
"Sometimes (when I nest them (my parentheticals) too much (like this 
(and this))) they get confusing."

Write a function that, given a sentence like the one above, along with the 
position of an opening parenthesis, finds the corresponding closing parenthesis.

Example: if the example string above is input with the number 10 (position of 
the first parenthesis), the output should be 79 (position of the last 
parenthesis).

"""

def find_closing_paren(sentence, pos):
    """Returns the location of a closing parenthesis, given and opening one

    >>> find_closing_paren("Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.", 10)
    79

    """
    paren_stack = []

    # iterate over chars
    for i in range(len(sentence)):

        # if open, add to stack, if closed pop off stack
        if sentence[i] == '(':
            paren_stack.append(i)
        elif sentence[i] == ')':
            open_pos = paren_stack.pop()
            if open_pos == pos:
                return i

# Runtime O(n)
# Space O(number of parenthesis)
# To do in O(1): just count open's and closed as int variables (length of stack)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"