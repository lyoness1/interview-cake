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

    while floor+1 < ceiling:

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






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"