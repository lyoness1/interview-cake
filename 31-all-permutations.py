"""
Write a recursive function for generating all permutations of an input string. 
Return them as a set.

To start, assume every character in the input string is unique.

"""


def generate_permutations(phrase):
    """Returns all permutations of an input string using recursion

        >>> generate_permutations('bath')
        set(['abth', 'hbta', 'bath', 'bhat', 'tbha', 'ahtb', 'atbh', 'hatb', 'thba', 'btha', 'htab', 'abht', 'ahbt', 'tbah', 'bhta', 'baht', 'habt', 'thab', 'athb', 'btah', 'tabh', 'htba', 'tahb', 'hbat'])

    """
    
    # base case: one letter left
    if len(phrase) <= 1:
        return set([phrase])

    # split the phrase into all but the last character, and the last character
    all_except_last_char = phrase[:-1]
    last_char = phrase[-1]

    # calculate permutations of smaller subproblems
    perms_of_smaller_phrase = generate_permutations(all_except_last_char)

    # initalize a set to store outputs
    permutations = set()

    # add the removed character to each possible position of the smaller perms
    for perm in perms_of_smaller_phrase:
        for i in range(len(phrase)):
            permutation = perm[:i] + last_char + perm[i:]
            permutations.add(permutation)
        
    return permutations



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"