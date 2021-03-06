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

    for i in xrange(L):
        pick = randint(i, L)
        arr[i], arr[pick] = arr[pick], arr[i]

    # would return arr, but len(arr) is for doctest
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
# Runtime: worst case is O('inf'), but unlikely. 
# Space: O(1) for iterative solution, O('inf') for recursive solution
# Edge cases: 
def rand7():
    return randint(1, 7)

def rand5():
    pick = rand7()
    if pick < 6:
        return pick
    else:
        rand5()


# 38: Rand5 --> Rand7
# Runtime: worst case is O(inf) but unlikely
# Space: O(1) for iterative, O(inf) for recursive (unlikely)
# Edge cases: 
def rando5():
    return randint(1, 5)

def rando7():

    while True:

        pick1 = rando5()
        pick2 = rando5()

        # 25 choices equal probability
        pick = pick1 * pick2

        if pick <= 21:
            return (pick % 7) + 1









if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
