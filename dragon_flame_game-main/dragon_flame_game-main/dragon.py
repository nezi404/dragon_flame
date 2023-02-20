import pygame
import math
from config import *
import fireballs
import game


class Dragon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def draw_dragons(self, sprite, x, y, speed, ang):
        self.pos = (x, y)
        self.size = (70, 50)
        self.speed = speed
        self.dir = pygame.math.Vector2()
        self.image = pygame.image.load(f"sprites/{sprite}.png")
        self.rect = pygame.Rect((self.pos), self.size)
        self.image = pygame.transform.scale(self.image, [90, 70])
        self.image = pygame.transform.rotate(self.image, ang)
        self.score = 0

    def dragon_move(self, dt):
        if self.dir.magnitude() > 0:
            self.pos += self.speed * self.dir * dt
        self.rect = pygame.Rect(self.pos, self.size)

    def upper_wall_collision(self, y):
        if self.rect.y < y:
            self.rect.y = y + 2

    def lower_wall_collision(self, y):
        if self.rect.y > y:
            self.rect.y = y - 2

    def left_wall_collision(self, x):
        if self.rect.x < x:
            self.rect.x = x + 2

    def right_wall_collision(self, x):
        if self.rect.x > x:
            self.rect.x = x - 2


