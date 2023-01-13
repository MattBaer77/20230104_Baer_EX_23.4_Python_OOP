from random import choice

class WordFinder:

    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """Creates a new instance of WordFinder

        Attributes
        ----------
        path: str
            the name of any .txt file containing 1 word per line for at least 1 line
        words: list
            a list of the words read from the file from the entered path
        length: int
            an integer representing the number of words read
        
        """

        self.path = path

        self.words = self.load_dictionary()

        self.length = len(self.words)

    def load_dictionary(self):
        #reads dictionary file
        #saves to list
        words_list = list()
        words_read = 0

        file = open(f'{self.path}', 'r')
        for line in file:
            words_list.append(line.strip())
            words_read += 1
        file.close()

        print(f"{words_read} words read.")

        return words_list

    def random(self):
        """returns a random word from the list of words"""
        return choice(self.words)

class SpecialWordFinder(WordFinder):
    """Special wordfinder for handling lists with blanks and comments"""

    def load_dictionary(self):
                #reads dictionary file
        #saves to list
        words_list = list()
        words_read = 0

        file = open(f'{self.path}', 'r')
        for line in file:
            if not line.startswith('#'):
                words_list.append(line.strip())
                words_read += 1
        file.close()

        print(f"{words_read} words read.")

        return words_list