from chances_error import ChancesError


class Chances(object):
    def __init__(self, chances=None):
        self.chances = 9 if chances is None else chances

    def get_chances(self):
        return self.chances

    def decrease_chances(self):
        self.chances -= 1

        if self.chances == 0:
            raise ChancesError('You don`t have any chances :P')
