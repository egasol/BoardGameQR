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
            "scout": functools.partial(self.scout, 2),
            "barter": functools.partial(self.interact, "barter"),
            "perception": functools.partial(self.interact, "perception"),
        }

    def set_position(self, position):
        tile = self.map_grid.world_map[position[0]][position[1]]
        self.position = position

        if tile.event is not None:
            return tile.event["enter"]
        else:
            return None

    def set_map(self, map_grid):
        self.map_grid = map_grid

    def walk(self, direction):
        position_previous = self.position
        position_new = (self.position[0] + direction[0],
                        self.position[1] + direction[1])

        try:
            tile = self.map_grid.world_map[position_new[0]][position_new[1]]

            if tile.is_walkable():
                feedback = self.set_position(position_new)

                if feedback is None:
                    return "You walked to the " + self.map_grid.get_direction(position_previous, position_new)
                else:
                    return feedback
        except:
            return "You can not walk any further."

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
                    event_name = tile.event["name"]
                    text = "You see " + event_name + " to the " + \
                        self.map_grid.get_direction(
                            self.position, (x, y))

                    return text

    def interact(self, interact):
        (px, py) = self.position
        tile = self.map_grid.world_map[px][py]

        if tile.event is not None:
            dialogue = tile.event["dialogue"].get(interact)

            if dialogue is not None:
                # TODO: Add prerequisite loop to enable any number of branches in dialogue.
                prerequisite = dialogue.get("prerequisite")

                # TODO: Add possibility to check status / items of party or player.
                if prerequisite is not None:
                    status = tile.event["status"][prerequisite["status_name"]]
                    dialogue = prerequisite[status]

                success_rate = dialogue.get("rate")

                if success_rate is None:
                    response = dialogue.get("success")
                else:
                    # TODO: Add modifier based on player stats.
                    if 1 > success_rate:
                        response = dialogue.get("success")
                    else:
                        response = dialogue.get("failure")

                status_update = response.get("status_update")
                response_voice = response.get("response")

                if status_update is not None:
                    tile.event["status"][status_update["status_name"]
                                         ] = status_update["status_set"]

                # TODO: Add inventory manipulation based on inventory_update.

                return response_voice
            else:
                return "You can not do that here."
        else:
            return f"You have nothing to {interact} with here."

    def action(self, action):
        if action in self.actions.keys():
            feedback = self.actions[action]()
            return feedback
        else:
            print("Invalid action...", action, "not in", self.actions.keys())
            return None
