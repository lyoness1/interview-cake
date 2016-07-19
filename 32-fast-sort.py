"""
Write a function that takes:

- a list of unsorted_scores
- the highest_possible_score in the game

and returns a sorted list of scores in less than O(nlg(n)) time.

"""

# Runtime: counting sort is O(n)
# Space: O(n) to make histogram and output
def fast_sort(arr, max_score):
    """Takes an unsorted arr and a max_score and returns sorted list

        >>> fast_sort([20, 0, 40, 60, 15, 3, 80, 56, 60, 44, 90, 100], 100)
        [0, 3, 15, 20, 40, 44, 56, 60, 60, 80, 90, 100]

    """

    # counting sort - make histogram of counts for each score (score = index)
    histogram = [0] * (max_score + 1)

    # populate histogram
    for score in arr:
        histogram[score] += 1

    # reprint scores in output array
    output = []
    # iterate over entire histogram
    for i in range(len(histogram)):
        # for each score/index, append the score count's number of times
        for count in range(histogram[i]):
            output.append(i)

    return output



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
