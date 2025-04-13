import pygame

"""
This introduces functionality to change what's on the screen with the user's keyboard input.
It uses the pygame.KEYDOWN event to check for key presses and change the colour of the snake.
B=Blue, G=COLOUR_GREEN, R=COLOUR_RED, Y=COLOUR_YELLOW, O=COLOUR_ORANGE, The default is COLOUR_GREEN.

It also creates constants to make the  code more readable and easy to change when setting up the screen geometry and the snake's speed.

"""
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
SNAKE_SIZE = 20
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

    screen.fill(COLOUR_BLACK)

    # Draw a green square (the snake) at the center of the screen
    pygame.draw.rect(screen, colour, [SCREEN_CENTRE_X, SCREEN_CENTRE_Y, SNAKE_SIZE, SNAKE_SIZE])

    pygame.display.update()

    clock.tick(10) 

pygame.quit()