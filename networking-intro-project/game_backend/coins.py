import random

class Coin:
    def __init__(self, symbol="$"):
        self._symbol = symbol
        self._x = None
        self._y = None

    def initPos(self, _map):
        n_row = len(_map)
        #n_col = len(_map[0])

        y_init = random.randint(0,n_row-2)
        found = False
        while found is False:
            y_init += 1
            for i,c in enumerate(_map[y_init]):
                if c == ".":
                    x_init = i
                    found = True
                    break

        self._x = x_init
        self._y = y_init

        _map[self._y][self._x] = self._symbol