from random import randint
from math import pi

from .GetRandomAngle import getRandomAngle


def reflect(angle: float, side: str):
    random_bounce = randint(1, 4)
    match side:
        case "L":
            if random_bounce in (1, 2):
                return getRandomAngle(90, 270)
            return -angle + pi
        case "R":
            if random_bounce == 1:
                return getRandomAngle(270, 360)
            if random_bounce == 2:
                return getRandomAngle(0, 90)
            return -angle + pi
        case _:
            return -angle
