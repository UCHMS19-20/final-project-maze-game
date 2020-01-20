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
import time

# Initialize pygame so it runs in the background and manages things
pygame.init()

# Create a font object
font = pygame.font.SysFont("Arial", 50)
# Create text using the font
text1 = font.render("Instructions:", True, (0,0,0))


# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (800, 600) )

# fill the screen with white
screen.fill((255,255,255))
# draw text to screen
screen.blit(text1, (20, 20) )
# update the display
pygame.display.flip()

# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
    time.sleep(2)
    font = pygame.font.SysFont("Arial", 30)
    # Create text using the font
    text1 = font.render("Move the yellow box with the arrow keys.", True, (0,0,0))


    # Create a display. Size must be a tuple, which is why it's in parentheses
    screen = pygame.display.set_mode( (800, 600) )

    # fill the screen with white
    screen.fill((255,255,255))
    # draw text to screen
    screen.blit(text1, (20, 20) )
    # update the display
    pygame.display.flip()

    # Main loop. Your game would go inside this loop
    while True:
        # do something for each event in the event queue (list of things that happen)
        for event in pygame.event.get():
            # Check to see if the current event is a QUIT event
            if event.type == pygame.QUIT:
                # If so, exit the program
                sys.exit()
        # Create a font object
        time.sleep(4)
        font = pygame.font.SysFont("Arial", 20)
        # Create text using the font
        text1 = font.render("Don't hit the walls.", True, (0,0,0))


        # Create a display. Size must be a tuple, which is why it's in parentheses
        screen = pygame.display.set_mode( (800, 600) )

        # fill the screen with white
        screen.fill((255,255,255))
        # draw text to screen
        screen.blit(text1, (20, 20) )
        # update the display
        pygame.display.flip()

        # Main loop. Your game would go inside this loop
        while True:
            # do something for each event in the event queue (list of things that happen)
            for event in pygame.event.get():
                # Check to see if the current event is a QUIT event
                if event.type == pygame.QUIT:
                    # If so, exit the program
                    sys.exit()
            # Create a font object
            time.sleep(4)
            font = pygame.font.SysFont("Arial", 20)
            # Create text using the font
            text1 = font.render("Get the yellow box to the bottom right corner.", True, (0,0,0))


            # Create a display. Size must be a tuple, which is why it's in parentheses
            screen = pygame.display.set_mode( (800, 600) )

            # fill the screen with white
            screen.fill((255,255,255))
            # draw text to screen
            screen.blit(text1, (20, 20) )
            # update the display
            pygame.display.flip()

            # Main loop. Your game would go inside this loop
            while True:
                # do something for each event in the event queue (list of things that happen)
                for event in pygame.event.get():
                    # Check to see if the current event is a QUIT event
                    if event.type == pygame.QUIT:
                        # If so, exit the program
                        sys.exit()
                # Create a font object
                time.sleep(4)
                font = pygame.font.SysFont("Arial", 50)
                # Create text using the font
                text1 = font.render("PRESS ENTER TO BEGIN", True, (0,0,0))


                # Create a display. Size must be a tuple, which is why it's in parentheses
                screen = pygame.display.set_mode( (800, 600) )

                # fill the screen with white
                screen.fill((255,255,255))
                # draw text to screen
                screen.blit(text1, (20, 20) )
                # update the display
                pygame.display.flip()

                # Main loop. Your game would go inside this loop
                while True:
                    # do something for each event in the event queue (list of things that happen)
                    for event in pygame.event.get():
                        # Check to see if the current event is a QUIT event
                        if event.type == pygame.QUIT:
                            # If so, exit the program
                            sys.exit()
                    pressed = pygame.key.get_pressed()
                    if pressed[pygame.K_RETURN]:
                        sys.exit()
                        # 