"""
List of ints 1...n
len(list) = n+1
at least one int appears 2+ times
can be several dupes appearing >2 times
"""

# runtime O(n)
# space: O(n) for additional seen and dupes sets
def find_dupes(arr):
    """Returns any integer that appears more than once

        >>> find_dupes([1, 2, 3, 4, 4, 4, 5, 6, 6, 7, 8, 9])
        set([4, 6])

    """

    seen = set()
    dupes = set()

    for item in arr:
        if item in seen:
            dupes.add(item)
        else:
            seen.add(item)

    return dupes


# space: O(1), but original input will be altered 
# runtime O(nlg(n))
def find_dupes_again(arr):
    """Returns any integer that appears more than once

        >>> find_dupes_again([1, 3, 2, 4, 4, 4, 5, 6, 6, 7, 8, 9])
        4

    """

    # nlg(n) time to sort - in place, so dupes will be next to one another
    arr.sort()

    # find first duplicate and return it. Worst case O(n)
    for i in range(1, len(arr)):

        if arr[i] == arr[i+1]:
            return arr[i]

    return False



# space: O(1) - doesn't count all extra variables. If list is long, still small
# runtime: nlg(n) by use of binary division
def find_dupes_better(arr):
    """Returns any integer that appears more than once

        >>> find_dupes_better([1, 3, 2, 4, 4, 4, 5, 6, 6, 7, 8, 9])
        4

    """

    # divide range of possible numbers in arr in half
    floor = 1
    # because ints are in the range 1...n in list of length n+1, 
    # but we don't know n, this will find n as ceiling
    ceiling = len(arr) - 1

    # iterative loop to avoid space of recursive callstack 
    while floor < ceiling:

        # mid is the value of n/2
        mid = floor + (ceiling - floor)/2

        lower_floor, lower_ceiling = floor, mid
        upper_floor, upper_ceiling = mid+1, ceiling

        items_in_lower_half = 0

        for item in arr:

            # if item is in lower range, incretment lower range item count
            if item <= lower_ceiling and item >= lower_floor:
                items_in_lower_half += 1

            # find possible number of values contained in lower range
            num_pos_values_lower = lower_ceiling - lower_floor + 1

            # if there are more items than possible values, 
            # at least one duplicate exists in the lower half. 
            if items_in_lower_half > num_pos_values_lower:

                # re-divide list in half and continue
                floor, ceiling = lower_floor, lower_ceiling

            # otherwise, there must be at least one duplicate in the upper half
            else:
                floor, ceiling = upper_floor, upper_ceiling

    # this is a bit tricky...
    # when floor and ceiling finally converge, that is the range that has a dupe
    # the range will be only the dupe, or it would have kept iterating. 
    return floor


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
