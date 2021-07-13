from pygame import *


class Panel:
    def __init__(self, x: int):
        self.x = x
        self.y = 300
        self.surface = Surface((25, 200), SRCALPHA)
        self.hit_box = (self.x, self.y, self.x + 25, self.y + 200)
        draw.rect(self.surface, Color("white"), (0, 0, 25, 200))

    def draw(self):
        self.hit_box = (self.x, self.y, self.x + 25, self.y + 200)
        return self.surface, (self.x, self.y)

    def update(self, movement: str, screenHeight: int):
        match movement:
            case "down":
                self.y += 10
            case "up":
                self.y -= 10

        self.y = max(0, min(self.y, screenHeight - 200))
        draw.rect(self.surface, Color("white"), (0, 0, 25, 200))
