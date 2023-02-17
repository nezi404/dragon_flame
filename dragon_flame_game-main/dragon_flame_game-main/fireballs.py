import pygame
import config
import dragon
import game


class Fireball(pygame.sprite.Sprite):
    def __init__(self, posx, posy, spriteoffsetx, spriteoffsety, fireball_dir, enemy_pos, enemy_shield, 
                 num_bullet, bullet_desapear):
        super().__init__()
        self.image = config.fireball_img
        self.rect = self.image.get_rect(center=(posx + spriteoffsetx, posy + spriteoffsety))
        self.enemy_pos = pygame.Rect(enemy_pos)
        self.fireball_dir = fireball_dir
        self.enemy_shield = enemy_shield
        self.num_bullet = num_bullet
        self.less_bullet = bullet_desapear

    @staticmethod
    def add_bullet(bala):
        bala += 1
        return bala

    @staticmethod
    def remove_bullet(bala):
        bala -= 1
        return bala

    def update(self):

        self.rect.x += self.fireball_dir

        if self.rect.x > config.screen_width or self.rect.x < 0:
            self.kill()

        if self.rect.colliderect(self.enemy_pos):

            self.kill()

        if self.rect.colliderect(self.enemy_shield):
            self.kill()
