import pygame 
import random


# Global Variables: 

# Colors: 
class colors: 
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    WHITE = (255,255,255)
    BLACK = (0,0,0)

# Data Collection: 
class data_collection: 
    loop_counter = 0
    levels_cleared = 0
    levels_cleared_names = []


# Pygame Variables:
pygame.init()


# Screen Size: 
width = 400
height = 400

# Create the game window
screen = pygame.display.set_mode((width, height))

# Game Loop 
run = True # If this is set to true the game will be running

while run == True: 

    # Make the Background White
    screen.fill(colors.WHITE)

    # Update the display each tick
    pygame.display.update()

    # Event Listener: 
    for event in pygame.event.get():
        # Listen for the quit event 
        if event.type == pygame.QUIT: 
            run = False # Setting this to false will break the loop
        # Any Other Event Listeners:






pygame.quit()