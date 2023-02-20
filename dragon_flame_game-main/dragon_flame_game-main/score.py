import pygame
import config
import game
def score(colourblue, colourgreen, bluescore, greenscore, position1, position2, lifeb, shieldb, lifeg, shieldg, b_stts_pos, g_stts_pos):
    font = pygame.font.SysFont(config.font, 50, True)
    font2 = pygame.font.SysFont(config.font, 30, True)
    score1 = font.render(f"{bluescore}", True, colourblue)
    x = font.render(f"   X   ", True, "white")
    score2 = font.render(f" {greenscore}", True, colourgreen)
    b_stts = font2.render(f"LIFE  {lifeb}  SHIELD  {shieldb}", True, colourblue)
    g_stts = font2.render(f"LIFE  {lifeg}  SHIELD  {shieldg}", True, colourgreen)
    game.screen.blit(score1, position1)
    game.screen.blit(x, (640, position1[1]))
    game.screen.blit(score2, position2)
    game.screen.blit(b_stts, b_stts_pos)
    game.screen.blit(g_stts, g_stts_pos)