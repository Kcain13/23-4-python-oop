"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    '''machine for finding random words from dictionary'''

    def __init__ (self, path):
        '''read words.txt and reports # items read'''
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        '''parse dic_file -> list of words'''
        return [w.strip() for w in dict_file]
    
    def random(self):
        '''return random word'''

        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    '''will help exclude blank lines/comments'''

    def parse(self, dict_file):
        ''' parse dict_file -> list of words'''
        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]