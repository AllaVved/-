# 1. Найти и исправить 3 бага в созданной игре.
#   1. Хомячки не генерируются на месте игока: hamsters.py 2, 7, 18 строки
#   2. Игрок не реагирует на убитых хомячков: 73 строка
#   3. При убийстве всех хомячков heppy end: 88 строка

from player import Player
from hamsters import Hamster

hamsters_count = 4


class Game:
    happy_message = "WOW!!!!! You won!!!"
    map = """****\n****\n****\n****"""
    gameon = True

    def __init__(self):
        self.player = Player()
        self.hamsters = []
        for i in range(hamsters_count):
            self.hamsters.append(Hamster(i + 1, self.get_full_map()))

    def add_point(self, position, name, s):
        li = s.split("\n")
        row = li[position[1]]
        row = row[:position[0]] + name + row[position[0] + 1:]
        li[position[1]] = row
        return "\n".join(li)

    def render_map(self):
        s = self.map
        s = self.add_point(self.player.position, "X", s)
        for h in self.hamsters:
            if h.health > 0:
                s = self.add_point(h.position, str(h.id), s)
        print(s)

    def move_player(self, destination):
        """ destination = w,a,s,d """
        if destination == "s":
            if self.player.position[1] == len(self.map.split("\n")) - 1:
                return False
            self.player.position[1] += 1
        if destination == "w":
            if self.player.position[1] == 0:
                return False
            self.player.position[1] -= 1
        if destination == "a":
            if self.player.position[0] == 0:
                return False
            self.player.position[0] -= 1
        if destination == "d":
            if self.player.position[0] == len(self.map.split("\n")[0]) - 1:
                return False
            self.player.position[0] += 1
        self.on_move(destination)

    def get_full_map(self):
        s = self.map
        for h in self.hamsters:
            s = self.add_point(h.position, str(h.id), s)
        return s

    def get_hamster_on_position(self, coords):
        s = self.get_full_map()
        return s.split("\n")[coords[1]][coords[0]]

    directions = {"w": "s", "s": "w", "a": "d", "d": "a"}

    def on_move(self, direction):
        hamster = self.get_hamster_on_position(self.player.position)
        if not hamster == "*":
            if self.hamsters[int(hamster) - 1].health > 0:
                self.player.was_hit(int(hamster))
                if self.player.health <= 0:
                    print("game over... sorry!")
                    self.gameon = False
                print("player's health: ", self.player.health)
                killed = self.hamsters[int(hamster) - 1].on_shot()
                if not killed:
                    self.move_player(self.directions[direction])
                else:
                    print(self.hamsters[int(hamster) - 1].id, "was killed ")

    def start(self):
        game.render_map()
        while self.gameon:
            if all(i.health <= 0 for i in self.hamsters):
                print(self.happy_message)
                return True
            command = input("Insert command: ")
            if command in ["s", "w", "a", "d"]:
                self.move_player(command)
                self.render_map()
            if command == "e":
                self.player.wait()
            if command == "q":
                self.gameon = False


game = Game()

game.start()

"""

"""
