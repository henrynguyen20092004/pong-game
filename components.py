import pygame
from math import sin, cos
from pygame.locals import SRCALPHA

from helperFunction import reflect, collide

color = (255, 255, 255)


class Panel:
    def __init__(self, x: int):
        self.x = x
        self.y = 300
        self.surface = pygame.Surface((25, 200), SRCALPHA)
        self.hit_box = (self.x, self.y, self.x + 25, self.y + 200)
        pygame.draw.rect(self.surface, color, (0, 0, 25, 200))

    def draw(self):
        self.hit_box = (self.x, self.y, self.x + 25, self.y + 200)
        return self.surface, (self.x, self.y)

    def update(self, movement: str, screenHeight: int):
        match movement:
            case "down":
                self.y += 10
            case "up":
                self.y -= 10
        if self.y >= screenHeight - 200:
            self.y = screenHeight - 200
        if self.y <= 0:
            self.y = 0

        pygame.draw.rect(self.surface, color, (0, 0, 25, 200))


class Ball:
    def __init__(self, screen: tuple[float, float]):
        self.radius = 10
        self.color = color
        (self.screenWidth, self.screenHeight) = screen
        self.x = self.screenWidth / 2
        self.y = self.screenHeight / 2
        self.hit_box = (
            self.x - self.radius / 2,
            self.y - self.radius / 2,
            self.x + self.radius / 2,
            self.y + self.radius / 2,
        )

    def draw(self):
        return (self.x, self.y), self.radius

    def updateAngle(self, panels: list[Panel, Panel], ball_speed: int, ball_angle: float):
        if collide(self.hit_box, panels[0].hit_box):
            ball_angle = reflect(ball_angle, "R")
        if collide(self.hit_box, panels[1].hit_box):
            ball_angle = reflect(ball_angle, "L")

        if self.hit_box[1] <= 0:
            ball_angle = reflect(ball_angle, "D")
        if self.hit_box[3] >= self.screenHeight:
            ball_angle = reflect(ball_angle, "U")

        self.x += cos(ball_angle) * ball_speed
        self.y += sin(ball_angle) * ball_speed
        self.hit_box = (
            self.x - self.radius / 2,
            self.y - self.radius / 2,
            self.x + self.radius / 2,
            self.y + self.radius / 2,
        )

        return ball_angle

    def updatePoint(self, points: list[int, int], reset: bool):
        if self.hit_box[2] <= 0:
            points[1] += 1
            reset = True
            self.color = (0, 0, 0)
        if self.hit_box[0] >= self.screenWidth:
            points[0] += 1
            reset = True
            self.color = (0, 0, 0)

        return (points, reset)
