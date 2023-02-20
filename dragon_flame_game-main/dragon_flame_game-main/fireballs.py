import pygame
import config
import dragon
import game


class Fireball(pygame.sprite.Sprite):
    def __init__(self, dragon, posx, posy, spriteoffsetx, spriteoffsety, fireball_dir, enemy_pos, enemy_shield, my_shield,):
        super().__init__()
        self.size = (20, 20)
        self.image = config.fireball_img
        self.rect = pygame.Rect(((posx + spriteoffsetx, posy + spriteoffsety), self.size))
        self.enemy_pos = enemy_pos.rect
        self.fireball_dir = fireball_dir
        self.enemy_shield = enemy_shield
        self.my_shield = my_shield
        self.dragon = dragon






    def update(self):

        self.rect.x += self.fireball_dir

        if self.rect.x > config.screen_width + 100 or self.rect.x < 0:
            self.kill()

        #elif self.rect.colliderect(self.enemy_pos):
         #   self.kill()
          #  self.num_bullet.add(self)

        #elif self.rect.colliderect(self.enemy_shield):
         #   self.kill()

        elif self.rect.colliderect(self.my_shield):
            self.kill()


    def kill_bullet(self):
        self.kill()









