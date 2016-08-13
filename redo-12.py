# 12: How Quickly Can you Find a Number in a Sorted List?
# Runtime: O(lg(n)) binary search
# Space: O(1)
def find_target(target, arr):
    """Returns number of guesses for target

        >>> find_target(8, [x for x in range(101)])
        7

    """

    floor = 0
    ceiling = len(arr)
    steps = 0

    while floor < ceiling:

        # guess middle of range
        guess_idx = floor + (ceiling - floor) / 2
        guess = arr[guess_idx]

        # increment steps
        steps += 1

        # assess guess against target
        if guess == target:
            return steps

        # reassign range indexes
        elif guess < target:
            floor = guess_idx

        else:
            ceiling = guess_idx

    return False


# 13: Find Rotation Point
# Runtime: O(lg(n))
# Space: O(1)
# Edge cases: already sorted
def find_rotation(arr):
    """Returns the index of the rotation point

        >>> find_rotation(['play', 'xebra', 'bat', 'cat', 'dog'])
        2

        >>> find_rotation(['ptolemaic','retrograde','supplant','undulate','xenoepist','asymptote','babka','banoffee','engender','karpatka','othellolagkage'])
        5

    """

    floor = 0
    ceiling = len(arr)-1

    # edge case: already sorted
    if arr[ceiling] > arr[floor]:
        return floor

    # check middle
    while ceiling - floor > 1:

        guess_idx = floor + (ceiling - floor) / 2

        # option 1: rotation is before guess
        if arr[guess_idx] < arr[floor]:
            ceiling = guess_idx

        # option 1: rotation is after guess
        else: 
            floor = guess_idx

    # when floor and ceiling are one apart, ceiling will be rotation
    return ceiling











if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"