from .monster import Monster
from .coins import Coin
from .sword import Sword

class Player:
    def __init__(self, symbol="@"):
        self._symbol = symbol
        self._coins = 0
        self._swords = 0
        self._life = 5
        self._x = None
        self._y = None
    
    def get_life(self):
        return self._life
    

    def get_coins(self):
        return self._coins
    
    def get_swords(self):
        return self._life
    

    def initPos(self, _map):
        n_row = len(_map)
        #n_col = len(_map[0])

        y_init = n_row//2
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

    def move(self, dx, dy, map):
        new_x = self._x + dx
        new_y = self._y + dy

        if map[new_y][new_x] == "." or map[new_y][new_x] == "x" :
            ret =True
            map[new_y][new_x] = self._symbol
            map[self._y][self._x] = "."
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"."}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
            self._x = new_x
            self._y = new_y
        elif map[new_y][new_x] == "#":
            ret = False
            data = []
        elif map[new_y][new_x] == "O":
            ret = True
            map[new_y][new_x] = self._symbol
            map[self._y][self._x] = "."
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"."}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
            self._x = new_x
            self._y = new_y
            self._coins +=1
            #new_coin = Coin()
            #new_coin.initPos( map )
        elif map[new_y][new_x] == "T":
            ret = True
            map[new_y][new_x] = self._symbol
            map[self._y][self._x] = "."
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"."}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
            self._x = new_x
            self._y = new_y
            self._swords +=1
            #self.new_sword = Sword()
            #self.new_sword.initPos(self, map)

        elif map[new_y][new_x] == "W":
            if self._swords >=1:
                ret = True
                map[new_y][new_x] = self._symbol
                map[self._y][self._x] = "."
                data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"."}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
                self._x = new_x
                self._y = new_y
            else:
                ret = False
                data = []
                self._life -= 1


            #new_coin = Coin()
            #new_coin.initPos( map )
            

         #elif map[new_y][new_x] == "W":

        #accessoires= [self._life, self._swords, self._coins]

        return data, ret #, accessoires