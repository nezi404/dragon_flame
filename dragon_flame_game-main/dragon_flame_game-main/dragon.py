import pygame
import math
from config import *
import fireballs
import game


class Dragon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score = 0

    def draw_dragons(self, sprite, x, y, speed, ang):
        self.pos = (x, y)
        self.size = (90, 70)
        self.speed = speed
        self.dir = pygame.math.Vector2()
        self.image = pygame.image.load(f"sprites/{sprite}.png")
        self.rect = pygame.Rect(self.pos, self.size)
        self.image = pygame.transform.scale(self.image, [90, 70])
        self.image = pygame.transform.rotate(self.image, ang)
        self.score = 0

    def dragon_move(self, dt):
        if self.dir.magnitude() > 0:
            self.pos += self.speed * self.dir * dt
        self.rect = pygame.Rect(self.pos, self.size)

    @staticmethod
    def blue_blow_fireball():
        blue_fire = fireballs.Fireball(game.blue_dragon.rect.x, game.blue_dragon.rect.y, 65, 30, 5, game.green_dragon, game.green_wall, game.num_blue_bullet, game.blue_less_bullet)
        return blue_fire
    @staticmethod
    def green_blow_fireball():
        green_fire = fireballs.Fireball(game.green_dragon.rect.x, game.green_dragon.rect.y, -50, 30, -5, game.blue_dragon, game.blue_wall, game.num_green_bullet, game.green_less_bullet)
        return green_fire