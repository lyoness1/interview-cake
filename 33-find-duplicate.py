"""
Write a function to find the number that appears twice in a list.
Hint: If the series is always 1, 2, 3,..., n-1, n: use math!

"""

# using .count()
# runtime O(n^2)
# space O(1)
def find_duplicate_1(arr):
    """Returns the number that appears twice

        >>> find_duplicate_1([1, 2, 3, 4, 5, 5, 6, 7, 8, 9])
        5

    """

    for item in arr:
        if arr.count(item) == 2:
            return item


# counting sort
# O(n) runtime
# O(n) space
def find_duplicate_2(arr):
    """Returns the number that appears twice

        >>> find_duplicate_2([1, 2, 3, 4, 5, 5, 6, 7, 8, 9])
        5

    """
    
    counter = [0] * (len(arr) + 1)

    for item in arr:
        counter[item] += 1

    return counter.index(2)


# using triangular series math
# sum(1 + 2 + ... + (n-1) + n) = (n^2 + n) / 2
# because:
# pairs sum to n+1: (1) + (n) = (n+1), (2) + (n-1) = (n+1), ...
# there are n/2 pairs
# sum(1 + 2 + ... + (n-1) + n) = (n/2)(n+1) = (n^2 + n) / 2
# runtime: O(n)
# space: O(1)
def find_duplicate_3(arr):
    """Returns the number that appears twice

        >>> find_duplicate_3([1, 2, 3, 4, 5, 5, 6, 7, 8, 9])
        5

    """
    # calculate the sum of the digits in the given input list
    given_sum = 0
    for item in arr:
        given_sum += item

    # mathmatically calculate what the sum of the series should be
    n = arr[-1]
    should_be_sum = (n*n + n) / 2

    # find the difference (will be the integer that is given twice)
    difference = given_sum - should_be_sum

    return difference






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"