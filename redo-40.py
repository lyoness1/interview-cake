# 40: Find duplicate ints 1...n, len(arr) = n + 1
# Runtime: O(nlg(n))
# Space: O(1)
# Edge cases: 
def find_dupe(arr):
    """Returns the duplicate in arr

        >>> find_dupe([1, 2, 3, 4, 5, 6, 6, 7, 8, 9])
        [6]

        >>> find_dupe([1, 2, 3, 3, 5, 6, 7, 7, 7, 9])
        [3, 7]

    """
    # output list is O(1) space
    output = []

    # this solution only works if list is sorted, but nlg(n) < n^2
    # done in place, this destroys the input list
    # done with new list adds O(n) space but preserves input list
    arr.sort()

    # use index to pass over list once O(n) runtime
    i = 0
    # go to len - 2 so i doesn't go out of range
    while i < len(arr) - 2:
        # if find duplicate, add to list and increment until new int
        if arr[i + 1] == arr[i]:
            output.append(arr[i])
            while arr[i + 1] == arr[i]:
                i += 1
        # increment through list
        i += 1

    return output
        


def find_dupe_mathy(arr):
    """Returns the duplicate in arr

        >>> find_dupe_mathy([1, 2, 3, 4, 5, 6, 6, 7, 8, 9])
        6

        >>> find_dupe_mathy([1, 2, 3, 3, 4, 5, 6, 7, 8, 9])
        3

    """
    # one half has n items, the other n + 1 (b/c of duplicate)
    floor = 1
    ceiling = len(arr) - 1

    while floor < ceiling:
        # split list into two halves
        mid_idx = floor + ((ceiling - floor) / 2)
        lower_floor, lower_ceiling = floor, mid_idx
        upper_floor, upper_ceiling = mid_idx+1, ceiling

        # count expected and actual items in lower half
        actual_count = 0
        for item in arr:
            if item <= lower_ceiling and item >= lower_floor:
                actual_count += 1

        expected_count = lower_ceiling - lower_floor + 1

        # duplicate is in lower half
        if actual_count > expected_count:
            floor, ceiling = lower_floor, lower_ceiling
        # duplicate is in upper half
        else: 
            floor, ceiling = upper_floor, upper_ceiling

    # when floor and ceiling converge, floor will be duplicate
    return floor

# 41: Find Dupe Beast Mode
# Runtime: O(n)
# Space: O(1)
# Edge cases:
def find_dupe_beast(arr):
    """Returns the duplicate in arr

        >>> find_dupe_beast([1, 2, 3, 4, 5, 6, 6, 7, 8, 9])
        6

        >>> find_dupe_beast([1, 2, 3, 3, 4, 5, 6, 7, 8, 9])
        3

    """

    # think of list as ll with index + 1 = position. 
    # repeat will have two incoming pointers
    # start at end of list, as it will never have two incoming pointers
    start = arr[-1]
    second = start
    # increment faster runner one so while loop will be entered
    start = arr[start]

    # get into a cycle
    while start != second:
        start = arr[start-1]
        start = arr[start-1]
        second = arr[second]

    # find the length of the cycle by incrementing one runner until it loops
    start = arr[start-1]
    steps = 1
    while start != second:
        start = arr[start-1]
        steps += 1

    # start over, with second runner at same speed but length of cycle behind
    start = arr[-1]
    second = start

    for _ in xrange(steps):
        start = arr[start-1]

    # go around loop 













if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"