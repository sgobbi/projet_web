from game_backend.sword import Sword
from .map_generator import Generator
from .player import Player
from .monster import Monster
from .coins import Coin
from .sword import Sword



class Game:
    def __init__(self, width=96, height=32):
        self._generator = Generator(width=width, height=height)
        self._generator.gen_level()
        self._generator.gen_tiles_level()
        self._map = self._generator.tiles_level
        self._generator.gen_accessories()

        self._player = Player()
        self._player.initPos( self._map )

        self._monster = Monster()
        self._monster.initPos( self._map )

        #self._coin = Coin()
        #self._coin.initPos( self._map )

        #self._sword = Sword()
        #self._sword.initPos( self._map )

        


    def getMap(self):
        return self._map

    def move(self, dx, dy):
        #dat1 = self._player.move(dx, dy, self._map)[0]
        #dat2 = self._player.move(dx, dy, self._map)[1]
        #accessoire = self._player.move(dx, dy, self._map)[2]
        #return dat1, dat2
        
        return self._player.move(dx, dy, self._map)