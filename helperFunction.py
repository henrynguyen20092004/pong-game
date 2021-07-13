from random import randint
from math import pi


def collide(hit_box1: tuple[float, float, float, float], hit_box2: tuple[int, int, int, int]):
    return (
        hit_box1[0] >= hit_box2[0]
        and hit_box1[1] >= hit_box2[1]
        and hit_box1[2] <= hit_box2[2]
        and hit_box1[3] <= hit_box2[3]
    )


def getRandomAngle(lower: int, higher: int):
    initial_degree = 0
    while 75 <= initial_degree % 90 or initial_degree % 90 <= 15:
        initial_degree = randint(lower, higher)
    return initial_degree * pi / 180


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
