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
# make each instructional window a branch and interactive

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
        y -= .1
    if pressed[pygame.K_DOWN] and y < 685:
        y += .1
    if pressed[pygame.K_LEFT] and x > 0:
        x -= .1
    if pressed[pygame.K_RIGHT] and x < 1185:
        x += .1
        #makes the display screen white
    screen.fill(navy)
    # for block in groundBlocks:
    #     if(pygame.sprite.collide_rect(player, block)):
    #         sys.exit()
        #draws the rectangle which the player can move
    pygame.draw.rect(screen, green, (0, 10, 10, 690))
    pygame.draw.rect(screen, green, (0, 690, 1165, 10))
    pygame.draw.rect(screen, green, (1190, 0, 10, 700))
    pygame.draw.rect(screen, green, (0, 0, 1200, 10))
    pygame.draw.rect(screen, green, (35, 35, 10, 665))
    pygame.draw.rect(screen, green, (70, 35, 1095, 10))
    pygame.draw.rect(screen, green, (1155, 35, 10, 595))
    pygame.draw.rect(screen, green, (665, 620, 500, 10))
    pygame.draw.rect(screen, green, (630, 70, 10, 595))
    pygame.draw.rect(screen, green, (630, 170, 35, 10))
    pygame.draw.rect(screen, green, (630, 490, 35, 10))
    pygame.draw.rect(screen, green, (665, 70, 10, 525))
    pygame.draw.rect(screen, green, (665, 100, 35, 10))
    pygame.draw.rect(screen, green, (665, 195, 35, 10))
    pygame.draw.rect(screen, green, (700, 70, 10, 525))
    pygame.draw.rect(screen, green, (700, 270, 35, 10))
    pygame.draw.rect(screen, green, (700, 540, 35, 10))
    pygame.draw.rect(screen, green, (735, 70, 10, 525))
    pygame.draw.rect(screen, green, (735, 370, 35, 10))
    pygame.draw.rect(screen, green, (735, 120, 35, 10))
    pygame.draw.rect(screen, green, (770, 70, 10, 525))
    pygame.draw.rect(screen, green, (805, 430, 35, 10))
    pygame.draw.rect(screen, green, (805, 320, 35, 10))
    pygame.draw.rect(screen, green, (805, 70, 10, 525))
    pygame.draw.rect(screen, green, (840, 35, 10, 560))
    pygame.draw.rect(screen, green, (875, 70, 10, 560))
    pygame.draw.rect(screen, green, (910, 70, 10, 525))
    pygame.draw.rect(screen, green, (910, 70, 220, 10))
    pygame.draw.rect(screen, green, (1120, 70, 10, 525))
    pygame.draw.rect(screen, green, (910, 585, 220, 10))
    pygame.draw.rect(screen, green, (430, 70, 210, 10))
    pygame.draw.rect(screen, green, (210, 70, 165, 10))
    pygame.draw.rect(screen, green, (70, 70, 100, 10))
    pygame.draw.rect(screen, green, (170, 70, 10, 125))
    pygame.draw.rect(screen, green, (70, 185, 100, 10))
    pygame.draw.rect(screen, green, (170, 220, 10, 145))
    pygame.draw.rect(screen, green, (205, 35, 10, 295))
    pygame.draw.rect(screen, green, (170, 35, 35, 10))
    pygame.draw.rect(screen, green, (205, 320, 190, 10))
    pygame.draw.rect(screen, green, (395, 70, 10, 260))
    pygame.draw.rect(screen, green, (365, 70, 10, 230))
    pygame.draw.rect(screen, green, (335, 70, 10, 230))
    pygame.draw.rect(screen, green, (305, 70, 10, 230))
    pygame.draw.rect(screen, green, (275, 70, 10, 230))
    pygame.draw.rect(screen, green, (245, 70, 10, 230))
    pygame.draw.rect(screen, green, (170, 355, 225, 10))
    pygame.draw.rect(screen, green, (430, 70, 10, 260))
    pygame.draw.rect(screen, green, (395, 355, 10, 245))
    pygame.draw.rect(screen, green, (205, 590, 190, 10))
    pygame.draw.rect(screen, green, (105, 630, 365, 10))
    pygame.draw.rect(screen, green, (70, 220, 100, 10))
    pygame.draw.rect(screen, green, (70, 355, 100, 10))
    pygame.draw.rect(screen, green, (70, 390, 100, 10))
    pygame.draw.rect(screen, green, (70, 555, 100, 10))
    pygame.draw.rect(screen, green, (70, 590, 135, 10))
    pygame.draw.rect(screen, green, (195, 530, 10, 70))
    pygame.draw.rect(screen, green, (105, 520, 100, 10))
    pygame.draw.rect(screen, green, (105, 425, 10, 95))
    pygame.draw.rect(screen, green, (105, 425, 100, 10))
    pygame.draw.rect(screen, green, (195, 365, 10, 70))
    pygame.draw.rect(screen, green, (170, 355, 35, 10))
    pygame.draw.rect(screen, green, (70, 70, 10, 115))
    pygame.draw.rect(screen, green, (70, 220, 10, 135))
    pygame.draw.rect(screen, green, (70, 390, 10, 165))
    pygame.draw.rect(screen, green, (70, 590, 10, 75))
    pygame.draw.rect(screen, green, (70, 655, 400, 10))
    pygame.draw.rect(screen, green, (505, 655, 685, 10))
    pygame.draw.rect(screen, green, (470, 655, 10, 35))
    pygame.draw.rect(screen, green, (430, 355, 10, 255))
    pygame.draw.rect(screen, green, (430, 355, 85, 10))
    pygame.draw.rect(screen, green, (530, 355, 100, 10))
    pygame.draw.rect(screen, green, (465, 100, 10, 260))
    pygame.draw.rect(screen, green, (489, 100, 10, 230))
    pygame.draw.rect(screen, green, (513, 100, 10, 230))
    pygame.draw.rect(screen, green, (537, 100, 10, 230))
    pygame.draw.rect(screen, green, (564, 100, 10, 230))
    pygame.draw.rect(screen, green, (587, 100, 10, 230))
    pygame.draw.rect(screen, green, (606, 100, 10, 230))
    pygame.draw.rect(screen, green, (460, 385, 10, 255))
    pygame.draw.rect(screen, green, (460, 385, 140, 10))
    pygame.draw.rect(screen, green, (600, 385, 10, 100))
    pygame.draw.rect(screen, green, (600, 515, 10, 125))
    pygame.draw.rect(screen, green, (580, 515, 10, 125))
    pygame.draw.rect(screen, green, (560, 425, 10, 215))
    pygame.draw.rect(screen, green, (540, 425, 10, 215))
    pygame.draw.rect(screen, green, (520, 425, 10, 215))
    pygame.draw.rect(screen, green, (500, 425, 10, 215))
    pygame.draw.rect(screen, yellow, pygame.Rect(x, y, 15, 15))
    pygame.display.update()

    # testing