# 0, 1, 2, 3, 4, 5, 6, 7,  8, ...
# 0, 1, 1, 2, 3, 5, 8, 13, 21,...


def fib(n):
    """Returns n'th fibonacci number

        >>> fib(7)
        13

    """

    if n in [0, 1]:
        return n

    # initialize previous two numbers
    prev2 = 0
    prev1 = 1

    # loop will be for 2nd fib num forward
    step = 2

    while step <= n:
        result = prev1 + prev2
        prev2 = prev1
        prev1 = result
        step += 1

    return result

# Runtime: O(n)
# Space: O(1)


def fib_recursive(n):
    """Returns n'th fibonacci number

        >>> fib_recursive(7)
        13

    """

    if n in [0, 1]:
        return n

    else: 
        return fib_recursive(n-1) + fib_recursive(n-2)


# Runtime: O(2^n) because two recursive calls, repeat steps


def fib_recursive_better(n):
    """Returns n'th fibonacci number using memorization

        >>> fib_recursive_better(8)
        21

    """

    # create dictionary to store previously calculated values
    already_computed = {
        0: 0,
        1: 1
    }

    def fib_helper(n, already_computed):
        """Recursive helper"""

        # base case: already computed
        if n in already_computed:
            return already_computed[n]

        # calculate
        result = (fib_helper(n-1, already_computed) +
                            fib_helper(n-2, already_computed))

        # memorize
        already_computed[n] = result

        return result

    return fib_helper(n, already_computed)

# Runtime: O(n)
# Space: O(n)




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
