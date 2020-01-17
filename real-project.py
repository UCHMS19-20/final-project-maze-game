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

# --------------------------------------------------------------------------------------------

import sys
import pygame

# Initialize pygame so it runs in the background and manages things
pygame.init()

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (700, 500) )

# colors
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
lime = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
yellow = pygame.Color(255,255,0)
green = pygame.Color(0,128,0)
navy = pygame.Color(0,0,128)

# original player position
x = 15
y = 15
# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= .08
    if pressed[pygame.K_DOWN]: y += .08
    if pressed[pygame.K_LEFT]: x -= .08
    if pressed[pygame.K_RIGHT]: x += .08

        #makes the display screen white
    screen.fill(navy)

        #draws the rectangle which the player can move
    pygame.draw.rect(screen, white, pygame.Rect(x, y, 15, 15))
    # if x < 0 or x > 700 or y<0 or y>500:
    #     sys.exit()
        #redraws the entire screen
    pygame.draw.rect(screen, green, (0,0,10,500))
    pygame.draw.rect(screen, green, (0,0,700,10))
    pygame.display.update()