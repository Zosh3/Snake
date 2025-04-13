import pygame
from snake import Snake
from game_constants import COLOUR_BLACK, COLOUR_GREEN
from game_constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_CENTRE_X, SCREEN_CENTRE_Y
from game_constants import FRAME_RATE
from game_constants import  KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from game_constants import KEY_COLOUR_MAP
from game_constants import SNAKE_DIRECTION_UP, SNAKE_DIRECTION_DOWN, SNAKE_DIRECTION_LEFT, SNAKE_DIRECTION_RIGHT

"""
Change the functionality so that the snake continues to move in the direction of the last key pressed, even when the key is released.
"""

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
slippy = Snake(colour, snake_x, snake_y)

game_over = False
while not game_over:
    for event in pygame.event.get():
        #print(event)  # Print the event to see what is happening
        if event.type == pygame.QUIT:
            game_over = True
        if slippy.is_on_screen() == False:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key in KEY_COLOUR_MAP:
                slippy.colour = KEY_COLOUR_MAP[event.key]
            elif event.key == KEY_UP:
                slippy.direction = SNAKE_DIRECTION_UP
            elif event.key == KEY_DOWN:    
                slippy.direction = SNAKE_DIRECTION_DOWN
            elif event.key == KEY_LEFT:    
                slippy.direction = SNAKE_DIRECTION_LEFT
            elif event.key == KEY_RIGHT:    
                slippy.direction = SNAKE_DIRECTION_RIGHT

    screen.fill(COLOUR_BLACK)
    slippy.move2()  # Move the snake in the current direction
    slippy.draw(screen)

    pygame.display.update()

    clock.tick(FRAME_RATE) # Limit the frame rate to SNAKE_SPEED FPS 

pygame.quit()