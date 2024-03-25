from MapTile import MapTile, Terrain

import random
import numpy as np


class MapGrid:
    def __init__(self, map_size, party):
        self.world_map, self.start = self._generate_map(map_size)
        self.party = party
        party.set_position(self.start)
        party.set_map(self)
    
    def _generate_map(self, map_size):
        print("generating map...")
        world_map = np.empty(map_size, dtype=object)
        world_map.flat = [MapTile(Terrain.Wall) for _ in world_map.flat]
        
        start_x = random.choice(range(1, map_size[0]-1))
        start_y = random.choice(range(1, map_size[1]-1))
        for y in range(start_y-1, start_y+2):
            for x in range(start_x-1, start_x+2):
                tile = world_map[x][y]
                tile.set_terrain(Terrain.Ground)

        return world_map, (start_x, start_y)
    
    def draw_map(self):
        width, height = np.shape(self.world_map)

        map_string = ""

        for y in range(height):
            for x in range(width):
                tile = self.world_map[x][y]
                if self.party.position == (x, y):
                    symbol = "P"
                else:
                    symbol = tile.get_symbol()
                map_string += symbol + " "
            map_string += "\n"

        print(map_string)
