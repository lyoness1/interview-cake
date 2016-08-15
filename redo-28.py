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

    for idx, char in enumerate(sentence[pos+1:]):
        if char == "(":
            opens += 1
        elif char == ")":
            opens -= 1
        if opens == 0:
            return pos + idx + 1

    return "parenthesis are no balanced"


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"