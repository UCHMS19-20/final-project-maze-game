# import pygame
 
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# BLUE = (0, 0, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# PURPLE = (255, 0, 255)
 
 
# class Wall(pygame.sprite.Sprite):
#     """This class represents the bar at the bottom that the player controls """
 
#     def __init__(self, x, y, width, height, color):
#         """ Constructor function """
 
#         # Call the parent's constructor
#         super().__init__()
 
#         # Make a BLUE wall, of the size specified in the parameters
#         self.image = pygame.Surface([width, height])
#         self.image.fill(color)
 
#         # Make our top-left corner the passed-in location.
#         self.rect = self.image.get_rect()
#         self.rect.y = y
#         self.rect.x = x
 
 
# class Player(pygame.sprite.Sprite):
#     """ This class represents the bar at the bottom that the
#     player controls """
 
#     # Set speed vector
#     change_x = 0
#     change_y = 0
 
#     def __init__(self, x, y):
#         """ Constructor function """
 
#         # Call the parent's constructor
#         super().__init__()
 
#         # Set height, width
#         self.image = pygame.Surface([15, 15])
#         self.image.fill(GREEN)
 
#         # Make our top-left corner the passed-in location.
#         self.rect = self.image.get_rect()
#         self.rect.y = y
#         self.rect.x = x
 
#     def changespeed(self, x, y):
#         """ Change the speed of the player. Called with a keypress. """
#         self.change_x += x
#         self.change_y += y
 
#     def move(self, walls):
#         """ Find a new position for the player """
 
#         # Move left/right
#         self.rect.x += self.change_x
 
#         # Did this update cause us to hit a wall?
#         block_hit_list = pygame.sprite.spritecollide(self, walls, False)
#         for block in block_hit_list:
#             # If we are moving right, set our right side to the left side of
#             # the item we hit
#             if self.change_x > 0:
#                 self.rect.right = block.rect.left
#             else:
#                 # Otherwise if we are moving left, do the opposite.
#                 self.rect.left = block.rect.right
 
#         # Move up/down
#         self.rect.y += self.change_y
 
#         # Check and see if we hit anything
#         block_hit_list = pygame.sprite.spritecollide(self, walls, False)
#         for block in block_hit_list:
 
#             # Reset our position based on the top/bottom of the object.
#             if self.change_y > 0:
#                 self.rect.bottom = block.rect.top
#             else:
#                 self.rect.top = block.rect.bottom
 
 
# class Room(object):
#     """ Base class for all rooms. """
 
#     # Each room has a list of walls, and of enemy sprites.
#     wall_list = None
#     enemy_sprites = None
 
#     def __init__(self):
#         """ Constructor, create our lists. """
#         self.wall_list = pygame.sprite.Group()
#         self.enemy_sprites = pygame.sprite.Group()
 
 
# class Room1(Room):
#     """This creates all the walls in room 1"""
#     def __init__(self):
#         super().__init__()
#         # Make the walls. (x_pos, y_pos, width, height)
 
#         # This is a list of walls. Each is in the form [x, y, width, height]
#         walls = [[0, 0, 20, 250, WHITE],
#                  [0, 350, 20, 250, WHITE],
#                  [780, 0, 20, 250, WHITE],
#                  [780, 350, 20, 250, WHITE],
#                  [20, 0, 760, 20, WHITE],
#                  [20, 580, 760, 20, WHITE],
#                  [390, 50, 20, 500, BLUE]
#                 ]
 
#         # Loop through the list. Create the wall, add it to the list
#         for item in walls:
#             wall = Wall(item[0], item[1], item[2], item[3], item[4])
#             self.wall_list.add(wall)
 
 
# class Room2(Room):
#     """This creates all the walls in room 2"""
#     def __init__(self):
#         super().__init__()
 
#         walls = [[0, 0, 20, 250, RED],
#                  [0, 350, 20, 250, RED],
#                  [780, 0, 20, 250, RED],
#                  [780, 350, 20, 250, RED],
#                  [20, 0, 760, 20, RED],
#                  [20, 580, 760, 20, RED],
#                  [190, 50, 20, 500, GREEN],
#                  [590, 50, 20, 500, GREEN]
#                 ]
 
#         for item in walls:
#             wall = Wall(item[0], item[1], item[2], item[3], item[4])
#             self.wall_list.add(wall)
 
 
# class Room3(Room):
#     """This creates all the walls in room 3"""
#     def __init__(self):
#         super().__init__()
 
#         walls = [[0, 0, 20, 250, PURPLE],
#                  [0, 350, 20, 250, PURPLE],
#                  [780, 0, 20, 250, PURPLE],
#                  [780, 350, 20, 250, PURPLE],
#                  [20, 0, 760, 20, PURPLE],
#                  [20, 580, 760, 20, PURPLE]
#                 ]
 
#         for item in walls:
#             wall = Wall(item[0], item[1], item[2], item[3], item[4])
#             self.wall_list.add(wall)
 
#         for x in range(100, 800, 100):
#             for y in range(50, 451, 300):
#                 wall = Wall(x, y, 20, 200, RED)
#                 self.wall_list.add(wall)
 
#         for x in range(150, 700, 100):
#             wall = Wall(x, 200, 20, 200, WHITE)
#             self.wall_list.add(wall)
 
 
# def main():
#     """ Main Program """
 
#     # Call this function so the Pygame library can initialize itself
#     pygame.init()
 
#     # Create an 800x600 sized screen
#     screen = pygame.display.set_mode([800, 600])
 
#     # Set the title of the window
#     pygame.display.set_caption('Maze Runner')
 
