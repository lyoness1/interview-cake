"""
Build a word cloud, an infographic where the size of a word corresponds to how 
often it appears in the body of text.

"""

def get_word_data(sentence):
    """Returns a dictionary of word frequency

        >>> get_word_data('After beating the eggs, Dana read the next step: Add milk and eggs, then add flour and sugar.')
        {'and': 2, 'then': 1, 'eggs,': 2, 'read': 1, 'flour': 1, 'after': 1, 'milk': 1, 'next': 1, 'add': 2, 'sugar.': 1, 'the': 2, 'beating': 1, 'step:': 1, 'dana': 1}

    """

    # make a list of all lower-case words
    words = sentence.lower().split()

    # remove punctuation (not apostrophy's)
    punctuation = ".,:;!?()"
    for word in words:
        word.strip(punctuation)

    # initialize and populate histogram of word counts
    histogram = {}
    for word in words: 
        if word in histogram:
            histogram[word] += 1
        else: 
            histogram[word] = 1

    return histogram


# runtime: O(n)
# space: O(n)
# all words lower case, even proper nouns
# all punctuation ignored, except hyphens
def get_better_word_data(sentence):
    """Returns a dictionary of word frequency

        >>> get_better_word_data('After beating the eggs, Dana read the next step: Add milk and eggs, then add flour and sugar.')
        {'and': 2, 'then': 1, 'read': 1, 'flour': 1, 'eggs': 2, 'after': 1, 'add': 2, 'next': 1, 'step': 1, 'the': 2, 'beating': 1, 'milk': 1, 'dana': 1}

        >>> get_better_word_data('Cliff finished his cake and paid the bill. Bill finished his cake at the edge of the cliff.')
        {'and': 1, 'his': 2, 'of': 1, 'bill': 2, 'paid': 1, 'finished': 2, 'edge': 1, 'at': 1, 'cake': 2, 'the': 3, 'cliff': 1}

    """

    # initialize histogram dict
    histogram = {}

    # initialize word string to concatinate
    current_word = ""

    # loop through characters in input sentence
    # punctuation will be ignored, including apostrphe's
    for char in sentence:
        # if char is alphabetic, lower-case it and concatinate to current_word
        if char.isalpha() or char == "-":
            char = char.lower()
            current_word += char
        # if a space is encountered, add word to histogram and reset curr_word
        elif char == " ":
            if current_word in histogram:
                histogram[current_word] += 1
            else: 
                histogram[current_word] = 1
            current_word = ""

    return histogram


# Interview Cake answer
class WordCloudData:

    def __init__(self, input_string):
        self.words_to_counts = {}
        self.populate_words_to_counts(input_string)

    def populate_words_to_counts(self, input_string):
        # iterates over each character in the input string, splitting
        # words and passing them to add_word_to_dictionary()

        current_word = ''
        for i in range(0, len(input_string)):

            character = input_string[i]

            # if we reached the end of the string we check if the last
            # character is a letter and add the last word to our dictionary
            if i == len(input_string)-1:
                if self.is_letter(character): current_word += character
                if current_word: self.add_word_to_dictionary(current_word)

            # if we reach a space or emdash we know we're at the end of a word
            # so we add it to our dictionary and reset our current word
            elif character == ' ' or character == u'\u2014':
                if current_word: self.add_word_to_dictionary(current_word)
                current_word = ''

            # we want to make sure we split on ellipses so if we get two periods in
            # a row we add the current word to our dictionary and reset our current word
            elif character == '.':
                if i < len(input_string)-1 and input_string[i+1] == '.':
                    if current_word: self.add_word_to_dictionary(current_word)
                    current_word = ''

            # if the character is a letter or an apostrophe, we add it to our current word
            elif self.is_letter(character) or character == '\'':
                current_word += character

            # if the character is a hyphen, we want to check if it's surrounded by letters
            # if it is, we add it to our current word
            elif character == '-':
                if i > 0 and self.is_letter(input_string[i-1]) and \
                        self.is_letter(input_string[i+1]):
                    current_word += character

    def add_word_to_dictionary(self, word):

        # if the word is already in the dictionary we increment its count
        if word in self.words_to_counts:
            self.words_to_counts[word] += 1

        # if a lowercase version is in the dictionary, we know our input word must be uppercase
        # but we only include uppercase words if they're always uppercase
        # so we just increment the lowercase version's count
        elif word.lower() in self.words_to_counts:
            self.words_to_counts[word.lower()] += 1

        # if an uppercase version is in the dictionary, we know our input word must be lowercase.
        # since we only include uppercase words if they're always uppercase, we add the
        # lowercase version and give it the uppercase version's count
        elif word.capitalize() in self.words_to_counts:
            self.words_to_counts[word] = 1
            self.words_to_counts[word] += self.words_to_counts[word.capitalize()]
            del self.words_to_counts[word.capitalize()]

        # otherwise, the word is not in the dictionary at all, lowercase or uppercase
        # so we add it to the dictionary
        else:
            self.words_to_counts[word] = 1

    def is_letter(self, character):
        return character in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"