# plan:
# - make a maze where the user's mouse is tracked
# - use pixels to draw the maze with multiple traps, but not too
#   difficult resulting in the user failing from trying to take normal path
# - make the user lose and restart if a wall (filled pixel) is touched
# - make multiple levels of the maze, and allow each to have
#   a level of difficulty from easy to hard
# - make a win/lose message
# - possibly add a timed gamemode
# - more to come from plan

import sys
import pygame
pygame.init()
screen = pygame.display.set_mode((700, 500))
screen.fill((255,255,255))
pygame.display.flip()
pygame.display.get_surface()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()