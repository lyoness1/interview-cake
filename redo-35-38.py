# 35: In place shuffle
# Runtime: O(n)
# Space: O(1)
# Edge cases: 

# randint(A, B) produces n, such that A <= n <= B
from random import randint

# math note: 
# 1/n that an item is picked first
# (n-1)/n that some other item is picked, (n-1)/n * 1/(n-1) the item is second
# (n-1)/n * (n-2)/(n-1) * 1/(n-2) the item is picked third...
# all items have 1/n probibility of being chosen in any order

def shuffle(arr):
    """randomly shuffles a list in place

        >>> shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        10

    """

    L = len(arr) - 1

    for i in xrange(len(arr)):

        idx_to_switch = randint(i, L)
        arr[i], arr[idx_to_switch] = arr[idx_to_switch], arr[i]

    return len(arr)


# 36: Riffle
# Runtime: O(n)
# Space: O(1)
# Edge cases: 
def is_riffle(deck, half1, half2):
    """Returns a boolean if deck is a single riffle of half1 and half2

        >>> is_riffle([1, 2, 4, 5, 3, 6], [1, 2, 3], [4, 5, 6])
        True

        >>> is_riffle([1, 2, 6, 5, 3, 4], [1, 2, 3], [4, 5, 6])
        False

    """

    deck_idx = 0
    half1_idx = 0
    half2_idx = 0

    for i in xrange(len(deck)-1):
        if deck[deck_idx] == half1[half1_idx]:
            deck_idx += 1
            half1_idx += 1
        elif deck[deck_idx] == half2[half2_idx]:
            deck_idx += 1
            half2_idx += 1
        else:
            return False

    return True


# 37: Rand7 --> Rand5
# Runtime: 
# Space: 
# Edge cases: 
def rand7():
    return randint(1, 7)

def rand5():
    pick = rand7()
    if pick < 6:
        return pick
    else: 
        return rand5()










if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
