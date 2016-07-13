"""
Given a sorted list, how quickly find item?
"""

# Solution: binary search

def find_item(item, arr):
    """Returns steps to find item in arr, False if not there

        >>> find_item(8, [x for x in range(101)])
        7

    """

    low_index = 0
    high_index = len(arr)-1  # for arr [0,1,2,3], len = 4, arr.index(3) = 3
    guess = None
    steps = 0

    while guess != item and low_index < high_index:

        # increment steps
        steps += 1
        
        # start at mid point
        guess_index = low_index + (high_index - low_index) / 2
        guess = arr[guess_index]

        if guess == item:
            return steps

        # reassign guessing parameters
        elif guess < item: 
            low_index = guess_index

        else:
            high_index = guess_index

    return False

# Runtime: O(lg(n))
# Space: O(1)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"