import random


class Coin:
    def __init__(self, center_x: int, center_y: int):
        self.center_x: int = center_x # the x placement of the Coin
        self.center_y: int = center_y # the y placement of the coin
        self.value: int = 10 # the value of the coin


class Character:
    def __init__(self, center_x: int, center_y: int):
        self.center_x: int = center_x # the x placement of the character
        self.center_y: int = center_y # the y placement of the character
        self.change_x: int = 0 # the change of the x placement
        self.change_y: int = 0 # the change of the y placement
        self.speed: int = 1 # the speed of the character


class Player(Character):
    def __init__(self, center_x: int, center_y: int):
        super().__init__(center_x, center_y)
        self.score: int = 0 # the score of the player
        self.lives: int = 3 # the amount of lives of the player

    def move(self) -> None:
        """
        moves the player in the chosen direction
        :return: None
        """
        self.center_x = self.change_x * self.speed
        self.center_y = self.change_y * self.speed


class Enemy(Character):
    def __init__(self, center_x: int, center_y: int):
        super().__init__(center_x, center_y)
        self.time_to_change_direction: float = 0


    def pick_new_direction(self) -> None:
        """
        picks a new direction for the enemy and moves it in that direction
        :return: None
        """
        move_option_lst: list = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]
        move_chosen: tuple = move_option_lst[random.randint(0, 4)]
        self.change_x, self.change_y = move_chosen[1], move_chosen[0]
        self.time_to_change_direction = random.uniform(0.3, 1.0)

    def update(self, delta_time: float = 1/60) -> None:
        """
        makes the timer until the enemy moves again
        :param delta_time: the change in time until the enemy moves
        :return: None
        """
        while delta_time > 0:
            delta_time -= 0.001
        self.center_x = self.change_x * self.speed
        self.center_y = self.change_y * self.speed


class Wall:
    def __init__(self, center_x: int, center_y: int):
        self.center_x: int = center_x # the x placement of the Wall
        self.center_y: int = center_y # the y placement of the Wall