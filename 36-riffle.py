"""
I suspect the online poker game I'm playing shuffles cards by doing a single 
riffle. 

To prove this, let's write a function to tell us if a full deck of cards 
shuffled_deck is a single riffle of two other halves half1 and half2.

We'll represent a stack of cards as a list of integers in the range 1-52
(since there are 52 distinct cards in a deck).

"""

# runtime: O(n)
# space: O(n) b/c of callstack
def is_riffle(deck, firsthalf, secondhalf):
    """Returns True is deck is a single riffle of first and second halves

        >>> is_riffle([1, 2, 4, 3, 5, 6], [1, 2, 3], [4, 5, 6])
        True

        >>> is_riffle([1, 3, 4, 5, 6, 2], [1, 2, 3], [4, 5, 6])
        False

    """
    # base case: out of cards
    if not firsthalf or not secondhalf:
        return True

    top_card = deck.pop()

    if top_card == firsthalf[-1]:
        firsthalf.pop()
        return is_riffle(deck, firsthalf, secondhalf)

    elif top_card == secondhalf[-1]:
        secondhalf.pop()
        return is_riffle(deck, firsthalf, secondhalf)

    return False


# runtime: O(n)
# space: O(1)
# could do with indexing through lists, instead of popping, which would 
# not harm the original input lists
def is_riffle_iterative(deck, firsthalf, secondhalf):
    """Returns True is deck is a single riffle of first and second halves

        >>> is_riffle_iterative([1, 2, 4, 3, 5, 6], [1, 2, 3], [4, 5, 6])
        True

        >>> is_riffle_iterative([1, 3, 4, 5, 6, 2], [1, 2, 3], [4, 5, 6])
        False

    """
    # while there are still cards to look at
    while firsthalf or secondhalf:

        # match the top card of the deck with either of the halves
        # if it matches, remove the matching card and continue
        top_card = deck.pop()
        if top_card == firsthalf[-1]:
            firsthalf.pop()
        elif top_card == secondhalf[-1]:
            secondhalf.pop()
        # if it doesn't match one of the top cards, it's not a riffle
        else: 
            return False

    # once both halves are empty, all cards have been checked
    return True


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"