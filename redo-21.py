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
        tracker ^= item

    return tracker










if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"