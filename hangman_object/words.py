from random import randint


class Words:
    def __init__(self):
        self.words = ('test', 'testtest')

    def get_word(self):
        index = randint(0, len(self.words) - 1)
        return self.words[index]
