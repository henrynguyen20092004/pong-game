from random import randint
from math import pi


def getRandomAngle(lower: int, higher: int):
    initial_degree = 0
    while 75 <= initial_degree % 90 or initial_degree % 90 <= 15:
        initial_degree = randint(lower, higher)
    return initial_degree * pi / 180
