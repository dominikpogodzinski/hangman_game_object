from chances_error import ChancesError
from hangman import Hangman


class HangmanGame:
    def __init__(self):
        self.hangman = Hangman()
        print(self.hangman.get_title())

    def play(self):
        while True:
            print(f'You have: {self.hangman.get_chances()} chances')
            print(self.hangman.get_word_for_search())
            letter = input('Give me some letter: ')

            if self.hangman.is_it_word_to_find(letter):
                self.win()
                break

            try:
                self.hangman.guess_letter(letter)
            except ChancesError:
                self.loose()
                break

            if self.hangman.are_all_letters_found():
                self.win()
                break

    def loose(self):
        print('\nLoooser!!!!!')
        self.print_word_to_find()

    def win(self):
        print('\nCongratulations!!!')
        self.print_word_to_find()

    def print_word_to_find(self):
        print(f'Search word is: {self.hangman.get_word_to_find()}')


def main():
    while True:
        game = HangmanGame()
        game.play()

        if input('Do you play one moore time? [t/n]: ') == 'n':
            print('Thanks for playing')
            break


if __name__ == '__main__':
    main()
