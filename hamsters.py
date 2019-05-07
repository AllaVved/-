from random import randint, choice
from player import Player


class Hamster:
    def __init__(self, hid, map):
        self.player = Player()
        self.id = hid
        self.health = 2
        self.position = self.get_clear_position(map)

    def get_clear_position(self, map):
        map_width = len(map.split("\n")[0])
        map_height = len(map.split("\n"))
        while True:
            coords = [randint(0, map_width - 1), randint(0, map_height - 1)]
            if map.split("\n")[coords[1]][coords[0]] == "*":
                if self.player.position != coords:
                    return coords

    def on_shot(self):
        self.health -= 1
        return self.health == 0
