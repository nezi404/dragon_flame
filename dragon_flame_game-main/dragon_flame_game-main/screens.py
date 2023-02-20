import pygame
import config

start_frames = config.start_sheet_height / config.start_frame_height


def sprite_frame(sheet, width, height, frame):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (0, height * frame, width, height))
    image.set_colorkey([0, 0, 0])
    return image


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
   
