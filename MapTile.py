from enum import Enum, auto


class Terrain(Enum):
    Ground = auto()
    Wall = auto()


class MapTile:
    def __init__(self, terrain):
        self.terrain = terrain
    
    def set_terrain(self, terrain):
        self.terrain = terrain
    
    def get_symbol(self):
        if self.terrain == Terrain.Ground:
            symbol = " "
        elif self.terrain == Terrain.Wall:
            symbol = "W"
        else:
            symbol = "?"
        
        return symbol