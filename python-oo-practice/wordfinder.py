from random import choice

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    def __init__(self, file):
        self.file = file
        self.words = self.convert_file_to_str().split("\n")
    
    def random(self):
        """
        Selects random word from file and returns it
        """
        if(len(self.words) != 0):
            return choice(self.words)

    def convert_file_to_str(self):
        """
        Gets file, reads file and add to words list
        """
        file = open(self.file, 'r')
        file_str = file.read()
        file.close()
        return file_str