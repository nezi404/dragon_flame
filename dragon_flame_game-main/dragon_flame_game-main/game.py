import pygame
import time
import shield
from controls import *
from config import *
from dragon import *
from shield import *
from powerup import *
import score

pygame.init()
clock = pygame.time.Clock()

# Joystick settings
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

# Draw sprites
Shield.draw_shields(blue_wall, shield_speed, blue_w, initial_bw_x_pos, initial_w_y_pos)
Shield.draw_shields(green_wall, shield_speed, green_w, initial_gw_x_pos, initial_w_y_pos)

Dragon.draw_dragons(blue_dragon, blue_d, initial_bd_x_pos, initial_d_y_pos, dragon_speed, blue_angle)
Dragon.draw_dragons(green_dragon, green_d, initial_gd_x_pos, initial_d_y_pos, dragon_speed, green_angle)

Power.draw(blue_power_up, blue_pu, 100, 100)
Power.draw(green_power_up, green_pu, 550, 100)

# Start screen
start = False
game_pause = False
image_update = pygame.time.get_ticks()
frame = 0

num_green_bullet = 0
num_blue_bullet = 0
green_bullet = False
blue_bullet = False
green_less_bullet = False
blue_less_bullet = False
move_b_power = False
move_g_power = False
cond_g = True
cond_b = True
blue_fireball_group = pygame.sprite.Group()
green_fireball_group = pygame.sprite.Group()


