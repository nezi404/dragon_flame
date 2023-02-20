import game
from config import *


class Shield(pygame.sprite.Sprite):
    def __init__(self):
        pass

    def draw_shields(self, speed, sprite, x, y):

        self.image = pygame.image.load(f"sprites/{sprite}.png")
        self.rect = pygame.Rect(x, y, 0, 0)
        self.pos = (x, y)
        self.size = (50, 50)
        self.speed = speed
        self.image = pygame.transform.scale(self.image, [90, 80])
        self.dir = pygame.math.Vector2()

    def shield_move(self, dt):
        if self.dir.magnitude() > 0:
            self.pos += self.speed * self.dir * dt
        self.rect = pygame.Rect(self.pos, self.size)

    def upper_wall_collision(self, y):
        if self.rect.y < y:
            self.rect.y = y + 2

    def lower_wall_collision(self, y):
        if self.rect.y > y:
            self.rect.y = y - 2
