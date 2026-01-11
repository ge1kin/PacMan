class Coin:
    def __init__(self, center_x: str, center_y: str, value: str):
        if not center_x.isdigit():
            print("center x must be an integer number!")
        if not center_y.isdigit():
            print("center y must be an integer number!")
        self.center_x = int(center_x)
        self.center_y = int(center_y)
        if not value.isdigit():
            self.value: int = 10
        else:
            self.value: int = int(value)


class Character:
    def __init__(self, center_x: str, center_y: str, speed: str):
        if not center_x.isdigit():
            print("center x must be an integer number!")
        if not center_y.isdigit():
            print("center y must be an integer number!")
        if not speed.isdigit():
            print("speed must be an integer number!")
        self.center_x: int = int(center_x)
        self.center_y: int = int(center_y)
        self.speed: int = int(speed)
        self.change_x: int = 0
        self.change_y: int = 0