#     # Create the player paddle object
#     player = Player(50, 50)
#     movingsprites = pygame.sprite.Group()
#     movingsprites.add(player)
 
#     rooms = []
 
#     room = Room1()
#     rooms.append(room)
 
#     room = Room2()
#     rooms.append(room)
 
#     room = Room3()
#     rooms.append(room)
 
#     current_room_no = 0
#     current_room = rooms[current_room_no]
 
#     clock = pygame.time.Clock()
 
#     done = False
 
#     while not done:
 
#         # --- Event Processing ---
 
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 done = True
 
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         player.changespeed(-5, 0)
            #     if event.key == pygame.K_RIGHT:
            #         player.changespeed(5, 0)
            #     if event.key == pygame.K_UP:
            #         player.changespeed(0, -5)
            #     if event.key == pygame.K_DOWN:
            #         player.changespeed(0, 5)
 
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT:
            #         player.changespeed(5, 0)
            #     if event.key == pygame.K_RIGHT:
            #         player.changespeed(-5, 0)
            #     if event.key == pygame.K_UP:
            #         player.changespeed(0, 5)
            #     if event.key == pygame.K_DOWN:
            #         player.changespeed(0, -5)
 
# # # #         # --- Game Logic ---
 
# # # #         player.move(current_room.wall_list)
 
# # # #         if player.rect.x < -15:
# # # #             if current_room_no == 0:
# # # #                 current_room_no = 2
# # # #                 current_room = rooms[current_room_no]
# # # #                 player.rect.x = 790
# # # #             elif current_room_no == 2:
# # # #                 current_room_no = 1
# # # #                 current_room = rooms[current_room_no]
# # # #                 player.rect.x = 790
# # # #             else:
# # # #                 current_room_no = 0
# # # #                 current_room = rooms[current_room_no]
# # # #                 player.rect.x = 790
 
# # # #         if player.rect.x > 801:
# # # #             if current_room_no == 0:
# # # #                 current_room_no = 1
# # # #                 current_room = rooms[current_room_no]
# # # #                 player.rect.x = 0
# # # #             elif current_room_no == 1:
# # # #                 current_room_no = 2
# # # #                 current_room = rooms[current_room_no]
# # # #                 player.rect.x = 0
# # # #             else:
# # # #                 current_room_no = 0
# # # #                 current_room = rooms[current_room_no]
# # # #                 player.rect.x = 0
 
# # # #         # --- Drawing ---
# # # #         screen.fill(BLACK)
 
# # # #         movingsprites.draw(screen)
# # # #         current_room.wall_list.draw(screen)
 
# # # #         pygame.display.flip()
 
# # # #         clock.tick(60)
 
# # # #     pygame.quit()
 
# # # # if __name__ == "__main__":
# # # #     main()

# # # import sys, pygame
# # # pygame.init()

# # # size = width, height = 320, 240
# # # speed = [2, 2]
# # # black = 0, 0, 0

# # # screen = pygame.display.set_mode(size)

# # # ball = pygame.image.load("intro_ball.gif")
# # # ballrect = ball.get_rect()

# # # while 1:
# # #     for event in pygame.event.get():
# # #         if event.type == pygame.QUIT: sys.exit()

# # #     ballrect = ballrect.move(speed)
# # #     if ballrect.left < 0 or ballrect.right > width:
# # #         speed[0] = -speed[0]
# # #     if ballrect.top < 0 or ballrect.bottom > height:
# # #         speed[1] = -speed[1]

# # #     screen.fill(black)
# # #     screen.blit(ball, ballrect)
# # #     pygame.display.flip()

# import sys
# import pygame

# #must call before anything else for other functions to work
# pygame.init()

# #creates the display screen with the desired size
# screen = pygame.display.set_mode( (600, 400) )

# #set-up the colors based on RGB table
# white = pygame.Color(255,255,255)
# black = pygame.Color(0,0,0)
# red = pygame.Color(255,0,0)

# #creates variables for player position
# player_x = 260
# player_y = 150

# # Main loop, game goes inside this loop
# while True:
#     # do something for each event in the event queue
#     for event in pygame.event.get():
#         # Check to see if the current event is a QUIT event
#         if event.type == pygame.QUIT:
#             # If so, exit the program
#             sys.exit()
#         #checks to see if current event is a key being pressed
#         elif event.type == pygame.KEYDOWN:
#             #is the key being pressed the left arrow?
#             if event.key == pygame.K_LEFT:
#                 #if so move the x positon to the left
#                 player_x -= 10
#                 # screen.blit(player, (player_x, player_y))
#             #is the key being pressed yhe right arrow
#             elif event.key == pygame.K_RIGHT:
#                 #if so move the x position to the right
#                 player_x += 10
#                 # screen.blit(player, (player_x, player_y))
#             elif event.key == pygame.K_UP:
#                 player_y -= 10
#             elif event.key == pygame.K_DOWN:
#                 player_y += 10

#         #makes the display screen white
#         screen.fill(white)
#         pygame.display.flip()

#         #draws the rectangle which the player can move
#         pygame.draw.rect(screen, red, (player_x, player_y, 25, 25))
        
#         #redraws the entire screen
#         pygame.display.update()

import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30
n = 1
pygame.key.set_repeat()
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 1
        if pressed[pygame.K_DOWN]: y += 1
        if pressed[pygame.K_LEFT]: x -= 1
        if pressed[pygame.K_RIGHT]: x += 1

        screen.fill((0, 0, 0))
        
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        
        pygame.display.flip()