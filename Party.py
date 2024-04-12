import functools
from random import random, choice


class Party:
    def __init__(self):
        self.position = None
        self.map_grid = None
        self.hp = 10
        self.inventory = {
            "gold": 12,
        }

        self.actions = {
            "north": functools.partial(self.walk, (0, -1)),
            "south": functools.partial(self.walk, (0, 1)),
            "east": functools.partial(self.walk, (1, 0)),
            "west": functools.partial(self.walk, (-1, 0)),
            "long north": functools.partial(self.walk, (0, -3)),
            "long south": functools.partial(self.walk, (0, 3)),
            "long east": functools.partial(self.walk, (3, 0)),
            "long west": functools.partial(self.walk, (-3, 0)),
            "scout": functools.partial(self.scout, 2),
            "barter": functools.partial(self.interact, "barter"),
            "perception": functools.partial(self.interact, "perception"),
            "threaten": functools.partial(self.interact, "threaten"),
            "collect": functools.partial(self.interact, "collect"),
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

            if tile.is_walkable:
                feedback = self.set_position(position_new)
                direction = self.map_grid.get_direction(position_previous, position_new)

                if feedback is None:
                    return "You " + choice(["walk", "traverse", "travel", "venture"]) + " to the " + direction
                else:
                    return feedback
            else:
                return "The way ahead is blocked by " + tile.name
        except:
            return "You can not walk any further."

    def scout(self, area):
        (px, py) = self.position

        x_from = max(px - area, 0)
        x_to = min(px + area + 1, self.map_grid.world_map.shape[0] - 1)
        y_from = max(py - area, 0)
        y_to = min(py + area + 1, self.map_grid.world_map.shape[1] - 1)

        scout_list = []

        for y in range(y_from, y_to):
            for x in range(x_from, x_to):
                tile = self.map_grid.world_map[x][y]
                if tile.event is not None:
                    event_name = tile.event["name"]
                    text = "You see " + event_name + " to the " + \
                        self.map_grid.get_direction(
                            self.position, (x, y))

                    scout_list.append(text)

        if len(scout_list) > 0:
            return choice(scout_list)
        else:
            return "You see nothing of interest."

    def interact(self, interact):
        (px, py) = self.position
        tile = self.map_grid.world_map[px][py]

        if tile.event is not None:
            interaction = tile.event["interaction"].get(interact)

            if interaction is not None:
                while True:
                    prerequisite = interaction.get("prerequisite")

                    if prerequisite is not None:
                        status_event = prerequisite.get("status_name")
                        status_party = prerequisite.get("item")

                        if status_event is not None:
                            status = tile.event["status"][status_event]
                        elif status_party is not None:
                            status_amount = prerequisite["amount"]
                            party_amount = self.inventory.get(status_party)
                            if party_amount is not None:
                                status = party_amount >= status_amount
                            else:
                                status = False
                        status_string = "true" if status == True else "false"  # TODO: Fix this, ugly af
                        interaction = prerequisite[status_string]
                    else:
                        break

                success_rate = interaction.get("rate")

                if success_rate is None:
                    response = interaction.get("success")
                else:
                    # TODO: Add modifier based on player stats.
                    # TODO: Consume card during rolls
                    roll = random()
                    if roll > success_rate:
                        print(
                            f"{interact} roll succeded! ({roll:.2f} > {success_rate:.2f})")
                        response = interaction.get("success")
                    else:
                        print(
                            f"{interact} roll failed! ({roll:.2f} < {success_rate:.2f})")
                        response = interaction.get("failure")

                status_update = response.get("status_update")
                inventory_update = response.get("inventory_update")
                dialogue = response.get("dialogue")

                if isinstance(dialogue, list):
                    dialogue = choice(dialogue)

                if status_update is not None:
                    status_name = status_update["status_name"]
                    status_value = status_update["status_set"]

                    tile.event["status"][status_name] = status_value

                if inventory_update is not None:
                    for item in inventory_update:
                        item_name = item["name"]
                        item_amount = item["amount"]
                        if item["name"] in self.inventory:
                            self.inventory[item_name] += item_amount
                        else:
                            self.inventory[item_name] = item_amount

                    print(self.inventory)

                return dialogue
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
