import functools


class Party:
    def __init__(self):
        self.position = None
        self.world = None
        self.hp = 10

        self.actions = {
            "north": functools.partial(self.walk, (0, -1)),
            "south": functools.partial(self.walk, (0, 1)),
            "east": functools.partial(self.walk, (1, 0)),
            "west": functools.partial(self.walk, (-1, 0))
        }
    
    def set_position(self, position):
        self.position = position
    
    def set_map(self, map_grid):
        self.map_grid = map_grid
    
    def walk(self, direction):
        new_position = (self.position[0] + direction[0], self.position[1] + direction[1])

        tile = self.map_grid.world_map[new_position[0]][new_position[1]]

        if tile.is_walkable():
            self.set_position(new_position)
    
    def action(self, action):
        if action in self.actions.keys():
            self.actions[action]()
            return True
        else:
            print("Invalid action...", action, "not in", self.actions.keys())
            return False
