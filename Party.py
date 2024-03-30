import functools


class Party:
    def __init__(self):
        self.position = None
        self.map_grid = None
        self.hp = 10

        self.actions = {
            "north": functools.partial(self.walk, (0, -1)),
            "south": functools.partial(self.walk, (0, 1)),
            "east": functools.partial(self.walk, (1, 0)),
            "west": functools.partial(self.walk, (-1, 0)),
            "scout": functools.partial(self.scout, 2)
        }

    def set_position(self, position):
        tile = self.map_grid.world_map[position[0]][position[1]]

        if tile.event == True:
            print("Event triggered!")

        self.position = position

    def set_map(self, map_grid):
        self.map_grid = map_grid

    def walk(self, direction):
        new_position = (self.position[0] + direction[0],
                        self.position[1] + direction[1])

        try:
            tile = self.map_grid.world_map[new_position[0]][new_position[1]]

            if tile.is_walkable():
                self.set_position(new_position)
        except:
            print("Map border...")

    def scout(self, area):
        (px, py) = self.position

        x_from = max(px - area, 0)
        x_to = min(px + area + 1, self.map_grid.world_map.shape[0] - 1)
        y_from = max(py - area, 0)
        y_to = min(py + area + 1, self.map_grid.world_map.shape[1] - 1)

        for y in range(y_from, y_to):
            for x in range(x_from, x_to):
                tile = self.map_grid.world_map[x][y]
                if tile.event is not None:
                    text = "Event detected to the "
                    if y > py:
                        text += "south"
                    if y < py:
                        text += "north"
                    if x > px:
                        text += "east"
                    if x < px:
                        text += "west"
                    print(text)

    def action(self, action):
        if action in self.actions.keys():
            self.actions[action]()
            return True
        else:
            print("Invalid action...", action, "not in", self.actions.keys())
            return False
