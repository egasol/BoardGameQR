from MapTile import MapTile, Terrain

import numpy as np
import json
from pathlib import Path


class MapGrid:
    def __init__(self, map_size, party):
        self.world_map, self.start = self._generate_map(
            Path("SavedMaps/Tutorial"))
        self.party = party
        party.set_map(self)
        party.set_position(self.start)

    def _generate_map(self, map_path):
        map_file = map_path / Path("map.json")

        with open(map_file, "r") as f:
            map_saved = json.load(f)

        map_size = (map_saved["map_size"][0], map_saved["map_size"][1])
        map_grid = map_saved["map_grid"]
        map_start = (map_saved["start_point"][0], map_saved["start_point"][1])
        map_events = map_saved["events"]

        world_map = np.empty(map_size, dtype=object)
        world_map.flat = [MapTile(Terrain.Wall) for _ in world_map.flat]

        for y in range(world_map.shape[1]):
            for x in range(world_map.shape[0]):
                tile = world_map[x][y]
                tile.set_terrain(Terrain(int(map_grid[y][x])))

        for map_event in map_events:
            event_location_x = map_event["x"],
            event_location_y = map_event["y"],
            event_filepath = map_path / Path(map_event["file"])

            with open(event_filepath, "r") as f:
                event = json.load(f)

            world_map[event_location_x][event_location_y].set_event(event)

        return world_map, map_start

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

    def get_direction(self, position_from, position_to):
        (x_from, y_from) = position_from
        (x_to, y_to) = position_to

        direction = ""

        if y_to > y_from:
            direction += "south"
        if y_to < y_from:
            direction += "north"
        if x_to > x_from:
            direction += "east"
        if x_to < x_from:
            direction += "west"

        return direction
