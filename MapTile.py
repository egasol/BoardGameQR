from enum import Enum, auto


class Terrain(Enum):
    Ground = auto()
    Mountain = auto()
    Ocean = auto()
    Forest = auto()
    Farm = auto()


class MapTile:
    def __init__(self, terrain):
        if terrain == Terrain.Ground:
            self.is_walkable = True
            self.symbol = " "
            self.name = "grassland"
        elif terrain == Terrain.Mountain:
            self.is_walkable = False
            self.symbol = "♤"
            self.name = "mountains"
        elif terrain == Terrain.Ocean:
            self.is_walkable = False
            self.symbol = "~"
            self.name = "ocean"
        elif terrain == Terrain.Forest:
            self.is_walkable = True
            self.symbol = "♧"
        elif terrain == Terrain.Farm:
            self.is_walkable = True
            self.symbol = "⛆"

        self.terrain = terrain
        self.event = None

    def set_terrain(self, terrain):
        self.terrain = terrain

    def set_event(self, event):
        self.event = event
        self.symbol = event["symbol"]
