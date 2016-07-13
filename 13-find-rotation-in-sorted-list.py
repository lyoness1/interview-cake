"""
I opened up a dictionary to a page in the middle and started flipping through, 
looking for words I didn't know. I put each word I didn't know at increasing 
indices in a huge list I created in memory. When I reached the end of the 
dictionary, I started from the beginning and did the same thing until I reached 
the page I started at.

Now I have a list of words that are mostly alphabetical, except they start 
somewhere in the middle of the alphabet, reach the end, and then start from the 
beginning of the alphabet. In other words, this is an alphabetically ordered 
list that has been "rotated."

Write a function for finding the index of the "rotation point," which is where 
I started working from the beginning of the dictionary. This list is huge 
(there are lots of words I don't know) so we want to be efficient here.
"""

# Assumption: all lower case

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

# Solution 1: brute force (not efficient)
def find_rotation(arr):
    """Returns the index of the rotation point

        >>> find_rotation(['play', 'xebra', 'bat', 'cat', 'dog'])
        2

    """
    # edge case: already sorted
    if arr[0] < arr[-1]:
        return 0

    for idx, item in enumerate(arr):
        # if the first letter of next item is 'lower' than first letter of item,
        # rotation point is index of next item
        if arr[idx+1][0] < item[0]:
            return idx+1


# Solution 2: Divide and conquer. 
def find_rotation_efficient(arr):
    """Returns the index of the rotation point

        >>> find_rotation_efficient(words)
        5

    """
    # edge case: already sorted
    if arr[0] < arr[-1]:
        return 0

    low = 0
    high = len(arr)-1

    # when high is one greater than low, high will be rotation index
    while high - low > 1:

        # start guessing at middle
        guess_index = low + (high - low) / 2

        # rotation is left
        if arr[guess_index] < arr[low]:
            high = guess_index

        # rotation is right
        else:
            low = guess_index

    return high






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"
        