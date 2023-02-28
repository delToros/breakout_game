from turtle import Turtle
import math
import random

# Basic Sprite Class
class Sprite():
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.dx = 0
        self.dy = 0

    def render(self, pen):
        pen.penup()
        pen.goto(self.x, self.y)
        pen.shape(self.image)
        pen.stamp()


# Player class
class Player(Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height, image)
        self.lives = 3
        self.score = 0

    def move_left(self):
        if self.x >= -180:
            self.x -= self.dx

    def move_right(self):
        if self.x <= 180:
            self.x += self.dx

    def reset(self):
        self.x = 0
        self.y = -400
        self.lives -= 1

    def get_cor(self):
        self.border_lower = math.fabs((self.y - (self.height / 2)))
        self.border_higher = math.fabs((self.y + (self.height / 2)))
        self.border_right = math.fabs((self.x + (self.width / 2)))
        self.border_left = math.fabs((self.x - (self.width / 2)))


# Ball class
class Ball(Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height, image)
        self.dx = 0
        self.dy = 0
        self.ab = ''

    def get_cor(self):
        self.border_lower = math.fabs((self.y - (self.height / 2)))
        self.border_higher = math.fabs((self.y + (self.height / 2)))
        self.border_right = math.fabs((self.x + (self.width / 2)))
        self.border_left = math.fabs((self.x - (self.width / 2)))


    def move_right(self):
        self.x += self.dx
        self.y += self.dy

    def move_left(self):
        self.x -= self.dx
        self.y += self.dy

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def reset(self):
        self.x = 0
        self.y = -381
        self.dx = 0
        self.dy = 0
        self.ab = ''

    def is_aabb_collision(self, other):
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        return (y_collision and x_collision)

    def n_gen(self): # Generate random number to determine where ball will go upon start and set move speed
        self.ab = random.randint(1, 2)
        self.dx = 1
        self.dy = 1


# Block Class
class Block(Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height, image)
        #
        self.border_lower = math.fabs((self.y - (self.height / 2)))
        self.border_higher = math.fabs((self.y + (self.height / 2)))
        self.border_right = math.fabs((self.x + (self.width / 2)))
        self.border_left = math.fabs((self.x - (self.width / 2)))
        #

    def del_block(self, pen):
        pen.clear()
