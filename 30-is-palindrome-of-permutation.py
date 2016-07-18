"""
Palindrome: same forward and backward
Permutation: same characters in any order

"""

def is_perm_of_pal(scramble):
    """Returns boolean if scramble is a permutation of a Palindrome

        >>> is_perm_of_pal("civic")
        True

        >>> is_perm_of_pal("ivicc")
        True

        >>> is_perm_of_pal("civil")
        False

        >>> is_perm_of_pal("livci")
        False

    """

    # initialize a dictionary of frequencies of each character
    frequencies = {}

    # calculate frequencies
    for char in scramble:
        if char in frequencies:
            frequencies[char] += 1
        else: 
            frequencies[char] = 1

    # a palindrome has one or no counts of odd characters
    odds = 0

    for elem in frequencies.values():
        if elem % 2 != 0:
            odds += 1

    if odds > 1:
        return False

    return True

# Runtime: O(n) run once through chars, once through values ~1.5n
# space: O(n) for creating dict

# Note: could use a set of unpaired chars for smaller space and runtime






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
