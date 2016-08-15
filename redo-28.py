# 28: Find matching closing parenthesis
# Runtime: O(n)
# Space: O(1)
# Edge cases: 

def find_closing(sentence, pos):
    """Returns the location of a closing parenthesis, given and opening one

    >>> find_closing("Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.", 10)
    79

    """

    opens = 1

    # note: using slice could create space O(n), better to just increment pos
    for idx, char in enumerate(sentence[pos+1:]):
        if char == "(":
            opens += 1
        elif char == ")":
            opens -= 1
        if opens == 0:
            return pos + idx + 1

    return "parenthesis are no balanced"


# 29: Parse braces
# Runtime: O(n)
# Space: O(m) where m is number of openers
# Edge cases: 
def parse_braces(sentence):
    """Returns boolean for whether braces are properly closed

    >>> parse_braces("{ [ ] ( ) }")
    True

    >>> parse_braces("{ [ ( ] ) }")
    False

    >>> parse_braces("{ [ }")
    False

    """

    stack = []
    openers = ["(", "[", "{"]

    for char in sentence:
        if char in openers:
            stack.append(char)
        if char == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                return False
        if char == "]":
            if stack[-1] == "[":
                stack.pop()
            else: 
                return False
        if char == "}":
            if stack[-1] == "{":
                stack.pop()
            else: 
                return False

    if not stack:
        return True
    else:
        return False











if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"