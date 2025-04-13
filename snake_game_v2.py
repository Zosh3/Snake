import pygame

"""
This adds the standard pygame loop, check for a QUIT event.
It uses the while, for and if keywords
"""
# Set up constants for colours
# Each colour is a tuple of Red, Green,  Blue  values.  Each value can range from 0 to 255.
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

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
    for event in pygame.event.get():
        print(f"event: type: {event.type} dictionary items: {event.dict.items()}")  # Print the event to see what is happening
        if event.type == pygame.QUIT:
            game_over = True

    # Fill the background with black
    screen.fill(BLACK)

    # Draw a green square (the snake) at the center of the screen
    pygame.draw.rect(screen, GREEN, [320, 240, 20,20])

    pygame.display.update()

    clock.tick(5) # Limit the frame rate to 5 FPS

pygame.quit()