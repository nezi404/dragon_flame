import random
from controls import *
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
image_update_random = image_update
random_x = random.randint(10, 1360)

frame = 0
frame_background = 0

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
                    Controls.dragons_control_keys(blue_dragon, player_joy, joy_axis, axis_value, 0, 1, 1, 1)
                    Controls.shield_control_keys(blue_wall, player_joy, joy_axis, axis_value, 3, 1, shield_speed)
                    Controls.dragons_control_keys(green_dragon, player_joy, joy_axis, axis_value, 0, 1, 0, 1)
                    Controls.shield_control_keys(green_wall, player_joy, joy_axis, axis_value, 3, 0, shield_speed)

            if event.type == pygame.JOYBUTTONDOWN:
                import screens
                if not game_pause and start:
                    global green_bullet, blue_bullet, move_b_power, move_g_power
                    if event.button == 0 and event.joy == 1 and len(blue_fireball_group) < 6:
                        pygame.mixer.music.load(fireball_sound)
                        pygame.mixer.music.set_volume(0.5)
                        pygame.mixer.music.play()
                        blue_fire = fireballs.Fireball(blue_fire_ball, blue_dragon, blue_dragon.rect.x,
                                                       blue_dragon.rect.y,
                                                       70,
                                                       30, 5, green_dragon,
                                                       green_wall, blue_wall, b_shield)

                        blue_fireball_group.add(blue_fire)
                        blue_bullet = True
                    if event.button == 0 and event.joy == 0 and len(green_fireball_group) < 6:
                        pygame.mixer.music.load(fireball_sound)
                        pygame.mixer.music.set_volume(0.5)
                        pygame.mixer.music.play()
                        green_fire = fireballs.Fireball(green_fire_ball, green_dragon, green_dragon.rect.x,
                                                        green_dragon.rect.y, -50, 30, -5,
                                                        blue_dragon, blue_wall, green_wall, g_shield)
                        green_fireball_group.add(green_fire)

                        green_bullet = True

                    if event.button == 2 and event.joy == 1:
                        if blue_score == 3:
                            move_b_power = True

                    if event.button == 2 and event.joy == 0:
                        if green_score == 3:
                            move_g_power = True

                if event.button == 3:
                    pygame.mixer.music.load(menu_sound)
                    pygame.mixer.music.play()
                    if start:
                        game_pause = not game_pause
                    else:
                        start = True

    def game_loop(self):
        import screens
        global blue_dragon_dir, green_bullet, blue_bullet, num_green_bullet, \
            num_blue_bullet, blue_fire, green_fire, g_life, b_life, b_shield, g_shield, \
            cont_hit_b_shield, cont_hit_g_shield, g_vulnerable, b_vulnerable, move_power, \
            blue_score, green_score, move_b_power, move_g_power, cond_g, cond_b, frame, frame_background, image_update, random_x, image_update_random


        blue_score = 0
        green_score = 0

        while True:
            dt = clock.tick() / 1000
            self.check_events()
            screen.fill([0, 0, 0])
            current_time = pygame.time.get_ticks()

            if start and game_pause is False:

                screen.blit(background_image, (0, 100))
                self.scor = score.score(blue_colour, green_colour, blue_score, green_score, (550, 45), (700, 45),
                                        b_life, b_shield, g_life, g_shield, (10, 70), (screen_width - 430, 70))


                if current_time - image_update > lightning_cooldown:
                    image_update = current_time
                    frame_background = screens.frame_checker(frame_background, max_lightning_frames)
                    if frame_background == 9:
                        random_x = -300

                    if current_time - image_update_random > lightning_random_cooldown:
                        image_update_random = current_time
                        random_x = random.randint(10, 1325)


                screens.background_lightning(lightning_sheet_img, lightning_frame_width,
                                              lightning_sheet_height,
                                             frame_background, random_x)

                drawGroup.draw(screen)
                Dragon.dragon_move(green_dragon, dt)
                Dragon.dragon_move(blue_dragon, dt)
                Dragon.upper_wall_collision(blue_dragon, 75)
                Dragon.lower_wall_collision(blue_dragon, 580)
                Dragon.upper_wall_collision(green_dragon, 75)
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
                        pygame.mixer.music.load(win_sound)
                        pygame.mixer.music.play()
                        for a in range(max_win_frames * win_length):
                            screen.fill(black_colour)
                            frame = screens.frame_checker(frame, max_win_frames)
                            screens.win_text(blue_wins_sheet, frame, blue_win_frame_width)
                            pygame.display.flip()
                            pygame.time.wait(50)
                        exit()

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
                        pygame.mixer.music.load(win_sound)
                        pygame.mixer.music.play()

                        for a in range(max_win_frames * win_length):
                            screen.fill(black_colour)
                            frame = screens.frame_checker(frame, max_win_frames)
                            screens.win_text(green_wins_sheet, frame, green_win_frame_width)
                            pygame.display.flip()
                            pygame.time.wait(50)
                        exit()


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

                                pygame.mixer.music.load(win_sound)
                                pygame.mixer.music.play()
                                for a in range(max_win_frames * win_length):
                                    screen.fill(black_colour)
                                    frame = screens.frame_checker(frame, max_win_frames)
                                    screens.win_text(green_wins_sheet, frame, green_win_frame_width)
                                    pygame.display.flip()
                                    pygame.time.wait(50)
                                exit()

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

                                pygame.mixer.music.load(win_sound)
                                pygame.mixer.music.play()
                                for a in range(max_win_frames * win_length):
                                    screen.fill(black_colour)
                                    frame = screens.frame_checker(frame, max_win_frames)
                                    screens.win_text(green_wins_sheet, frame, green_win_frame_width)
                                    pygame.display.flip()
                                    pygame.time.wait(50)
                                exit()

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

                                pygame.mixer.music.load(win_sound)
                                pygame.mixer.music.play()
                                for a in range(max_win_frames * win_length):
                                    screen.fill(black_colour)
                                    frame = screens.frame_checker(frame, max_win_frames)
                                    screens.win_text(blue_wins_sheet, frame, blue_win_frame_width)
                                    pygame.display.flip()
                                    pygame.time.wait(50)
                                exit()


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
                                pygame.mixer.music.load(win_sound)
                                pygame.mixer.music.play()
                                for a in range(max_win_frames * win_length):
                                    screen.fill(black_colour)
                                    frame = screens.frame_checker(frame, max_win_frames)
                                    screens.win_text(blue_wins_sheet, frame, blue_win_frame_width)
                                    pygame.display.flip()
                                    pygame.time.wait(50)
                                exit()

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

                    if current_time - image_update > config.start_button_cooldown:
                        image_update = current_time
                        frame = screens.frame_checker(frame, config.start_frames)
                        screens.start_screen(frame)
                        pygame.display.flip()


                if game_pause:

                    if current_time - image_update >= config.return_button_cooldown:
                        image_update = current_time
                        frame = screens.frame_checker(frame, config.start_frames)
                        screens.game_pause_screen(frame)
                        pygame.display.flip()

