# 28: Find matching closing parenthesis
# Runtime: O(n)
# Space: O(1)
# Edge cases: 

def find_closing(sentence, pos):
    """Returns the location of a closing parenthesis, given and opening one

    >>> find_closing("Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.", 10)
    79

    """

    opens = 1

    # note: using slice could create space O(n), better to just increment pos
    for idx, char in enumerate(sentence[pos+1:]):
        if char == "(":
            opens += 1
        elif char == ")":
            opens -= 1
        if opens == 0:
            return pos + idx + 1

    return "parenthesis are no balanced"


# 29: Parse braces
# Runtime: O(n)
# Space: O(m) where m is number of openers
# Edge cases: 
def parse_braces(sentence):
    """Returns boolean for whether braces are properly closed

    >>> parse_braces("{ [ ] ( ) }")
    True

    >>> parse_braces("{ [ ( ] ) }")
    False

    >>> parse_braces("{ [ }")
    False

    """

    stack = []
    openers = ["(", "[", "{"]

    for char in sentence:
        if char in openers:
            stack.append(char)
        if char == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                return False
        if char == "]":
            if stack[-1] == "[":
                stack.pop()
            else: 
                return False
        if char == "}":
            if stack[-1] == "{":
                stack.pop()
            else: 
                return False

    if not stack:
        return True
    else:
        return False


# 30: Is any permutation of input a palindrome?
# Runtime: O(n)
# Space: O(n)
# Edge cases:
def is_palindrome(str):
    """Returns boolean to indicate palindrome present

        >>> is_palindrome("civic")
        True

        >>> is_palindrome("ivicc")
        True

        >>> is_palindrome("civil")
        False

        >>> is_palindrome("livci")
        False

    """

    char_counts = {}

    for char in str:
        if char not in char_counts:
            char_counts[char] = 1
        else: 
            char_counts[char] += 1

    odds = 0

    for count in char_counts.values():
        if count % 2 != 0:
            odds += 1

    if odds > 1:
        return False

    return True


# 31: All permutations of input string
# Runtime:
# Space: 
# Edge cases: 
def make_permutations(phrase):
    """Returns all permutations of an input string using recursion

        >>> make_permutations('bath')
        set(['abth', 'hbta', 'bath', 'bhat', 'tbha', 'ahtb', 'atbh', 'hatb', 'thba', 'btha', 'htab', 'abht', 'ahbt', 'tbah', 'bhta', 'baht', 'habt', 'thab', 'athb', 'btah', 'tabh', 'htba', 'tahb', 'hbat'])

    """
    
    # base case: one long
    if len(phrase) < 2:
        return set([phrase])

    # split phrase into one letter and rest of letters
    last_char = phrase[-1]
    other_chars = phrase[:-1]

    # get all possibilities
    smaller_perms = make_permutations(other_chars)

    # initailize output set
    perms = set()

    # put missing letter in each possible location within smaller perms
    for smaller_perm in smaller_perms:
        for i in xrange(len(phrase)):
            perms.add(smaller_perm[:i] + last_char + smaller_perm[i:])

    return perms


# 32: Sort Game Scores
# Runtime: O(2n) --> O(n)
# Space: O(2n) for histogram and output
# Edge cases: 
def sort_scores(unsorted, highest):
    """Takes an unsorted arr and a max_score and returns sorted list

        >>> sort_scores([20, 0, 40, 60, 15, 3, 80, 56, 60, 44, 90, 100], 100)
        [0, 3, 15, 20, 40, 44, 56, 60, 60, 80, 90, 100]

    """

    scores = [0] * (highest + 1)

    for num in unsorted:
        scores[num] += 1

    output = []

    for idx, score in enumerate(scores):
        for i in xrange(score):
            output.append(idx)

    return output


# 33: Find duplicate in range 1...n
# Runtime: O(1)
# Space: O(1)
# Edge case: 
def find_duplicate(arr):
    """Returns the number that appears twice

        >>> find_duplicate([1, 2, 3, 4, 5, 5, 6, 7, 8, 9])
        5

    """
    # get max
    n = len(arr) - 1

    # duplicate number is actual sum minus expected sum w/o duplicate
    return sum(arr) - ((n*n + n) / 2)










if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"