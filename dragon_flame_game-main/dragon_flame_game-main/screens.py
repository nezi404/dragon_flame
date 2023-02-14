import pygame

import config

start_frames = config.start_sheet_height / config.start_frame_height


def sprite_frame(sheet, width, height, frame):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (0, 0, width, height * frame))
    image.set_colorkey([0, 0, 0])
    return image


def start_screen(frames):
    import game
    frame_0 = sprite_frame(config.start_img_sheet, config.start_frame_width, config.start_frame_height, frames)
    game.screen.blit(frame_0, (config.start_xcoor, config.start_ycoor))


def game_pause_screen(frames):
    import game
    frame_0 = sprite_frame(config.return_img_sheet, config.return_frame_width, config.return_frame_height, frames)
    game.screen.blit(frame_0, (config.start_xcoor, config.start_ycoor))
   