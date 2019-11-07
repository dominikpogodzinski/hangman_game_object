from random import randint


class Words:
    def get_word(self):
        words_in_file = self.get_words_count()
        word_number = randint(1, words_in_file)
        return self.get_word_from_file(word_number).strip('\n')

    @staticmethod
    def get_word_from_file(word_number):
        with open('words_from_file/words.txt', 'r') as file:
            for i in range(1, word_number + 1):
                word = file.readline()
        return word

    @staticmethod
    def get_words_count():
        words_in_file = 0
        with open('words_from_file/words.txt', 'r') as file:
            while file.readline():
                words_in_file += 1

        return words_in_file
