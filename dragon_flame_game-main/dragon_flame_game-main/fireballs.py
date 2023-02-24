import pygame
import config
import dragon
import game


class Fireball(pygame.sprite.Sprite):
    def __init__(self, sprite, dragon, posx, posy, spriteoffsetx, spriteoffsety, fireball_dir,
                 enemy_pos, enemy_shield, my_shield, shield_value):
        super().__init__()
        self.size = (20, 20)
        self.image = sprite
        self.rect = pygame.Rect(((posx + spriteoffsetx, posy + spriteoffsety), self.size))
        self.enemy_pos = enemy_pos.rect
        self.fireball_dir = fireball_dir
        self.enemy_shield = enemy_shield
        self.my_shield = my_shield
        self.dragon = dragon
        self.shield_value = shield_value

    def update(self):

        self.rect.x += self.fireball_dir

        if self.rect.x > config.screen_width + 100 or self.rect.x < 0:
            self.kill()

        if self.shield_value > 0:
            if self.rect.colliderect(self.my_shield):
                self.kill()

    def kill_bullet(self):
        self.kill()
