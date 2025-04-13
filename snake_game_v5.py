import pygame
from snake1 import Snake1

"""
This introduces functionality to move the snake with the user's keyboard input (up / down / left / right keys).
"""
# Set up constants for colours
# Each colour is a tuple of COLOUR_RED, COLOUR_GREEN,  Blue  values.  Each value can range from 0 to 255.
# Set up constants for colours
# Each colour is a tuple of COLOUR_RED, COLOUR_GREEN,  Blue  values.  Each value can range from 0 to 255.
COLOUR_GREEN = (0, 255, 0)
COLOUR_BLACK = (0, 0, 0)
COLOUR_RED = (255, 0, 0)
COLOUR_BLUE = (0, 0, 255)
COLOUR_YELLOW = (255, 255, 0)
COLOUR_ORANGE = (255, 165, 0)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_HEIGHT = 480
SCREEN_CENTRE_X = SCREEN_WIDTH // 2
SCREEN_CENTRE_Y = SCREEN_HEIGHT // 2

FRAME_RATE = 10  # Frame rate in frames per second (FPS)

SNAKE_SIZE = 20
SNAKE_SPEED = 5  # Speed of the snake

snake_x = SCREEN_CENTRE_X  # Initial x position of the snake
snake_y = SCREEN_CENTRE_Y  # Initial y position of the snake

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

    # Create an instance of the snake class and draw it
slippy = Snake1(colour, snake_x, snake_y)

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
            elif event.key == pygame.K_UP:
                snake_y -= SNAKE_SPEED  # Move up
            elif event.key == pygame.K_DOWN:    
                snake_y += SNAKE_SPEED
            elif event.key == pygame.K_LEFT:    
                snake_x -= SNAKE_SPEED
            elif event.key == pygame.K_RIGHT:    
                snake_x += SNAKE_SPEED
    screen.fill(COLOUR_BLACK)

    slippy.x = snake_x  # Update the snake's x position
    slippy.y = snake_y  # Update the snake's y position
    slippy.draw(screen)

    pygame.display.update()

    clock.tick(FRAME_RATE) # Limit the frame rate to SNAKE_SPEED FPS 

pygame.quit()