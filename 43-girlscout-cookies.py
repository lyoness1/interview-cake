"""
Print merged lists in sorted order. Inputs will already be sorted. 

"""

# runtime: O(n) look at each item once, worst case
# space: O(n) for output list
def merge_lists(list1, list2):
    """Merges lists in order

        >>> merge_lists([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19])
        [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]

        >>> merge_lists([3, 4, 6, 10, 11], [1, 5, 8, 12, 14, 19, 24, 55])
        [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 19, 24, 55]

    """

    # initialize a new output list
    merged = []

    # use indexes for each list to comparge items
    idx1 = 0
    idx2 = 0

    # loop
    while idx1 < len(list1) and idx2 < len(list2):

        # compare items
        # if the current item in list 1 <= current in list2
        if list1[idx1] <= list2[idx2]:
            # add item from list1 to output
            merged.append(list1[idx1])
            # increment index
            idx1 += 1

        else: 
            # add item from lsit2 to output
            merged.append(list2[idx2])
            # increment index
            idx2 += 1

    # if list1 has been iterated over
    if idx1 == len(list1):
        merged.extend(list2[idx2:])

    # if list2 has been iterated over
    else:
        merged.extend(list1[idx1:])

    return merged



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"

