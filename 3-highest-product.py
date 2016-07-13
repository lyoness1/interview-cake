"""
Given a list_of_ints, find the highest_product you can get from three of the integers.
The input list_of_ints will always have at least three integers.
"""

# Solution 1: Brute force
def highest_product(arr):
    """Returns the highest product

    >>> highest_product([1, 2, 3, 4, 5])
    60

    """

    product = 1

    for i in range(3):
        # find the max value in the list, get the index, pop it, and mulitply
        product *= arr.pop(arr.index(max(arr)))

    return product

# Analysis:
# Runtime is O(3n) --> O(n). I bet we can do better...
# Space is constant

# Solution 2: Keep track of maxes, pass over list once
def highest_product_2(arr):
    """Returns the highest prodcut of three integers

    >>> highest_product_2([2, 3, 4])
    24

    """

    # make a list to store the highest three ints, initializing to first three
    maxes = [arr[0], arr[1], arr[2]]

    # find the lowest of the highest three ints
    lowest_max = min(maxes)

    # go through the rest of the list to check for higher values
    for num in arr[3:]:
        # if any value is higher than the lowest max, update maxes list
        if num > lowest_max:
            # remove the old maximum
            maxes.remove(lowest_max)
            # add the new one
            maxes.append(num)
            # recalculate the lowest max for continued comparison
            lowest_max = min(maxes)

    return maxes[0] * maxes[1] * maxes[2]

# Analysis:
# Runtime: O(n)
# Space: Constant (just making a new list of three and a lowest max variable)


# Solution 3: Gotchas! 
# What about negative numbers??
def highest_product_3(arr):
    """Returns the highest prodcut of three integers

    >>> highest_product_3([-10, -10, 1, 3, 2])
    300

    >>> highest_product_3([1, 10, -5, 1, -100])
    5000

    """
    # sort in place (this will take O(n), at least)
    arr.sort()

    # get the maximum positive solution (this only works if all three > 0)
    max_product = arr[-1] * arr[-2] * arr[-3]

    # check for better solutions involving negatives
    # the only solution involving negatives will have exactly two of them
    # check the two options manually and return the largest one. 
    if arr[0] < 0 and arr[1] < 0:
        if arr[0] * arr[1] * max(arr[-1], arr[-2], arr[-3]) > max_product:
            max_product = arr[0] * arr[1] * max(arr[-1], arr[-2], arr[-3])

    return max_product

# Analysis:
# Runtime: O(n) for sorting
# Space: constant. Well, this seems pretty good! 


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
