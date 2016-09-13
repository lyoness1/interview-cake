# 21: Find Missing Drone
# Runtime: O(n)
# Space: O(n)
# Edge cases: 
def find_drone(arr):
    """Returns the ID that isn't repeated in arr

        >>> find_drone([1, 2, 4, 4, 3, 6, 6, 3, 1, 2, 7, 9, 7])
        9

    """

    checked_out = set()

    for item in arr:
        if item in checked_out:
            checked_out.remove(item)
        else:
            checked_out.add(item)

    return next(iter(checked_out))

# runtime: O(n)
# space: O(1)
def find_drone_xor(arr):
    """Returns the ID that isn't repeated in arr

        >>> find_drone_xor([1, 2, 4, 4, 3, 6, 6, 3, 1, 2, 7, 9, 7])
        9

    """

    tracker = 0

    for item in arr:
        # XOR will turn 0 bits to 1's the first time they are seen
        # it will turn 1 bits to 0's the second time they are seen
        # whether 1 or 0, the bit will remain unchanged if item == 0 at that bit
        tracker ^= item

    return tracker


# NOTE:
# 1 ^ 1 = 0 (changed)
# 1 ^ 0 = 1 (unchanged)
# 0 ^ 1 = 1 (changed)
# 0 ^ 0 = 0 (unchanged)








if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"