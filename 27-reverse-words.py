"""
Write a function reverse_words() that takes a string message and reverses the 
order of the words in place. 

"""

# Runtime: O(n)
# Space: O(n) for words list
def reverse_words(s):
    """Reverses words 'in place'

    >>> reverse_words(
    ... 'find you will pain only go you recordings security the into if'
    ... )
    'if into the security recordings you go only pain will you find'

    """

    # create a list to store the words, split on spaces
    words = s.split(" ")

    # reverse the list in place, using slicing to insert
    for i in range(len(words)-1):
        # remove last word and insert at increasing locations
        word = words.pop()
        # have to wrap word in list so it is moved as entire string, not chars
        words[i:i] = [word]

    # return the words joined on spaces
    return " ".join(words)


def try_again(phrase):
    """Reverses words 'in place'

    >>> reverse_words(
    ... 'find you will pain only go you recordings security the into if'
    ... )
    'if into the security recordings you go only pain will you find'

    """

    words = phrase.split(" ")

    left = 0
    right = len(words) - 1

    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1

    return " ".join(words)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"