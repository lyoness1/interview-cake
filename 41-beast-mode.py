"""
List 1...n
n+1 items long --> at least one duplicate #
optimize for space --> O(1)
if space optimized, runtime nlg(n) on account of sort in place
can we do it in runtime O(n)?

"""

def find_dupes(arr):
    """Returns a duplicate number in list 1...n with n+1 items"""

    # if a value is repeated, the list linked by position/index+1 will loop
    # how to measure in a loop? 'fast runner' will lap 'slow runner'
    # if no duplicates, all values will be seen before loop starts. 

    slow = arr[-1]
    fast = arr[-1]

    values_seen = 1

    looped = False

    while not looped:

        # fast steps twice for every slow step of one
        fast = arr[fast-1]
        fast = arr[fast-1]
        slow = arr[slow-1]

        # increment how many values have been seen by slow runner
        # if slow runner sees all values before looping, then no duplicates
        values_seen += 1

        if fast == slow:
            looped = True

    # if slow runner saw all values, then no duplicates
    if values_seen < len(arr):
        return fast

    else:
        raise Exception("No duplicates")



# space O(1) because no data structures created (variables don't count)
# runtime O(n) coming from, worst case, a few loops around the list
def beast_mode(arr):
    """Returns a duplicate number in list 1...n with n+1 items

        >>> beast_mode([4, 6, 5, 2, 3, 8, 7, 9, 1, 5])
        5

        >>> beast_mode([5, 7, 2, 2, 4, 9, 8, 6, 1, 3])
        2

    """

    # first, start at position n+1 (arr[-1]), as that will not have incoming int
    # take n steps, so garuanteed to be in a cycle
    # grab that value, step until return (count length of cycle)
    # start over with two 'runners' cycle length apart. when the runners
    # are at the same value, that is the repeat number, or the first
    # number in the cycle!

    # start at the head of the list, or the last value
    position = len(arr)

    # move forward n steps in list to garuantee in loop of some length
    for i in xrange(len(arr)-1):
        position = arr[position-1]

    # count how long the cycle is by incrementing steps until returning to 
    # starting position (calculated above)
    steps = 1
    new_position = arr[position-1]
    while new_position != position:
        new_position = arr[new_position-1]
        steps += 1

    # send out two runners 
    # both start at head of list
    runner1 = len(arr)
    runner2 = len(arr)

    # runner1 gets a head start by the length of the loop cycle
    for i in xrange(steps):
        runner1 = arr[runner1-1]

    # once the distance apart is the length of the loop, runner2 starts at 
    # the same speed as runner1. When the meet, that will be the start of 
    # the loop which is the position with two incoming pointers, or the dupe!
    while runner1 != runner2:
        runner1 = arr[runner1-1]
        runner2 = arr[runner2-1]

    return runner1



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"

