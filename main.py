import pygame

import pygame.locals as pyGameLocal

from math import *
from Components import *

from Helper.GetRandomAngle import getRandomAngle


pygame.init()
pygame.display.set_caption("Pong")

screenSize = (1400, 800)
color = (255, 255, 255)
right_panel = Panel(1275)
left_panel = Panel(100)


def main():
    fpsClock = pygame.time.Clock()
    ball = Ball(screenSize)
    ball_speed = 10
    ball_point = 0
    ball_angle = getRandomAngle(0, 360)
    movement = ["", ""]
    screen = pygame.display.set_mode(screenSize)
    points = [0, 0]
    reset = False
    running = True
    font = pygame.font.SysFont("consolas", 30)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pyGameLocal.KEYDOWN:
                match event.key:
                    case pyGameLocal.K_w:
                        movement[0] = "up"
                    case pyGameLocal.K_s:
                        movement[0] = "down"
                    case pyGameLocal.K_UP:
                        movement[1] = "up"
                    case pyGameLocal.K_DOWN:
                        movement[1] = "down"
                    case pyGameLocal.K_ESCAPE:
                        running = False

            if event.type == pyGameLocal.KEYUP:
                match event.key:
                    case pyGameLocal.K_w:
                        movement[0] = ""
                    case pyGameLocal.K_s:
                        movement[0] = ""
                    case pyGameLocal.K_UP:
                        movement[1] = ""
                    case pyGameLocal.K_DOWN:
                        movement[1] = ""

        screen.fill((0, 0, 0))

        point_surface = font.render(
            "Player 1: " + str(points[0]) + " Player 2: " + str(points[1]),
            True,
            (0, 255, 0),
        )
        screen.blit(point_surface, (0, 0))
        if (sum(points) + ball_point) / 5 in range(1, 100):
            ball_speed += 1
            ball_point += 1
            if ball_point % 5 == 0:
                ball_point += 1

        screen.blit(right_panel.draw()[0], right_panel.draw()[1])
        screen.blit(left_panel.draw()[0], left_panel.draw()[1])
        pygame.draw.circle(screen, color, ball.draw()[0], ball.draw()[1])

        fpsClock.tick(60)
        ball_angle = ball.updateAngle([left_panel, right_panel], ball_speed, ball_angle)
        points, reset = ball.updatePoint(points, reset)
        left_panel.update(movement[0], screenSize[1])
        right_panel.update(movement[1], screenSize[1])
        pygame.display.update()

        if reset:
            reset = False
            ball = Ball(screenSize)
            ball_angle = getRandomAngle(0, 360)
            pygame.draw.circle(screen, color, ball.draw()[0], ball.draw()[1])
            pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
