import pygame

"""
This introduces functionality to change what's on the screen with the user's keyboard input.
It uses the pygame.KEYDOWN event to check for key presses and change the colour of the snake.
B=Blue, G=Green, R=Red, Y=Yellow, O=Orange, The default is Green.
"""
# Set up constants for colours
# Each colour is a tuple of Red, Green,  Blue  values.  Each value can range from 0 to 255.
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Initialize Pygame
pygame.init()
# Initialize the mixer module (which is used for sound)
pygame.mixer.init()  

# Create the game window
screen = pygame.display.set_mode((640, 480))

# Set the title of the window
pygame.display.set_caption("Python Snake Game")

clock = pygame.time.Clock()

game_over = False
while not game_over:
    colour = GREEN  # Default colour
    for event in pygame.event.get():
        print(event)  # Print the event to see what is happening
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                colour = BLUE
            elif event.key == pygame.K_g:
                colour = GREEN
            elif event.key == pygame.K_r:
                colour = RED
            elif event.key == pygame.K_y:
                colour = YELLOW
            elif event.key == pygame.K_o:
                colour = ORANGE
            else:
                colour = GREEN

    screen.fill(BLACK)

    # Draw a green square (the snake) at the center of the screen
    pygame.draw.rect(screen, colour, [320, 240, 20,20])

    pygame.display.update()

    clock.tick(1) # Limit the frame rate to 1 FPS so we see a changed colour

pygame.quit()