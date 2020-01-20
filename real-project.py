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

# background and outline with paint


# make initial pygame window with instructions and clickable button
# make the difficulty levels affect speed of sprite and replace with variables
# turn rectangles into branch

# --------------------------------------------------------------------------------------------

import sys
import pygame

# Initialize pygame so it runs in the background and manages things
pygame.init()

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (1200, 700) )

# colors
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
lime = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
yellow = pygame.Color(255,255,0)
green = pygame.Color(0,128,0)
navy = pygame.Color(0,0,128)

# groundBlocks = [pygame.draw.rect(screen, green, (0, 10, 10, 690))]

# original player position
x = 15
y = 674
# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y > 0:
        y -= .5
    if pressed[pygame.K_DOWN] and y < 685:
        y += .5
    if pressed[pygame.K_LEFT] and x > 0:
        x -= .5
    if pressed[pygame.K_RIGHT] and x < 1185:
        x += .5
        #makes the display screen white
    screen.fill(navy)
    # for block in groundBlocks:
    #     if(pygame.sprite.collide_rect(player, block)):
    #         sys.exit()
        #draws the rectangle which the player can move
    pygame.draw.rect(screen, yellow, pygame.Rect(x, y, 15, 15))
    pygame.draw.rect(screen, green, (0, 10, 10, 690))
    pygame.draw.rect(screen, green, (0, 690, 1165, 10))
    pygame.draw.rect(screen, green, (1190, 0, 10, 700))
    pygame.draw.rect(screen, green, (0, 0, 1200, 10))
    pygame.draw.rect(screen, green, (35, 35, 10, 665))
    pygame.draw.rect(screen, green, (70, 35, 100, 10))
    pygame.draw.rect(screen, green, (70, 70, 100, 10))
    pygame.draw.rect(screen, green, (70, 185, 100, 10))
    pygame.draw.rect(screen, green, (70, 220, 100, 10))
    pygame.draw.rect(screen, green, (70, 355, 100, 10))
    pygame.draw.rect(screen, green, (70, 390, 100, 10))
    pygame.draw.rect(screen, green, (70, 555, 100, 10))
    pygame.draw.rect(screen, green, (70, 590, 100, 10))
    pygame.draw.rect(screen, green, (70, 70, 10, 115))
    pygame.draw.rect(screen, green, (70, 220, 10, 135))
    pygame.draw.rect(screen, green, (70, 390, 10, 165))
    pygame.draw.rect(screen, green, (70, 590, 10, 75))
    pygame.draw.rect(screen, green, (70, 655, 400, 10))
    pygame.draw.rect(screen, green, (470, 655, 10, 35))
    pygame.display.update()