class Game:
    def __init__(self):
        pass

    # Check if an event happens
    @staticmethod
    def check_events():
        global hit_timer, start, game_pause
        clk.tick(60)
        if hit_timer > 0:
            hit_timer -= 1
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if start is True and not game_pause:
                if event.type == pygame.JOYAXISMOTION:
                    joy_axis = event.axis
                    axis_value = event.value
                    player_joy = event.joy
                    Controls.dragons_control_keys(blue_dragon, player_joy, joy_axis, axis_value, 0, 1, 0, 1)
                    Controls.shield_control_keys(blue_wall, player_joy, joy_axis, axis_value, 3, 0, shield_speed)
                    Controls.dragons_control_keys(green_dragon, player_joy, joy_axis, axis_value, 0, 1, 1, 1)
                    Controls.shield_control_keys(green_wall, player_joy, joy_axis, axis_value, 3, 0, shield_speed)

            if event.type == pygame.JOYBUTTONDOWN:
                import screens
                if not game_pause and start:
                    global green_bullet, blue_bullet, move_b_power, move_g_power
                    if event.button == 0 and event.joy == 0 and len(blue_fireball_group) < 6:
                        blue_fire = fireballs.Fireball(blue_fire_ball, blue_dragon, blue_dragon.rect.x,
                                                       blue_dragon.rect.y,
                                                       70,
                                                       30, 5, green_dragon,
                                                       green_wall, blue_wall, b_shield)

                        blue_fireball_group.add(blue_fire)
                        blue_bullet = True
                    if event.button == 0 and event.joy == 0 and len(green_fireball_group) < 6:

                        green_fire = fireballs.Fireball(green_fire_ball, green_dragon, green_dragon.rect.x,
                                                        green_dragon.rect.y, -50, 30, -5,
                                                        blue_dragon, blue_wall, green_wall, g_shield)
                        green_fireball_group.add(green_fire)

                        green_bullet = True

                    if event.button == 2 and event.joy == 0:
                        if blue_score == 3:
                            move_b_power = True

                        if green_score == 3:
                            move_g_power = True

                if event.button == 3:
                    if start:
                        game_pause = not game_pause
                    else:
                        start = True

    def game_loop(self):
        global blue_dragon_dir, green_bullet, blue_bullet, num_green_bullet, \
            num_blue_bullet, blue_fire, green_fire, g_life, b_life, b_shield, g_shield, \
            cont_hit_b_shield, cont_hit_g_shield, g_vulnerable, b_vulnerable, move_power, \
            blue_score, green_score, move_b_power, move_g_power, cond_g

        blue_score = 0
        green_score = 0

        while True:

            dt = clock.tick() / 1000
            self.check_events()
            screen.fill([0, 0, 0])
            current_time = pygame.time.get_ticks()

            if start and game_pause is False:

                self.scor = score.score(blue_colour, green_colour, blue_score, green_score, (600, 45), (775, 45),
                                        b_life, b_shield, g_life, g_shield, (10, 70), (screen_width - 375, 70))
                drawGroup.draw(screen)
                Dragon.dragon_move(green_dragon, dt)
                Dragon.dragon_move(blue_dragon, dt)
                Dragon.upper_wall_collision(blue_dragon, 0)
                Dragon.lower_wall_collision(blue_dragon, 580)
                Dragon.upper_wall_collision(green_dragon, 0)
                Dragon.lower_wall_collision(green_dragon, 580)
                Dragon.right_wall_collision(blue_dragon, initial_gw_x_pos - 150)
                Dragon.left_wall_collision(blue_dragon, 0)
                Dragon.right_wall_collision(green_dragon, 1310)
                Dragon.left_wall_collision(green_dragon, initial_bw_x_pos + 170)

                Shield.shield_move(green_wall, dt)
                Shield.shield_move(blue_wall, dt)
                Shield.upper_wall_collision(blue_wall, 0)
                Shield.lower_wall_collision(blue_wall, 600)
                Shield.upper_wall_collision(green_wall, 0)
                Shield.lower_wall_collision(green_wall, 600)

                blue_fireball_group.draw(screen)
                green_fireball_group.draw(screen)

                pygame.display.flip()

                if move_b_power:
                    drawGroup.add(blue_power_up)
                    Power.move_right(blue_power_up, 8, 2000)

                    if g_shield > 0:
                        g_shield = 0
                        cond_g = False

                    if g_vulnerable == 1 and cond_g is True:
                        Dragon.draw_dragons(green_dragon, vulnerable_gd, 2000, green_dragon.rect.y,
                                            dragon_speed, green_angle)
                        # //////////BLUE WINS

                    if g_shield == 0 and cond_g is True:
                        g_vulnerable = 2
                        Dragon.draw_dragons(green_dragon, vulnerable_gd, green_dragon.rect.x, green_dragon.rect.y,
                                            dragon_speed, green_angle)

                if move_g_power:
                    drawGroup.add(green_power_up)
                    Power.move_left(green_power_up, -8, -900)

                    if b_shield > 0:
                        b_shield = 0
                        cond_b = False

                    if b_vulnerable == 1 and cond_b is True:
                        Dragon.draw_dragons(blue_dragon, vulnerable_bd, 2000, blue_dragon.rect.y,
                                            dragon_speed, blue_angle)
                        # ///////////GREEN WINS

                    if b_shield == 0 and cond_b is True:
                        b_vulnerable = 2
                        Dragon.draw_dragons(blue_dragon, vulnerable_bd, blue_dragon.rect.x, blue_dragon.rect.y,
                                            dragon_speed, blue_angle)

                if green_bullet:
                    if pygame.sprite.spritecollide(blue_dragon, green_fireball_group, True):

                        if green_score <= 3:
                            if b_vulnerable == 1:
                                Dragon.draw_dragons(blue_dragon, vulnerable_bd, 2000, blue_dragon.rect.y,
                                                    dragon_speed, blue_angle)

                                # ////////////////////SCREEN GREEN WINS

                            green_score += 1
                            b_life -= 1
                            b_vulnerable = 1

                            Dragon.draw_dragons(blue_dragon, vulnerable_bd, blue_dragon.rect.x, blue_dragon.rect.y,
                                                dragon_speed, blue_angle)

                        if green_score > 3:
                            if b_vulnerable == 2:
                                Dragon.draw_dragons(blue_dragon, vulnerable_bd, 0, blue_dragon.rect.y,
                                                    dragon_speed, blue_angle)

                                # ////////////////////SCREEN GREEN WINS

                            else:
                                b_vulnerable = 2
                                Dragon.draw_dragons(blue_dragon, vulnerable_bd, blue_dragon.rect.x,
                                                    blue_dragon.rect.y, dragon_speed, blue_angle)

                    if b_shield > 0:
                        if pygame.sprite.spritecollide(blue_wall, green_fireball_group, True):
                            b_shield -= 1

                            if g_vulnerable == 1:
                                cont_hit_b_shield += 1
                                if cont_hit_b_shield == 6:
                                    Dragon.draw_dragons(green_dragon, green_d, green_dragon.rect.x, green_dragon.rect.y,
                                                        dragon_speed, green_angle)
                                    g_vulnerable = 0
                                    cont_hit_b_shield = 0

                    else:
                        drawGroup.remove(blue_wall)

                else:
                    b_vulnerable = 0

                if blue_bullet:
                    if pygame.sprite.spritecollide(green_dragon, blue_fireball_group, True):

                        if blue_score <= 3:
                            if g_vulnerable == 1:
                                Dragon.draw_dragons(green_dragon, vulnerable_gd, 2000, green_dragon.rect.y,
                                                    dragon_speed, green_angle)

                                # ////////////////////SCREEN BLUE WINS

                            blue_score += 1
                            g_life -= 1
                            g_vulnerable = 1

                            Dragon.draw_dragons(green_dragon, vulnerable_gd, green_dragon.rect.x, green_dragon.rect.y,
                                                dragon_speed,
                                                green_angle)

                        if blue_score > 3:
                            if g_vulnerable == 2:
                                Dragon.draw_dragons(green_dragon, vulnerable_gd, 2000, green_dragon.rect.y,
                                                    dragon_speed, green_angle)

                                # ////////////////////SCREEN BLUE WINS

                            else:
                                g_vulnerable = 2
                                Dragon.draw_dragons(green_dragon, vulnerable_gd, green_dragon.rect.x,
                                                    green_dragon.rect.y, dragon_speed, green_angle)

                    if g_shield > 0:
                        if pygame.sprite.spritecollide(green_wall, blue_fireball_group, True):
                            g_shield -= 1

                            if b_vulnerable == 1:
                                cont_hit_g_shield += 1
                                if cont_hit_g_shield == 6:
                                    Dragon.draw_dragons(blue_dragon, blue_d, blue_dragon.rect.x, blue_dragon.rect.y,
                                                        dragon_speed,
                                                        blue_angle)
                                    b_vulnerable = 0
                                    cont_hit_g_shield = 0

                    else:
                        drawGroup.remove(green_wall)

                else:
                    g_vulnerable = 0

                pygame.display.update()
                green_fireball_group.update()
                blue_fireball_group.update()

            else:
                import screens
                import config
                if not start:
                    global image_update, frame
                    if current_time - image_update > config.start_button_cooldown:
                        image_update = current_time
                        screens.start_screen(frame)
                        frame += 1
                        pygame.display.flip()
                        if frame > screens.start_frames:
                            frame = 0

                if game_pause:

                    if current_time - image_update >= config.return_button_cooldown:
                        image_update = current_time
                        screens.game_pause_screen(frame)
                        frame += 1
                        pygame.display.flip()
                        if frame > screens.start_frames:
                            frame = 0
