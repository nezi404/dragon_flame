import pygame
import config

def image_loader(image_path, x, y):
    image = pygame.image.load(image_path).convert_alpha()
    image = pygame.transform.scale(image, [x, y])
    return image

def frame_checker(frames, maxframe):
    frames+= 1
    if frames > maxframe:
        frames = 0
    return frames

def sprite_frame(sheet, width, height, frame):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (0, height * frame, width, height))
    image.set_colorkey([0, 0, 0])
    return image

def win_text(sheet, frames, win_frame_width):
    import game
    win = sprite_frame(sheet, win_frame_width, config.win_frame_height, frames)
    game.screen.blit(win, (config.win_x_coor, config.win_y_coor))



def start_screen(frames):
    import game
    frame_0 = sprite_frame(config.start_img_sheet, config.start_frame_width, config.start_frame_height, frames)
    frame_game = sprite_frame(config.game_name_img_sheet, config.game_name_frame_width, config.game_name_frame_height, frames)
    game.screen.blit(frame_0, (config.start_x_coor, config.start_y_coor))
    game.screen.blit(frame_game, (config.name_x_coor, config.name_y_coor))


def game_pause_screen(frames):
    import game
    frame_0 = sprite_frame(config.return_img_sheet, config.return_frame_width, config.return_frame_height, frames)
    game.screen.blit(frame_0, (config.start_x_coor, config.start_y_coor))
   
