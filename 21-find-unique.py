"""
Given the list of IDs, which contains many duplicate integers and one unique 
integer, find the unique integer.

The IDs are not guaranteed to be sorted or sequential. Orders aren't always 
fulfilled in the order they were received, and some deliveries get cancelled 
before takeoff.

"""

def find_unique(arr):
    """Returns the unique positive integer in the list

        >>> find_unique([1, 2, 3, 4, 5, 7, 6, 2, 5, 1, 3, 7, 6])
        4

    """

    # O(nlg(n))
    arr.sort()

    # O(n)
    for i in range(0, len(arr)/2+1, 2):
        if arr[i+1] != arr[i]:
            return arr[i]


def find_unique_again(arr):
    """Returns the unique positive integer in the list

        >>> find_unique_again([1, 2, 3, 4, 5, 7, 6, 2, 5, 1, 3, 7, 6])
        4

    """

    # O(n) space
    histogram = {}

    # O(n) runtime
    for item in arr:
        key = str(item)
        if key in histogram:
            histogram[key] += 1
        else: 
            histogram[key] = 1

    # O(n) runtime
    for k, val in histogram.iteritems():
        if val == 1:
            return int(k)


def find_unique_constant_space(arr):
    """Returns the unique positive integer in the list

        >>> find_unique_constant_space([1, 2, 3, 4, 5, 7, 6, 2, 5, 1, 3, 7, 6])
        4

    """

    unique = 0

    # the ^ operator (XOR, exclusive or) is a bitwise operator. 
    # it compares binary versions of the numbers, and for each digit, returns
    # a 0 if the digits are the same, or a 1 if the digits are each a 0 and 1. 
    # the first time the variable unique hits an ID, it will change to that ID,
    # but in binary. The next ID will change it to the bitwise difference 
    # between those two ID's. When it re-encounters an ID, it will 'cancel out'
    # that ID from before. Eventually, the unique variable will be left as 
    # only the binary version of the ID that wasn't cancelled out. 
    for item in arr:
        unique = unique ^ item

    return unique





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"