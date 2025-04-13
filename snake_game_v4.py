import pygame
from snake1 import Snake1

"""
This imports the basic snake class
"""
# Set up constants for colours
# Each colour is a tuple of red, green, blue  values.  Each value can range from 0 to 255.
COLOUR_GREEN = (0, 255, 0)
COLOUR_BLACK = (0, 0, 0)
COLOUR_RED = (255, 0, 0)
COLOUR_BLUE = (0, 0, 255)
COLOUR_YELLOW = (255, 255, 0)
COLOUR_ORANGE = (255, 165, 0)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_CENTRE_X = SCREEN_WIDTH // 2
SCREEN_CENTRE_Y = SCREEN_HEIGHT // 2

# Initialize Pygame
pygame.init()
# Initialize the mixer module (which is used for sound)
pygame.mixer.init()  

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Python Snake Game")

clock = pygame.time.Clock()

colour = COLOUR_GREEN  # Default colour

game_over = False
while not game_over:
    for event in pygame.event.get():
        #print(event)  # Print the event to see what is happening
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                colour = COLOUR_BLUE
            elif event.key == pygame.K_g:
                colour = COLOUR_GREEN
            elif event.key == pygame.K_r:
                colour = COLOUR_RED
            elif event.key == pygame.K_y:
                colour = COLOUR_YELLOW
            elif event.key == pygame.K_o:
                colour = COLOUR_ORANGE
            else:
                colour = COLOUR_GREEN

    screen.fill(COLOUR_BLACK)

    # Create an instance of the snake class and draw it
    slippy = Snake1(colour, SCREEN_CENTRE_X, SCREEN_CENTRE_Y)
    slippy.draw(screen)

    pygame.display.update()

    clock.tick(10) 

pygame.quit()