import pygame

pygame.font.init()
pygame.mixer.init()

# Screen
screen_width = 1400
screen_height = 680

# Clock
clk = pygame.time.Clock()
hit_timer = 0
fps = 60

# Dragons
drawGroup = pygame.sprite.Group()
green_dragon = pygame.sprite.Sprite(drawGroup)
blue_dragon = pygame.sprite.Sprite(drawGroup)

blue_d = "blue_dragon"
green_d = "green_dragon"

blue_angle = 70
green_angle = -70

dragon_speed = 100
dragon_size = (660, 500)

initial_bd_x_pos = 70
initial_gd_x_pos = 1230
initial_d_y_pos = 320

# Shields (walls)
blue_wall = pygame.sprite.Sprite(drawGroup)
green_wall = pygame.sprite.Sprite(drawGroup)
blue_w = "blue_wall"
green_w = "green_wall"
shield_size = (830, 365)



shield_speed = 15

initial_bw_x_pos = 200
initial_gw_x_pos = 1100
initial_w_y_pos = 325

# Game display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dragon-Flame")

# start screen
def image_loader(imagepath):
    image = pygame.image.load(imagepath).convert_alpha()
    return image
start_img_sheet = image_loader("sprites/start_message1.png")
start_frame_height = 90
start_frame_width = 580
start_sheet_height = 540
start_xcoor = screen_width/2 - start_frame_width/2
start_ycoor = screen_height - screen_height/3
start_button_cooldown = 90
# pause screen
return_img_sheet = image_loader("sprites/return_message.png")
return_frame_height = 90
return_frame_width = 615
return_sheet_height = 540
return_xcoor = screen_width/2 - start_frame_width/2
return_ycoor = screen_height - screen_height/3
return_button_cooldown = 90
# fireball related
fireball_img = image_loader("sprites/fireball_image.png")
fireball_scale = 1.5
fireball_frame_width = 24 * fireball_scale
fireball_frame_height = 24 * fireball_scale

max_num_bullets = 6
