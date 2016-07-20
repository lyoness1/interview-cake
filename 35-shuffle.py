"""
Shuffle things

"""

# randint(A, B) produces n, such that A <= n <= B
from random import randint


def shuffle(arr):
    """randomly shuffles a list in place

        >>> shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


    """

    L = len(arr) - 1

    # remove last item in arr, insert at random index
    for _ in range(len(arr)):
        item = arr.pop()
        location = randint(0, L)
        arr[location:location] = [item]

    return arr


# Interview Cake solution
# If we didn't have the "in place" requirement, we could allocate a new list, 
# then one-by one take a random item from the input list, remove it, put it in 
# the first position in the new list, and keep going until the input list is 
# empty (well, probably a copy of the input list—best not to destroy the input)
# How can we adapt this to be in-place?
# What if we make our new "random" list simply be the front of our input list?
def shuffling(the_list):

    # if it's 1 or 0 items, just return
    if len(the_list) <= 1:
        return the_list

    last_index_in_the_list = len(the_list) - 1

    # walk through from beginning to end
    for index_we_are_choosing_for in xrange(0, len(the_list)):

        # choose a random not-yet-placed item to place there
        # (could also be the item currently in that spot)
        # must be an item AFTER the current item, because the stuff
        # before has all already been placed
        random_choice_index = randint(index_we_are_choosing_for, last_index_in_the_list)

        # place our random choice in the spot by swapping
        the_list[index_we_are_choosing_for], the_list[random_choice_index] = the_list[random_choice_index], the_list[index_we_are_choosing_for]




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
