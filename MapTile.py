from enum import Enum, auto


class Terrain(Enum):
    Ground = auto()
    Wall = auto()
    Water = auto()


class MapTile:
    def __init__(self, terrain):
        self.terrain = terrain
        self.event = None

    def set_terrain(self, terrain):
        self.terrain = terrain

    def set_event(self, event):
        self.event = event

    def get_symbol(self):
        if self.terrain == Terrain.Ground:
            symbol = " "
        elif self.terrain == Terrain.Wall:
            symbol = "▢"
        elif self.terrain == Terrain.Water:
            symbol = "~"
        else:
            symbol = "?"

        if self.event is not None:
            symbol = "E"

        return symbol

    def is_walkable(self):
        if self.terrain == Terrain.Ground:
            return True
        else:
            return False
