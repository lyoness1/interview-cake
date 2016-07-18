"""
Write a recursive function for generating all permutations of an input string. 
Return them as a set.
Don't worry about time or space complexity—if we wanted efficiency we'd write 
an iterative version. 

To start, assume every character in the input string is unique.

Your function can have loops—it just needs to also be recursive.

"""

def generate_permutations(string):
    """Returns all permutations of an input string using recursion

        >>> generate_permutations('bath')
        


    """

    chars = string.split()
    print chars






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"