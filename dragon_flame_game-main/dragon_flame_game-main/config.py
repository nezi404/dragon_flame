import pygame
import screens

pygame.font.init()
pygame.mixer.init()

# Screen
screen_width = 1400
screen_height = 680

# Clock
clk = pygame.time.Clock()
hit_timer = 0
fps = 60
black_colour = (0, 0, 0)

# Dragons
drawGroup = pygame.sprite.Group()
green_dragon = pygame.sprite.Sprite(drawGroup)
blue_dragon = pygame.sprite.Sprite(drawGroup)

vulnerable_bd = "blue_vulnerable_dragon"
vulnerable_gd = "green_vulnerable_dragon"

death_bd = "death_b_dragon"
death_gd = "death_g_dragon"

cont_hit_b_shield = 0
cont_hit_g_shield = 0

blue_d = "blue_dragon"
green_d = "green_dragon"

b_life = 4
g_life = 4
b_shield = 30
g_shield = 30
blue_score = 0
green_score = 0

blue_angle = 70
green_angle = -70

dragon_speed = 200
dragon_size = (660, 500)

initial_bd_x_pos = 70
initial_gd_x_pos = 1230
initial_d_y_pos = 320

# Shields (walls)
blue_wall = pygame.sprite.Sprite(drawGroup)
green_wall = pygame.sprite.Sprite(drawGroup)
blue_w = "blue_wall"
green_w = "green_wall"

game_font = "font/PressStart2P.ttf"
shield_size = (830, 365)
shield_speed = 15

initial_bw_x_pos = 200
initial_gw_x_pos = 1100
initial_w_y_pos = 325

# Power up
blue_power_up = pygame.sprite.Sprite()
green_power_up = pygame.sprite.Sprite()
blue_pu = "blue_powerup"
green_pu = "green_powerup"

# Game display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dragon-Flame")





# Start screen
start_frame_height = 90
start_frame_width = 580
start_sheet_height = 540
start_img_sheet = screens.image_loader("sprites/start_message2.png", start_frame_width, start_sheet_height)
start_x_coor = screen_width/2 - start_frame_width/2
start_y_coor = screen_height - screen_height/3
start_button_cooldown = 90
start_frames = start_sheet_height / start_frame_height


name_sacale = 3
game_name_frame_height = 70 * name_sacale
game_name_frame_width = 320 * name_sacale
game_name_sheet_height = 560 * name_sacale
game_name_img_sheet = screens.image_loader("sprites/dragon_flame.png", game_name_frame_width, game_name_sheet_height)
name_x_coor = screen_width/2 - game_name_frame_width/2
name_y_coor = 150

# Pause screen
return_frame_height = 90
return_frame_width = 615
return_sheet_height = 450
return_img_sheet = screens.image_loader("sprites/return_message1.png", return_frame_width, return_sheet_height)
return_x_coor = screen_width/2 - start_frame_width/2
return_y_coor = screen_height - screen_height/3
return_button_cooldown = 90

# Fireball related
fireball_scale = 1.5
fireball_frame_width = 24 * fireball_scale
fireball_frame_height = 12 * fireball_scale
blue_fire_ball = screens.image_loader("sprites/blue_flame.png", fireball_frame_width, fireball_frame_height)
green_fire_ball = screens.image_loader("sprites/green_flame.png", fireball_frame_width, fireball_frame_height)
max_num_bullets = 6

# Scoring
font = "arial"
green_colour = (0, 100, 0)
blue_colour = (11, 11, 70)

# Winning
max_win_frames = 7
win_sheet_height = 455
blue_win_frame_width = 910
green_win_frame_width = 992
win_frame_height = win_sheet_height/max_win_frames
win_length = 20
blue_wins_sheet = screens.image_loader("sprites/blue_wins.png", blue_win_frame_width , win_sheet_height)
green_wins_sheet = screens.image_loader("sprites/green_wins.png", green_win_frame_width , win_sheet_height)
win_x_coor = 260
win_y_coor = 350


#Sounds
menu_sound = "sounds/start_pause_sound.wav"
fireball_sound = "sounds/fire_blow.mp3"
win_sound = "sounds/victory_sound.mp3"

#background
lightning_sheet_width = 1480
lightning_sheet_height = 700
lightning_frame_width = 148
max_lightning_frames = 9
lightning_sheet_img = screens.image_loader("sprites/lightning1.png", lightning_frame_width * (max_lightning_frames + 1), lightning_sheet_height)
lightning_cooldown = 60
lightning_random_cooldown = 4000
background_image = screens.image_loader("sprites/background_image1.png", screen_width, screen_height - 100)




