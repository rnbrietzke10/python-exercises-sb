from wordfinder import WordFinder
"""
Class that inherits from WordFinder
Filters out words that don't have # in front of it and that are not empty strings
"""

class SpecialWordFinder(WordFinder):
    def __init__(self, file):
        super().__init__(file)
        

    def remove_chars(self):
        self.words = [ x for x in self.words if "#" not in x]
        self.words = [ x for x in self.words if x]
        return self.words