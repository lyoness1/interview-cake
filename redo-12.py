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

        >>> find_rotation(['ptolemaic','retrograde','supplant','undulate',
        ... 'xenoepist','asymptote','babka','banoffee','engender','karpatka',
        ... 'othellolagkage'])
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


# 14: In Flight Movies
# Runtime: O(nlg(n)) to sort
# Space: O(1)
# Edge cases: multiple movies same length, ties
def find_movies(flight_length, movies):
    """Returns two movies that can be watched during flight time

    >>> find_movies(120, [60, 30, 70, 80, 40, 30, 60, 90])
    [(30, 90), (30, 90), (40, 80), (60, 60)]

    """

    movies.sort()  # [30, 30, 40, 60, 60, 70, 80, 90]

    floor = 0
    ceiling = len(movies)-1

    output = []

    while ceiling - floor >= 1:

        # if floor and celing movies match flight time, add to output
        if movies[floor] + movies[ceiling] == flight_length:
            output.append((movies[floor], movies[ceiling]))
            # account for same length but didtinct movies in list
            if movies[floor+1] == movies[floor]: 
                floor += 1
            elif movies[ceiling-1] == movies[ceiling]:
                ceiling -= 1
            else:
                floor += 1
                ceiling -= 1

        # if the sum of movie lengths is too long, decrease ceiling
        elif movies[floor] + movies[ceiling] > flight_length:
            ceiling -= 1

        # if the sum of movie lengths is too short, increment floor
        else:
            floor += 1

    return output


# 15: Fibonacci
# Runtime: 
# Space: 
# Edge cases: 0, 1
def get_nth_fib(n):
    """Returns the nth Fibonacci number

        >>> get_nth_fib(4)
        3

        >>> get_nth_fib(6)
        8

    """

    if n in [0, 1]:
        return n

    prev2 = 0
    prev1 = 1
    fib = prev1 + prev2
    step = 2

    while step < n:

        prev2 = prev1
        prev1 = fib
        fib = prev2 + prev1

        step += 1 

    return fib









if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"