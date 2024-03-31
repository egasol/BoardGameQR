from MapTile import MapTile, Terrain

import random
import numpy as np


class MapGrid:
    def __init__(self, map_size, party):
        self.world_map, self.start = self._generate_map(map_size)
        self.party = party
        party.set_map(self)
        party.set_position(self.start)

    def _generate_map(self, map_size):
        print("generating map...")
        world_map = np.empty(map_size, dtype=object)
        world_map.flat = [MapTile(Terrain.Wall) for _ in world_map.flat]

        padding = 4

        start_x = random.choice(range(padding, map_size[0]-padding))
        start_y = random.choice(range(padding, map_size[1]-padding))
        for y in range(start_y-padding, start_y+padding+1):
            for x in range(start_x-padding, start_x+padding+1):
                tile = world_map[x][y]
                tile.set_terrain(Terrain.Ground)

        event = {
            "name": "A couple of fishermen",
            "enter": "You see two fishermen who are busy trying to catch fish.",
            "status":
            {
                "fishingrod": True,
                "noticed_fishing_rod": False,
            },
            "dialogue":
            {
                "barter":
                {
                    "prerequisite":
                    {
                        "status_name": "fishingrod",
                        True:
                        {
                            "rate": 0.5,
                            "success":
                            {
                                "response": "Here's a fishingrod for you",
                                "status_update":
                                {
                                    "status_name": "fishingrod",
                                    "status_set": False,
                                },
                                "inventory_update":
                                {
                                    "name": "fishingrod",
                                    "amount": 1,
                                }
                            },
                            "failure":
                            {
                                "response": "Go away, you're scaring the fish",
                            }
                        },
                        False:
                        {
                            "success":
                            {
                                "response": "I have nothing to trade you.",
                            }
                        }
                    }
                },
                "perception":
                {
                    "rate": 0.8,
                    "success":
                    {
                        "response": "You notice that the fishermen have an extra fishing rod.",
                        "status_update":
                        {
                            "status_name": "noticed_fishing_rod",
                            "status_set": True,
                        },
                    },
                    "failure":
                    {
                        "response": "You notice nothing out of the ordinary.",
                    }
                }
            }
        }

        world_map[6][6].set_event(event)

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
