import pygame
import time

import controlers
import dragon
from config import *
from dragon import *
import shield
pygame.init()
clock = pygame.time.Clock()

# Joystick settings
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

# Draw sprites
Dragon.draw_dragons(blue_dragon, blue_d, initial_bd_x_pos, initial_d_y_pos, dragon_speed, blue_angle)
Dragon.draw_dragons(green_dragon, green_d, initial_gd_x_pos, initial_d_y_pos, dragon_speed, green_angle)
shield.Shield.draw_shields(blue_wall, shield_speed, blue_w, initial_bw_x_pos, initial_w_y_pos)
shield.Shield.draw_shields(green_wall, shield_speed, green_w, initial_gw_x_pos,  initial_w_y_pos)

# Start screen
start = False
game_pause = False
image_update = pygame.time.get_ticks()
frame = 0
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

            if start == True and not game_pause:
                if event.type == pygame.JOYAXISMOTION :
                    joy_axis = event.axis
                    axis_value = event.value
                    player_joy = event.joy
                    controlers.Controllers.dragons_control_keys(blue_dragon, player_joy, joy_axis, axis_value, 0, 1, 0)
                    controlers.Controllers.shield_control_keys(blue_wall, player_joy, joy_axis, axis_value, 3, 0)
                    controlers.Controllers.dragons_control_keys(green_dragon, player_joy, joy_axis, axis_value, 0, 1, 1)
                    controlers.Controllers.shield_control_keys(green_wall, player_joy, joy_axis, axis_value, 3, 1)
                    
            if event.type == pygame.JOYBUTTONDOWN:
                import screens
                if event.button == 3 :
                    if start :
                        game_pause = not game_pause
                    else:
                        start = True




    def game_loop(self):

        while True:

            dt = clock.tick() / 1000
            self.check_events()
            screen.fill([0, 0, 0])
            current_time =pygame.time.get_ticks()

            if start and game_pause == False:
                drawGroup.draw(screen)
                Dragon.dragon_move(green_dragon, dt)
                Dragon.dragon_move(blue_dragon, dt)

                Dragon.dragon_move(green_wall, dt)
                Dragon.dragon_move(blue_wall, dt)
                pygame.display.flip()

            else:
                import screens, config
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







