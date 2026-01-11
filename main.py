import random


class Coin:
    def __init__(self, center_x: int, center_y: int):
        self.center_x = center_x
        self.center_y = center_y
        self.value = 10
        self.change_x: int = 0
        self.change_y: int  = 0


class Character:
    def __init__(self, center_x: int, center_y: int, speed: int):
        self.center_x: int = center_x
        self.center_y: int = center_y
        self.speed: int = int(speed)
        self.change_x: int = 0
        self.change_y: int = 0


class Player(Character):
    def __init__(self, center_x: int, center_y: int, speed: int):
        super().__init__(center_x, center_y, speed)
        self.score: int = 0
        self.lives: int = 3

    def move(self) -> None:
        self.center_x = self.change_x * self.speed
        self.center_y = self.change_y * self.speed


class Enemy(Character):
    def __init__(self, center_x: int, center_y: int, speed: int):
        super().__init__(center_x, center_y, speed)
        self.time_to_change_direction: float = 0


    def pick_new_direction(self) -> None:
        move_option_lst: list = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]
        move_chosen: tuple = move_option_lst[random.randint(0, 4)]
        self.change_x, self.change_y = move_chosen[1], move_chosen[0]
        self.time_to_change_direction = random.uniform(0.3, 1.0)

    def update(self, delta_time: float = 1/60):
        while delta_time > 0:
            delta_time -= 0.001
        self.center_x = self.change_x * self.speed
        self.center_y = self.change_y * self.speed
        self.center_y = self.change_y * self.speed


class Wall:
    def __init__(self, center_x: int, center_y: int):
        self.center_x: int = center_x
        self.center_y: int = center_y