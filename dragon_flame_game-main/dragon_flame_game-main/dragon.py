import pygame
import math
from config import *


class Dragon(pygame.sprite.Sprite):
    def __init__(self):
        pass

    def draw_dragons(self, sprite, x, y, speed, ang):
        self.pos = (x, y)
        self.size = (0, 0)
        self.speed = speed
        self.dir = pygame.math.Vector2()
        self.image = pygame.image.load(f"sprites/{sprite}.png")
        self.rect = pygame.Rect(self.pos, self.size)
        self.image = pygame.transform.scale(self.image, [90, 70])
        self.image = pygame.transform.rotate(self.image, ang)

    def dragon_move(self, dt):
        if self.dir.magnitude() > 0:
            self.pos += self.speed * self.dir * dt
        self.rect = pygame.Rect(self.pos, self.size)
