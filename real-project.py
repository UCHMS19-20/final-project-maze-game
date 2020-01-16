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

# --------------------------------------------------------------------------------------------

# import sys
# import pygame

# # Initialize pygame so it runs in the background and manages things
# pygame.init()

# # Create a display. Size must be a tuple, which is why it's in parentheses
# screen = pygame.display.set_mode( (700, 500) )

# black = pygame.Color(0,0,0)
# white = pygame.Color(255,255,255)
# red = pygame.Color(255,0,0)
# lime = pygame.Color(0,255,0)
# blue = pygame.Color(0,0,255)
# yellow = pygame.Color(255,255,0)
# green = pygame.Color(0,128,0)
# navy = pygame.Color(0,0,128)

# # Main loop. Your game would go inside this loop
# while True:
#     # do something for each event in the event queue (list of things that happen)
#     for event in pygame.event.get():
#         # Check to see if the current event is a QUIT event
#         if event.type == pygame.QUIT:
#             # If so, exit the program
#             sys.exit()


# pygame.display.update()


import sys
import pygame

# Initialize pygame so it runs in the background and manages things
pygame.init()

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (700, 500) )

#set-up the colors based on RGB table
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
lime = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
yellow = pygame.Color(255,255,0)
green = pygame.Color(0,128,0)
navy = pygame.Color(0,0,128)

#creates variables for player position
x = 3
y = 3
# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 1
    if pressed[pygame.K_DOWN]: y += 1
    if pressed[pygame.K_LEFT]: x -= 1
    if pressed[pygame.K_RIGHT]: x += 1

        #makes the display screen white
    screen.fill(white)
    pygame.display.flip()

        #draws the rectangle which the player can move
    pygame.draw.rect(screen, red, pygame.Rect(x, y, 30, 30))
        
        #redraws the entire screen
    pygame.display.update()