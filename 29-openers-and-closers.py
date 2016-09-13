"""
Let's say:

'(', '{', '[' are called "openers."
')', '}', ']' are called "closers."
Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.

Examples:

"{ [ ] ( ) }" should return True
"{ [ ( ] ) }" should return False
"{ [ }" should return False

"""

def parse_braces(sentence):
    """Returns boolean for whether braces are properly closed

    >>> parse_braces("{ [ ] ( ) }")
    True

    >>> parse_braces("{ [ ( ] ) }")
    False

    >>> parse_braces("{ [ }")
    False

    """

    # identify braces
    openers = ['{', '[', '(']
    closers = ['}', ']', ')']

    # initialize a stack to store open braces
    stack = []

    # iterate through sentence
    for char in sentence: 

        # when an opener is met, add to stack
        if char in openers:
            stack.append(char)

        # if a closer is met, get it's index in closer list to validate that
        # the closer is a partner to the most recent opener. 
        # If there's a match, pop the opener off the stack
        # (could also use an opener to closer map/dictionary to track partners)
        elif char in closers:
            idx = closers.index(char)
            if stack[-1] == openers[idx]:
                stack.pop()
            # can't close a parenthesis until most recent open brace is closed
            else: 
                return False

    # an empty stack indicates all braces were closed in correct order
    if not stack:
        return True

    # an stack with any openers left means there weren't enough closers
    return False


def try_again(phrase):
    """Returns boolean for whether braces are properly closed

    >>> parse_braces("{ [ ] ( ) }")
    True

    >>> parse_braces("{ [ ( ] ) }")
    False

    >>> parse_braces("{ [ }")
    False

    """

    matches = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }

    openers = frozenset(matches.keys())
    closers = frozenset(matches.values())

    openers_stack = []

    for char in phrase: 

        # keep track of openers in stack
        if char in openers:
            openers_stack.append(char)

        # when a closer is found
        elif char in closers:
            # option 1: fails because there wasn't enough openers
            if not openers_stack:
                return False
            # option 2: fails if the most recent opener wasn't a match
            else:
                latest_opener = openers_stack.pop()
                if matches[latest_opener] != char:
                    return False

    # option 3: fails if too many openers, succeeds if all closed properly
    return openers_stack == []










if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
