"""
Reverse an *immutable* string in place

"""

def reverse_string(string):
    """Reverse a string 'in place'

        >>> reverse_string("Hello, how are you?")
        '?uoy era woh ,olleH'

    """

    chars = []
    for char in string:
        chars.append(char)

    # the .reverse() method, while in place, is probably not in the spirit of 
    # this problem... 
    chars.reverse()

    return "".join(chars)



def manual_reverse(string):
    """Reverse a string 'in place'

        >>> manual_reverse("Hello, how are you?")
        '?uoy era woh ,olleH'

    """

    chars = list(string)

    # reverse in place, manually, using list slicing to insert
    for i in range(len(chars)):
        char = chars.pop()
        chars[i:i] = char

    return "".join(chars)







if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"