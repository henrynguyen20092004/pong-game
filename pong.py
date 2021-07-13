import pygame
from pygame.locals import *
from random import randint
from math import *
from time import sleep

# Variables
width = 1200
height = 800
panel_speed = 10
ball_speed = 10
wrong_angle = [0, 1, 8, 9, 10, 17, 18, 19, 26, 27, 28, 35]
ball_angle_in_degree = randint(0, 35)
while ball_angle_in_degree in wrong_angle:
    ball_angle_in_degree = randint(0, 35)
ball_angle = ball_angle_in_degree * pi / 18
p1_point = 0
p2_point = 0
reset = False

# Initialize the game and create the window
pygame.init()
white = (255, 255, 255)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')


def reflect(angle, side):
    random_bounce = randint(1, 4)
    if side == 'L':
        if random_bounce in (1, 2):
            angle_in_degree = randint(9, 27)
            while angle_in_degree in wrong_angle:
                angle_in_degree = randint(9, 27)
            return angle_in_degree * pi / 18
        else:
            return -angle + pi
    if side == 'R':
        if random_bounce == 1:
            angle_in_degree = randint(27, 35)
            while angle_in_degree in wrong_angle:
                angle_in_degree = randint(27, 35)
            return angle_in_degree * pi / 18
        elif random_bounce == 2:
            angle_in_degree = randint(0, 9)
            while angle_in_degree in wrong_angle:
                angle_in_degree = randint(0, 9)
            return angle_in_degree * pi / 18
        else:
            return -angle + pi
    elif side in ('U', 'D'):
        return -angle


def collide(hit_box1, hit_box2):
    return hit_box1[0] >= hit_box2[0] and hit_box1[1] >= hit_box2[1] and\
           hit_box1[2] <= hit_box2[2] and hit_box1[3] <= hit_box2[3]


class LeftPanel:
    def __init__(self):
        self.y = 300
        self.surface = pygame.Surface((25, 200), SRCALPHA)
        self.hit_box = (100, self.y, 125, self.y + 200)
        pygame.draw.rect(self.surface, white, (0, 0, 25, 200))

    def draw(self):
        self.hit_box = (100, self.y, 125, self.y + 200)
        screen.blit(self.surface, (100, self.y))

    def update(self, move_up, move_down):
        if move_down:
            self.y += panel_speed
        if move_up:
            self.y -= panel_speed

        if self.y >= height - 200:
            self.y = height - 200
        if self.y <= 0:
            self.y = 0


class RightPanel:
    def __init__(self):
        self.y = 300
        self.surface = pygame.Surface((25, 200), SRCALPHA)
        self.hit_box = (1075, self.y, 1100, self.y + 200)
        pygame.draw.rect(self.surface, white, (0, 0, 25, 200))

    def draw(self):
        self.hit_box = (1075, self.y, 1100, self.y + 200)
        screen.blit(self.surface, (1075, self.y))

    def update(self, move_up, move_down):
        if move_down:
            self.y += panel_speed
        if move_up:
            self.y -= panel_speed

        if self.y >= height - 200:
            self.y = height - 200
        if self.y <= 0:
            self.y = 0


# Create panels
right_panel = RightPanel()
left_panel = LeftPanel()


class Ball:
    def __init__(self):        
        self.radius = 10
        self.x = width / 2
        self.y = height / 2
        self.center = (self.x, self.y)
        self.hit_box = (self.x - self.radius / 2, self.y - self.radius / 2,
                        self.x + self.radius / 2, self.y + self.radius / 2)

    def update(self):
        global ball_angle
        global p1_point
        global p2_point
        global reset
        color = white
        if collide(self.hit_box, left_panel.hit_box):
            ball_angle = reflect(ball_angle, 'R')
        if collide(self.hit_box, right_panel.hit_box):
            ball_angle = reflect(ball_angle, 'L')
        if self.hit_box[1] <= 0:
            ball_angle = reflect(ball_angle, 'D')
        if self.hit_box[3] >= height:
            ball_angle = reflect(ball_angle, 'U')
        if self.hit_box[0] <= 0:
            p2_point += 1
            reset = True
            color = (0, 0, 0)
        if self.hit_box[2] >= width:
            p1_point += 1
            reset = True
            color = (0, 0, 0)
        self.x += cos(ball_angle) * ball_speed
        self.y += sin(ball_angle) * ball_speed
        self.center = (self.x, self.y)
        self.hit_box = (self.x - self.radius / 2, self.y - self.radius / 2,
                        self.x + self.radius / 2, self.y + self.radius / 2)
        pygame.draw.circle(screen, color, self.center, self.radius)


def main():
    # Import global variable
    global p1_point
    global p2_point
    global reset
    global ball_angle
    global ball_speed
    global ball_angle_in_degree

    # FPS
    FPS = 60
    fpsClock = pygame.time.Clock()

    # Create ball and movement variables
    ball = Ball()
    ball_point = 0
    moveUp = [False, False]
    moveDown = [False, False]
    running = True

    # Font
    font = pygame.font.SysFont('consolas', 30)

    # Run
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Detect key pressing
            if event.type == KEYDOWN:
                if event.key == K_w:
                    moveUp[0] = True
                if event.key == K_s:
                    moveDown[0] = True
                if event.key == K_UP:
                    moveUp[1] = True
                if event.key == K_DOWN:
                    moveDown[1] = True
                if event.key == K_ESCAPE:
                    running = False

            # Detect key releasing
            if event.type == KEYUP:
                if event.key == K_w:
                    moveUp[0] = False
                if event.key == K_s:
                    moveDown[0] = False
                if event.key == K_UP:
                    moveUp[1] = False
                if event.key == K_DOWN:
                    moveDown[1] = False

        # Screen update
        screen.fill((0, 0, 0))

        # Point
        point_surface = font.render('Player 1: ' + str(p1_point) + ' Player 2: ' + str(p2_point), True, white)
        screen.blit(point_surface, (0, 0))
        if (p1_point + p2_point + ball_point) / 5 in range(1, 11):
            ball_speed += 1
            ball_point += 1
            if ball_point % 5 == 0:
                ball_point += 1

        # Draw
        right_panel.draw()
        left_panel.draw()

        # Update
        ball.update()
        left_panel.update(moveUp[0], moveDown[0])
        right_panel.update(moveUp[1], moveDown[1])
        pygame.display.update()
        fpsClock.tick(FPS)

        # Create new ball every reset
        if reset:
            ball_angle_in_degree = randint(0, 35)
            while ball_angle_in_degree in wrong_angle:
                ball_angle_in_degree = randint(0, 35)
            ball_angle = ball_angle_in_degree * pi / 18
            ball = Ball()
            ball.update()
            pygame.display.update()
            sleep(0.25)
            reset = False


# Run main()
if __name__ == '__main__':
    main()
    pygame.quit()
