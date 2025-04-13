import pygame
import random  # Import the random module
from serpent import Serpent

# Screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

SCREEN_CENTRE_X = SCREEN_WIDTH // 2
SCREEN_CENTRE_Y = SCREEN_HEIGHT // 2

# Colors (using RGB tuples)
COLOUR_BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLOUR_GREEN = (0, 255, 0)
COLOUR_RED = (255, 0, 0)
COLOUR_BLUE = (0, 0, 255)

## Set out the geometry of the game

# Snake properties
SNAKE_BLOCK_SIZE = 20 # must be a factor of both screen width and height
SNAKE_SPEED = 5  # Controls how fast the snake moves (frames per second)

# def get_random_colour():
#     """Generate a random colour."""
#     return random.choice([COLOUR_GREEN, WHITE, COLOUR_RED, COLOUR_BLUE])

# random_colour = get_random_colour()

# print("Initial random colour:", random_colour)  # Print the random colour+

# Function to generate random food coordinates
def generate_food():
    # food_x = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK_SIZE) / 20.0) * 20.0
    # food_y = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK_SIZE) / 20.0) * 20.0
    food_x = random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE)
    food_y = random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE)
    print("Food coordinates:", food_x, food_y)
    return food_x, food_y

# Initial food position
food_x, food_y = generate_food()

# Initial snake position
snake_x = SCREEN_CENTRE_X
snake_y = SCREEN_CENTRE_Y

# Initial snake length
snake_length = 3

# Initial snake body is horizontal three cells long
slippy = Serpent("Slippy", SNAKE_BLOCK_SIZE, SCREEN_CENTRE_X, SCREEN_CENTRE_Y)
print(slippy)


# Initial direction (start moving right)
direction_x = 0 #SNAKE_BLOCK_SIZE
direction_y = 0

# Initial food position
food_x, food_y = generate_food()

# Initialize Pygame
pygame.init()
pygame.mixer.init()  # Initialize the mixer module

# Draw the food
def draw_food():
    """Draw the food on the screen."""
    pygame.draw.rect(screen, COLOUR_RED, [food_x, food_y, SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE])

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Python Snake Game")

# Load the eating sound
eat_sound = pygame.mixer.Sound("sounds/snake.mp3")  

clock = pygame.time.Clock()

# Game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        # while moving up or down, only left or right is allowed but not reverse direction
        # while moving left or right, only up or down is allowed but not reverse direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction_x == 0:
                direction_x = -SNAKE_BLOCK_SIZE
                direction_y = 0
            elif event.key == pygame.K_RIGHT and direction_x == 0:
                direction_x = SNAKE_BLOCK_SIZE
                direction_y = 0
            elif event.key == pygame.K_UP and direction_y == 0:
                direction_y = -SNAKE_BLOCK_SIZE
                direction_x = 0
            elif event.key == pygame.K_DOWN and direction_y == 0:
                direction_y = SNAKE_BLOCK_SIZE
                direction_x = 0

        print(f"Update on direction: {direction_x}, {direction_y}")

    # Update snake's head position
    snake_x += direction_x
    snake_y += direction_y

 # Check for boundary collision
    if snake_x >= SCREEN_WIDTH or snake_x < 0 or snake_y >= SCREEN_HEIGHT or snake_y < 0:
        game_over = True

     # Check if snake eats the food
    if snake_x == food_x and snake_y == food_y:
        food_x, food_y = generate_food()
        slippy.increment_length()
        slippy.eat()

    # Update snake body
    snake_head = [snake_x, snake_y]

    slippy.update(snake_head)

    print(f"Slippy: {slippy} ")

    # Check for collisions with the walls

  # Fill the background with black
    screen.fill(COLOUR_BLACK)

    draw_food()
    #pygame.draw.rect(screen, COLOUR_RED, [food_x, food_y, SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE])

    # Draw the snake
    slippy.draw(screen, COLOUR_GREEN)

    # Keep the window open (we'll add drawing here later)
    pygame.display.update()
    clock.tick(SNAKE_SPEED)

# Quit Pygame
pygame.quit()