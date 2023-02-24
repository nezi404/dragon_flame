import pygame
import math
from config import *
import game


class Power(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def draw(self, sprite, x, y):
        self.pos = (x, y)
        self.size = (70, 50)
        self.image = pygame.image.load(f"sprites/{sprite}.png")
        self.rect = pygame.Rect(self.pos, self.size)
        self.image = pygame.transform.scale(self.image, [790, 770])

    def move_right(self, p, q):

        self.rect.x += p

        if self.rect.x > q:
            self.rect.x = q

    def move_left(self, p, q):

        self.rect.x += p

        if self.rect.x < q:
            self.rect.x = q
