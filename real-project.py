# import the necessary modules for the code
import sys
import pygame
import time
# initialize pygame so it runs in the background and manages things
pygame.init()
# create a title for the pygame windows that open
pygame.display.set_caption('Maze Game')
# create new font size
font = pygame.font.SysFont("Arial", 50)
# create text using the font
text1 = font.render("Instructions:", True, (0,0,0))
# create a display
screen = pygame.display.set_mode( (800, 200) )
# fill the screen with white
screen.fill((255,255,255))
# draw text to screen
screen.blit(text1, (20, 20) )
# update the display
pygame.display.flip()
# loop to progress through instructions
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
    # 2 second delay
    time.sleep(2)
    # create new font size
    font = pygame.font.SysFont("Arial", 30)
    # create text using the font
    text1 = font.render("Move the yellow box with the arrow keys.", True, (0,0,0))
    # create a display
    screen = pygame.display.set_mode( (800, 200) )
    # fill the screen with white
    screen.fill((255,255,255))
    # draw text to screen
    screen.blit(text1, (20, 20) )
    # update the display
    pygame.display.flip()
    # loop to continue instructions
    while True:
        # do something for each event in the event queue (list of things that happen)
        for event in pygame.event.get():
            # Check to see if the current event is a QUIT event
            if event.type == pygame.QUIT:
                # If so, exit the program
                sys.exit()
        # 4 second delay
        time.sleep(4)
        # create new font size
        font = pygame.font.SysFont("Arial", 30)
        # create text using the font
        text1 = font.render("Don't hit the walls.", True, (0,0,0))
        # create a display
        screen = pygame.display.set_mode( (800, 200) )
        # fill the screen with white
        screen.fill((255,255,255))
        # draw text to screen
        screen.blit(text1, (20, 20) )
        # update the display
        pygame.display.flip()
        # loop to continue with instructions
        while True:
            # do something for each event in the event queue (list of things that happen)
            for event in pygame.event.get():
                # Check to see if the current event is a QUIT event
                if event.type == pygame.QUIT:
                    # If so, exit the program
                    sys.exit()
            # 4 second delay
            time.sleep(4)
            # create a new font size
            font = pygame.font.SysFont("Arial", 30)
            # create text using the font
            text1 = font.render("Get the yellow box to the bottom right corner.", True, (0,0,0))
            # create a display
            screen = pygame.display.set_mode( (800, 200) )
            # fill the screen with white
            screen.fill((255,255,255))
            # draw text to screen
            screen.blit(text1, (20, 20) )
            # update the display
            pygame.display.flip()
            # loop to choose gamemode difficulty
            while True:
                # do something for each event in the event queue (list of things that happen)
                for event in pygame.event.get():
                    # Check to see if the current event is a QUIT event
                    if event.type == pygame.QUIT:
                        # If so, exit the program
                        sys.exit()
                # 4 second delay
                time.sleep(4)
                # create new font size
                font = pygame.font.SysFont("Arial", 30)
                # create text using the font
                text1 = font.render("Press 1 for easy, 2 for medium, or 3 for hard.", True, (0,0,0))
                # create a display
                screen = pygame.display.set_mode( (800, 200) )
                # fill the screen with white
                screen.fill((255,255,255))
                # draw text to screen
                screen.blit(text1, (20, 20) )
                # update the display
                pygame.display.flip()
                # gamemode loop containing if statement with everything
                while True:
                    # do something for each event in the event queue (list of things that happen)
                    for event in pygame.event.get():
                        # Check to see if the current event is a QUIT event
                        if event.type == pygame.QUIT:
                            # If so, exit the program
                            sys.exit()
                    # if statement to determine which key was pressed determining speed of yellow block
                    pressed = pygame.key.get_pressed()
                    if pressed[pygame.K_1]:
                        # create a display
                        screen = pygame.display.set_mode( (1200, 700) )
                        # creates a list of colors that can be used later easily if necessary
                        black = pygame.Color(0,0,0)
                        white = pygame.Color(255,255,255)
                        red = pygame.Color(255,0,0)
                        lime = pygame.Color(0,255,0)
                        blue = pygame.Color(0,0,255)
                        yellow = pygame.Color(255,255,0)
                        green = pygame.Color(0,128,0)
                        navy = pygame.Color(0,0,128)
                        # yellow block starting position
                        x = 15
                        y = 674
                        # game loop
                        while True:
                            # do something for each event in the event queue (list of things that happen)
                            for event in pygame.event.get():
                                # Check to see if the current event is a QUIT event
                                if event.type == pygame.QUIT:
                                    # If so, exit the program
                                    sys.exit()
                            # creates a variable for the sprite as a yellow rectangle
                            sprite = pygame.draw.rect(screen, yellow, pygame.Rect(x, y, 15, 15))
                            # creates speed for which the yellow block will move with each arrow key press
                            pressed = pygame.key.get_pressed()
                            if pressed[pygame.K_UP] and y > 0:
                                y -= .1
                            if pressed[pygame.K_DOWN] and y < 685:
                                y += .1
                            if pressed[pygame.K_LEFT] and x > 0:
                                x -= .1
                            if pressed[pygame.K_RIGHT] and x < 1185:
                                x += .1
                            # makes the maze background navy
                            screen.fill(navy)
                            # creates a list of rectangles that can be used to make collision borders
                            rectangle_list = [
                                pygame.Rect(0, 10, 10, 690),
                                pygame.Rect(0, 690, 1165, 10),
                                pygame.Rect(1190, 0, 10, 700),
                                pygame.Rect(0, 0, 1200, 10),
                                pygame.Rect(35, 35, 10, 665),
                                pygame.Rect(70, 35, 1095, 10),
                                pygame.Rect(1155, 35, 10, 595),
                                pygame.Rect(665, 620, 500, 10),
                                pygame.Rect(630, 70, 10, 595),
                                pygame.Rect(630, 170, 35, 10),
                                pygame.Rect(630, 490, 35, 10),
                                pygame.Rect(665, 70, 10, 525),
                                pygame.Rect(665, 100, 35, 10),
                                pygame.Rect(665, 195, 35, 10),
                                pygame.Rect(700, 70, 10, 525),
                                pygame.Rect(700, 270, 35, 10),
                                pygame.Rect(700, 540, 35, 10),
                                pygame.Rect(735, 70, 10, 525),
                                pygame.Rect(735, 370, 35, 10),
                                pygame.Rect(735, 120, 35, 10),
                                pygame.Rect(770, 70, 10, 525),
                                pygame.Rect(805, 430, 35, 10),
                                pygame.Rect(805, 320, 35, 10),
                                pygame.Rect(805, 70, 10, 525),
                                pygame.Rect(840, 35, 10, 560),
                                pygame.Rect(875, 70, 10, 560),
                                pygame.Rect(910, 70, 10, 525),
                                pygame.Rect(910, 70, 220, 10),
                                pygame.Rect(1120, 70, 10, 525),
                                pygame.Rect(910, 585, 220, 10),
                                pygame.Rect(430, 70, 210, 10),
                                pygame.Rect(210, 70, 165, 10),
                                pygame.Rect(70, 70, 100, 10),
                                pygame.Rect(170, 70, 10, 125),
                                pygame.Rect(70, 185, 100, 10),
                                pygame.Rect(170, 220, 10, 145),
                                pygame.Rect(205, 35, 10, 295),
                                pygame.Rect(170, 35, 35, 10),
                                pygame.Rect(205, 320, 190, 10),
                                pygame.Rect(395, 70, 10, 260),
                                pygame.Rect(365, 70, 10, 230),
                                pygame.Rect(335, 70, 10, 230),
                                pygame.Rect(305, 70, 10, 230),
                                pygame.Rect(275, 70, 10, 230),
                                pygame.Rect(245, 70, 10, 230),
                                pygame.Rect(170, 355, 225, 10),
                                pygame.Rect(430, 70, 10, 260),
                                pygame.Rect(395, 355, 10, 245),
                                pygame.Rect(205, 590, 190, 10),
                                pygame.Rect(105, 630, 365, 10),
                                pygame.Rect(70, 220, 100, 10),
                                pygame.Rect(70, 355, 100, 10),
                                pygame.Rect(70, 390, 100, 10),
                                pygame.Rect(70, 555, 100, 10),
                                pygame.Rect(70, 590, 135, 10),
                                pygame.Rect(195, 530, 10, 70),
                                pygame.Rect(105, 520, 100, 10),
                                pygame.Rect(105, 425, 10, 95),
                                pygame.Rect(105, 425, 100, 10),
                                pygame.Rect(195, 365, 10, 70),
                                pygame.Rect(170, 355, 35, 10),
                                pygame.Rect(70, 70, 10, 115),
                                pygame.Rect(70, 220, 10, 135),
                                pygame.Rect(70, 390, 10, 165),
                                pygame.Rect(70, 590, 10, 75),
                                pygame.Rect(70, 655, 400, 10),
                                pygame.Rect(505, 655, 685, 10),
                                pygame.Rect(470, 655, 10, 35),
                                pygame.Rect(430, 355, 10, 255),
                                pygame.Rect(430, 355, 85, 10),
                                pygame.Rect(530, 355, 100, 10),
                                pygame.Rect(465, 100, 10, 260),
                                pygame.Rect(489, 100, 10, 230),
                                pygame.Rect(513, 100, 10, 230),
                                pygame.Rect(537, 100, 10, 230),
                                pygame.Rect(564, 100, 10, 230),
                                pygame.Rect(587, 100, 10, 230),
                                pygame.Rect(606, 100, 10, 230),
                                pygame.Rect(460, 385, 10, 255),   
                                pygame.Rect(460, 385, 140, 10),
                                pygame.Rect(600, 385, 10, 100),
                                pygame.Rect(600, 515, 10, 125),
                                pygame.Rect(580, 515, 10, 125),
                                pygame.Rect(560, 425, 10, 215),
                                pygame.Rect(540, 425, 10, 215),
                                pygame.Rect(520, 425, 10, 215),
                                pygame.Rect(500, 425, 10, 215)]
                            # draws all of the necessary rectangles on the maze
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
                            # for statement to detect collisions
                            for rect in rectangle_list:
                                pygame.draw.rect(screen, green, rect, -1)
                                if sprite.colliderect(rect):
                                    # create new font size
                                    font = pygame.font.SysFont("Arial", 50)
                                    # create text using the font - LOSE MESSAGE
                                    text1 = font.render("Your skills ran into a problem. :(", True, (255,255,255))
                                    # create a display
                                    screen = pygame.display.set_mode( (800, 200) )
                                    # fill the screen with blue
                                    screen.fill((0,0,255))
                                    # draw text to screen
                                    screen.blit(text1, (20, 20) )
                                    # update the display
                                    pygame.display.flip()
                                    # 10 second delay
                                    time.sleep(10)
                                    # close the screen
                                    sys.quit()
                            # sets win condition
                            if y >= 685:
                                # create new font size
                                font = pygame.font.SysFont("Arial", 50)
                                # create text using the font
                                text1 = font.render("Your skills succeeded this time. :)", True, (black))
                                # create a display
                                screen = pygame.display.set_mode( (800, 200) )
                                # fill the screen with lime
                                screen.fill((lime))
                                # draw text to screen
                                screen.blit(text1, (20, 20) )
                                # update the display
                                pygame.display.flip()
                                # 10 second delay
                                time.sleep(10)
                                # close the game
                                sys.quit()
                            pygame.display.update()
                    if pressed[pygame.K_2]:
                        # create a display
                        screen = pygame.display.set_mode( (1200, 700) )
                        # creates a list of colors that can be used later easily if necessary
                        black = pygame.Color(0,0,0)
                        white = pygame.Color(255,255,255)
                        red = pygame.Color(255,0,0)
                        lime = pygame.Color(0,255,0)
                        blue = pygame.Color(0,0,255)
                        yellow = pygame.Color(255,255,0)
                        green = pygame.Color(0,128,0)
                        navy = pygame.Color(0,0,128)
                        # yellow block starting position
                        x = 15
                        y = 674
                        # game loop
                        while True:
                            # do something for each event in the event queue (list of things that happen)
                            for event in pygame.event.get():
                                # Check to see if the current event is a QUIT event
                                if event.type == pygame.QUIT:
                                    # If so, exit the program
                                    sys.exit()
                            # creates a variable for the sprite as a yellow rectangle
                            sprite = pygame.draw.rect(screen, yellow, pygame.Rect(x, y, 15, 15))
                            # creates speed for which the yellow block will move with each arrow key press
                            pressed = pygame.key.get_pressed()
                            if pressed[pygame.K_UP] and y > 0:
                                y -= .3
                            if pressed[pygame.K_DOWN] and y < 685:
                                y += .3
                            if pressed[pygame.K_LEFT] and x > 0:
                                x -= .3
                            if pressed[pygame.K_RIGHT] and x < 1185:
                                x += .3
                            # makes the maze background navy
                            screen.fill(navy)
                            # creates a list of rectangles that can be used to make collision borders
                            rectangle_list = [
                                pygame.Rect(0, 10, 10, 690),
                                pygame.Rect(0, 690, 1165, 10),
                                pygame.Rect(1190, 0, 10, 700),
                                pygame.Rect(0, 0, 1200, 10),
                                pygame.Rect(35, 35, 10, 665),
                                pygame.Rect(70, 35, 1095, 10),
                                pygame.Rect(1155, 35, 10, 595),
                                pygame.Rect(665, 620, 500, 10),
                                pygame.Rect(630, 70, 10, 595),
                                pygame.Rect(630, 170, 35, 10),
                                pygame.Rect(630, 490, 35, 10),
                                pygame.Rect(665, 70, 10, 525),
                                pygame.Rect(665, 100, 35, 10),
                                pygame.Rect(665, 195, 35, 10),
                                pygame.Rect(700, 70, 10, 525),
                                pygame.Rect(700, 270, 35, 10),
                                pygame.Rect(700, 540, 35, 10),
                                pygame.Rect(735, 70, 10, 525),
                                pygame.Rect(735, 370, 35, 10),
                                pygame.Rect(735, 120, 35, 10),
                                pygame.Rect(770, 70, 10, 525),
                                pygame.Rect(805, 430, 35, 10),
                                pygame.Rect(805, 320, 35, 10),
                                pygame.Rect(805, 70, 10, 525),
                                pygame.Rect(840, 35, 10, 560),
                                pygame.Rect(875, 70, 10, 560),
                                pygame.Rect(910, 70, 10, 525),
                                pygame.Rect(910, 70, 220, 10),
                                pygame.Rect(1120, 70, 10, 525),
                                pygame.Rect(910, 585, 220, 10),
                                pygame.Rect(430, 70, 210, 10),
                                pygame.Rect(210, 70, 165, 10),
                                pygame.Rect(70, 70, 100, 10),
                                pygame.Rect(170, 70, 10, 125),
                                pygame.Rect(70, 185, 100, 10),
                                pygame.Rect(170, 220, 10, 145),
                                pygame.Rect(205, 35, 10, 295),
                                pygame.Rect(170, 35, 35, 10),
                                pygame.Rect(205, 320, 190, 10),
                                pygame.Rect(395, 70, 10, 260),
                                pygame.Rect(365, 70, 10, 230),
                                pygame.Rect(335, 70, 10, 230),
                                pygame.Rect(305, 70, 10, 230),
                                pygame.Rect(275, 70, 10, 230),
                                pygame.Rect(245, 70, 10, 230),
                                pygame.Rect(170, 355, 225, 10),
                                pygame.Rect(430, 70, 10, 260),
                                pygame.Rect(395, 355, 10, 245),
                                pygame.Rect(205, 590, 190, 10),
                                pygame.Rect(105, 630, 365, 10),
                                pygame.Rect(70, 220, 100, 10),
                                pygame.Rect(70, 355, 100, 10),
                                pygame.Rect(70, 390, 100, 10),
                                pygame.Rect(70, 555, 100, 10),
                                pygame.Rect(70, 590, 135, 10),
                                pygame.Rect(195, 530, 10, 70),
                                pygame.Rect(105, 520, 100, 10),
                                pygame.Rect(105, 425, 10, 95),
                                pygame.Rect(105, 425, 100, 10),
                                pygame.Rect(195, 365, 10, 70),
                                pygame.Rect(170, 355, 35, 10),
                                pygame.Rect(70, 70, 10, 115),
                                pygame.Rect(70, 220, 10, 135),
                                pygame.Rect(70, 390, 10, 165),
                                pygame.Rect(70, 590, 10, 75),
                                pygame.Rect(70, 655, 400, 10),
                                pygame.Rect(505, 655, 685, 10),
                                pygame.Rect(470, 655, 10, 35),
                                pygame.Rect(430, 355, 10, 255),
                                pygame.Rect(430, 355, 85, 10),
                                pygame.Rect(530, 355, 100, 10),
                                pygame.Rect(465, 100, 10, 260),
                                pygame.Rect(489, 100, 10, 230),
                                pygame.Rect(513, 100, 10, 230),
                                pygame.Rect(537, 100, 10, 230),
                                pygame.Rect(564, 100, 10, 230),
                                pygame.Rect(587, 100, 10, 230),
                                pygame.Rect(606, 100, 10, 230),
                                pygame.Rect(460, 385, 10, 255),   
                                pygame.Rect(460, 385, 140, 10),
                                pygame.Rect(600, 385, 10, 100),
                                pygame.Rect(600, 515, 10, 125),
                                pygame.Rect(580, 515, 10, 125),
                                pygame.Rect(560, 425, 10, 215),
                                pygame.Rect(540, 425, 10, 215),
                                pygame.Rect(520, 425, 10, 215),
                                pygame.Rect(500, 425, 10, 215)]
                            # draws all of the necessary rectangles on the maze
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
                            # for statement to detect collisions
                            for rect in rectangle_list:
                                pygame.draw.rect(screen, green, rect, -1)
                                if sprite.colliderect(rect):
                                    # create new font size
                                    font = pygame.font.SysFont("Arial", 50)
                                    # create text using the font - LOSE MESSAGE
                                    text1 = font.render("Your skills ran into a problem. :(", True, (255,255,255))
                                    # create a display
                                    screen = pygame.display.set_mode( (800, 200) )
                                    # fill the screen with blue
                                    screen.fill((0,0,255))
                                    # draw text to screen
                                    screen.blit(text1, (20, 20) )
                                    # update the display
                                    pygame.display.flip()
                                    # 10 second delay
                                    time.sleep(10)
                                    # close the screen
                                    sys.quit()
                            # sets win condition
                            if y >= 685:
                                # create new font size
                                font = pygame.font.SysFont("Arial", 50)
                                # create text using the font
                                text1 = font.render("Your skills succeeded this time. :)", True, (black))
                                # create a display
                                screen = pygame.display.set_mode( (800, 200) )
                                # fill the screen with lime
                                screen.fill((lime))
                                # draw text to screen
                                screen.blit(text1, (20, 20) )
                                # update the display
                                pygame.display.flip()
                                # 10 second delay
                                time.sleep(10)
                                # close the game
                                sys.quit()
                            pygame.display.update()
                    if pressed[pygame.K_3]:
                        # create a display
                        screen = pygame.display.set_mode( (1200, 700) )
                        # creates a list of colors that can be used later easily if necessary
                        black = pygame.Color(0,0,0)
                        white = pygame.Color(255,255,255)
                        red = pygame.Color(255,0,0)
                        lime = pygame.Color(0,255,0)
                        blue = pygame.Color(0,0,255)
                        yellow = pygame.Color(255,255,0)
                        green = pygame.Color(0,128,0)
                        navy = pygame.Color(0,0,128)
                        # yellow block starting position
                        x = 15
                        y = 674
                        # game loop
                        while True:
                            # do something for each event in the event queue (list of things that happen)
                            for event in pygame.event.get():
                                # Check to see if the current event is a QUIT event
                                if event.type == pygame.QUIT:
                                    # If so, exit the program
                                    sys.exit()
                            # creates a variable for the sprite as a yellow rectangle
                            sprite = pygame.draw.rect(screen, yellow, pygame.Rect(x, y, 15, 15))
                            # creates speed for which the yellow block will move with each arrow key press
                            pressed = pygame.key.get_pressed()
                            if pressed[pygame.K_UP] and y > 0:
                                y -= .5
                            if pressed[pygame.K_DOWN] and y < 685:
                                y += .5
                            if pressed[pygame.K_LEFT] and x > 0:
                                x -= .5
                            if pressed[pygame.K_RIGHT] and x < 1185:
                                x += .5
                            # makes the maze background navy
                            screen.fill(navy)
                            # creates a list of rectangles that can be used to make collision borders
                            rectangle_list = [
                                pygame.Rect(0, 10, 10, 690),
                                pygame.Rect(0, 690, 1165, 10),
                                pygame.Rect(1190, 0, 10, 700),
                                pygame.Rect(0, 0, 1200, 10),
                                pygame.Rect(35, 35, 10, 665),
                                pygame.Rect(70, 35, 1095, 10),
                                pygame.Rect(1155, 35, 10, 595),
                                pygame.Rect(665, 620, 500, 10),
                                pygame.Rect(630, 70, 10, 595),
                                pygame.Rect(630, 170, 35, 10),
                                pygame.Rect(630, 490, 35, 10),
                                pygame.Rect(665, 70, 10, 525),
                                pygame.Rect(665, 100, 35, 10),
                                pygame.Rect(665, 195, 35, 10),
                                pygame.Rect(700, 70, 10, 525),
                                pygame.Rect(700, 270, 35, 10),
                                pygame.Rect(700, 540, 35, 10),
                                pygame.Rect(735, 70, 10, 525),
                                pygame.Rect(735, 370, 35, 10),
                                pygame.Rect(735, 120, 35, 10),
                                pygame.Rect(770, 70, 10, 525),
                                pygame.Rect(805, 430, 35, 10),
                                pygame.Rect(805, 320, 35, 10),
                                pygame.Rect(805, 70, 10, 525),
                                pygame.Rect(840, 35, 10, 560),
                                pygame.Rect(875, 70, 10, 560),
                                pygame.Rect(910, 70, 10, 525),
                                pygame.Rect(910, 70, 220, 10),
                                pygame.Rect(1120, 70, 10, 525),
                                pygame.Rect(910, 585, 220, 10),
                                pygame.Rect(430, 70, 210, 10),
                                pygame.Rect(210, 70, 165, 10),
                                pygame.Rect(70, 70, 100, 10),
                                pygame.Rect(170, 70, 10, 125),
                                pygame.Rect(70, 185, 100, 10),
                                pygame.Rect(170, 220, 10, 145),
                                pygame.Rect(205, 35, 10, 295),
                                pygame.Rect(170, 35, 35, 10),
                                pygame.Rect(205, 320, 190, 10),
                                pygame.Rect(395, 70, 10, 260),
                                pygame.Rect(365, 70, 10, 230),
                                pygame.Rect(335, 70, 10, 230),
                                pygame.Rect(305, 70, 10, 230),
                                pygame.Rect(275, 70, 10, 230),
                                pygame.Rect(245, 70, 10, 230),
                                pygame.Rect(170, 355, 225, 10),
                                pygame.Rect(430, 70, 10, 260),
                                pygame.Rect(395, 355, 10, 245),
                                pygame.Rect(205, 590, 190, 10),
                                pygame.Rect(105, 630, 365, 10),
                                pygame.Rect(70, 220, 100, 10),
                                pygame.Rect(70, 355, 100, 10),
                                pygame.Rect(70, 390, 100, 10),
                                pygame.Rect(70, 555, 100, 10),
                                pygame.Rect(70, 590, 135, 10),
                                pygame.Rect(195, 530, 10, 70),
                                pygame.Rect(105, 520, 100, 10),
                                pygame.Rect(105, 425, 10, 95),
                                pygame.Rect(105, 425, 100, 10),
                                pygame.Rect(195, 365, 10, 70),
                                pygame.Rect(170, 355, 35, 10),
                                pygame.Rect(70, 70, 10, 115),
                                pygame.Rect(70, 220, 10, 135),
                                pygame.Rect(70, 390, 10, 165),
                                pygame.Rect(70, 590, 10, 75),
                                pygame.Rect(70, 655, 400, 10),
                                pygame.Rect(505, 655, 685, 10),
                                pygame.Rect(470, 655, 10, 35),
                                pygame.Rect(430, 355, 10, 255),
                                pygame.Rect(430, 355, 85, 10),
                                pygame.Rect(530, 355, 100, 10),
                                pygame.Rect(465, 100, 10, 260),
                                pygame.Rect(489, 100, 10, 230),
                                pygame.Rect(513, 100, 10, 230),
                                pygame.Rect(537, 100, 10, 230),
                                pygame.Rect(564, 100, 10, 230),
                                pygame.Rect(587, 100, 10, 230),
                                pygame.Rect(606, 100, 10, 230),
                                pygame.Rect(460, 385, 10, 255),   
                                pygame.Rect(460, 385, 140, 10),
                                pygame.Rect(600, 385, 10, 100),
                                pygame.Rect(600, 515, 10, 125),
                                pygame.Rect(580, 515, 10, 125),
                                pygame.Rect(560, 425, 10, 215),
                                pygame.Rect(540, 425, 10, 215),
                                pygame.Rect(520, 425, 10, 215),
                                pygame.Rect(500, 425, 10, 215)]
                            # draws all of the necessary rectangles on the maze
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
                            # for statement to detect collisions
                            for rect in rectangle_list:
                                pygame.draw.rect(screen, green, rect, -1)
                                if sprite.colliderect(rect):
                                    # create new font size
                                    font = pygame.font.SysFont("Arial", 50)
                                    # create text using the font - LOSE MESSAGE
                                    text1 = font.render("Your skills ran into a problem. :(", True, (255,255,255))
                                    # create a display
                                    screen = pygame.display.set_mode( (800, 200) )
                                    # fill the screen with blue
                                    screen.fill((0,0,255))
                                    # draw text to screen
                                    screen.blit(text1, (20, 20) )
                                    # update the display
                                    pygame.display.flip()
                                    # 10 second delay
                                    time.sleep(10)
                                    # close the game
                                    sys.quit()
                            # sets win condition
                            if y >= 685:
                                # create new font size
                                font = pygame.font.SysFont("Arial", 50)
                                # create text using the font
                                text1 = font.render("Your skills succeeded this time. :)", True, (black))
                                # create a display
                                screen = pygame.display.set_mode( (800, 200) )
                                # fill the screen with lime
                                screen.fill((lime))
                                # draw text to screen
                                screen.blit(text1, (20, 20) )
                                # update the display
                                pygame.display.flip()
                                # 10 second delay
                                time.sleep(10)
                                # close the game
                                sys.quit()
                            pygame.display.update()