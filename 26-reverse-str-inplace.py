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



def IC_answer(string):

    str_list = list(string)

    left_pointer = 0
    right_pointer = len(str_list) - 1

    while left_pointer < right_pointer:

        str_list[left_pointer], str_list[right_pointer] = \
            str_list[right_pointer], str_list[left_pointer]

        left_pointer += 1
        right_pointer -= 1

    return "".join(str_list)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"