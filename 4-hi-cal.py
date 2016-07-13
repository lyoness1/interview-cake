"""
Meetings are stored as tuples (start, end).
Write a function condense_meeting_times() that takes a list of meeting time 
ranges and returns a list of condensed ranges.

For example, given:

    [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

your function would return:

    [(0, 1), (3, 8), (9, 12)]

Do not assume the meetings are in order. The meeting times are coming from 
multiple teams.

Write a solution that's efficient even when we can't put a nice upper bound on 
the numbers representing our time ranges. Here we've simplified our times down 
to the number of 30-minute slots past 9:00 am. But we want the function to work 
even for very large numbers, like Unix timestamps. In any case, the spirit of 
the challenge is to merge meetings where start_time and end_time don't have an 
upper bound.

"""

# Solution 1: This doesn't work... go to #2
def condense_meeting_times(arr):
    """Returns condensed meeting times"""

    # make a list to store output
    output = []

    # sort the meeting times by start time (this will be O(n), at least)
    # without sorting by start times, the random order will make this O(n^2)
    arr.sort()

    # iterate over all the time blocks and check for merges
    for time_block in arr[:-1]:
        # unpack the first two meeting time
        first_start, first_stop = time_block
        # unpack the next time block into start and stop times
        second_start, second_stop = arr[arr.index(time_block) + 1]
        # if there is overlap, condense them
        if second_start <= first_stop:
            # the second one has the later stop
            if second_stop > first_stop:
                output.append((first_start, second_stop))
            # else, the first one had the later stop
            output.append((first_start, first_stop))
        # else, there wasn't overlap
        # append first meeting to output, and continue for loop
        output.append((first_start, first_stop))

    return output

# Analysis:
# Runtime O(n) to sort, O(n) to go through original list --> O(2n) --> O(n)
# Space O(n) to make a new output list

# Solution 2: 
def condense_meeting_times_2(arr):
    """Returns condensed meeting times

    >>> condense_meeting_times_2([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    [(0, 1), (3, 8), (9, 12)]

    >>> condense_meeting_times_2([(1, 2), (2, 3)])
    [(1, 3)]

    """

    # sort the meeting times by start time (this will be O(lg(n)), at least)
    # without sorting by start times, the random order will make this O(n^2)
    arr.sort()

    # make a list to store output
    output = [arr[0]]

    # iterate over all the time blocks and check for merges
    for time_block in arr[1:]:
        # get the times to compare against from the latest block in output
        first_start, first_stop = output[-1]
        # unpack the current time block being assessed for overlap
        second_start, second_stop = time_block
        # if the current time block overlaps with most recent, condense the two
        # by updating the entire tuple in the output list with latest time
        if second_start <= first_stop:
            output[-1] = (first_start, max(first_stop, second_stop))
        # else, there was no overlap. Add current to output and continue loop
        else:
            output.append((second_start, second_stop))

    return output

# Analysis:
# Runtime O(lg(n)) to sort, O(n) to go through original list --> O(2n) --> O(n)
# Space O(n) to make a new output list



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
