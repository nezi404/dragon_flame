import pygame
import time
import shield
from controls import *
from config import *
from dragon import *
from shield import *

pygame.init()
clock = pygame.time.Clock()

# Joystick settings
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

# Draw sprites
Dragon.draw_dragons(blue_dragon, blue_d, initial_bd_x_pos, initial_d_y_pos, dragon_speed, blue_angle)
Dragon.draw_dragons(green_dragon, green_d, initial_gd_x_pos, initial_d_y_pos, dragon_speed, green_angle)
Shield.draw_shields(blue_wall, shield_speed, blue_w, initial_bw_x_pos, initial_w_y_pos)
Shield.draw_shields(green_wall, shield_speed, green_w, initial_gw_x_pos, initial_w_y_pos)

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
fireball_group = pygame.sprite.Group()


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
                    Controls.shield_control_keys(green_wall, player_joy, joy_axis, axis_value, 3, 1, shield_speed)

            if event.type == pygame.JOYBUTTONDOWN:
                import screens
                if not game_pause and start:
                    global green_bullet, blue_bullet
                    if event.button == 0 and event.joy == 0 and not blue_less_bullet:
                        blue_bullet = True
                    if event.button == 0 and event.joy == 1 and not green_less_bullet:
                        green_bullet = True
                if event.button == 3:
                    if start:
                        game_pause = not game_pause
                    else:
                        start = True

    def game_loop(self):
        global blue_dragon_dir, green_bullet, blue_bullet, num_green_bullet, \
            num_blue_bullet, blue_less_bullet, green_less_bullet
        while True:

            dt = clock.tick() / 1000
            self.check_events()
            screen.fill([0, 0, 0])
            current_time = pygame.time.get_ticks()

            if start and game_pause is False:

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

                fireball_group.draw(screen)

                pygame.display.flip()

                if green_bullet:
                    global num_green_bullet
                    blue_dragon_dir = blue_dragon.dir
                    green_bullet = not green_bullet
                    num_green_bullet = fireballs.Fireball.add_bullet(num_green_bullet)
                    fireball_group.add(dragon.Dragon.green_blow_fireball())

                if blue_bullet:
                    global num_blue_bullet
                    blue_dragon_dir = blue_dragon.dir
                    blue_bullet = not blue_bullet
                    fireball_group.add(dragon.Dragon.blue_blow_fireball())
                    num_blue_bullet = fireballs.Fireball.add_bullet(num_blue_bullet)

                pygame.display.update()
                fireball_group.update()

            else:
                import screens
                import config
                if not start:
                    global image_update, frame
                    if current_time - image_update >= config.start_button_cooldown:
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
