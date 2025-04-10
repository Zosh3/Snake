import pygame
import random  # Import the random module

# Initialize Pygame
pygame.init()
pygame.mixer.init()  # Initialize the mixer module

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors (using RGB tuples)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake properties
SNAKE_BLOCK_SIZE = 20
SNAKE_SPEED = 5  # Controls how fast the snake moves (frames per second)

random_colour = random.choice([GREEN, WHITE, RED])
print("Random colour:", random_colour)  # Print the random colour+

# Function to generate random food coordinates
def generate_food():
    food_x = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK_SIZE) / 20.0) * 20.0
    food_y = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK_SIZE) / 20.0) * 20.0
    print("Food coordinates:", food_x, food_y)
    return food_x, food_y

# Initial food position
food_x, food_y = generate_food()

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Python Snake Game")

# Initial snake position
snake_x = SCREEN_WIDTH // 2
snake_y = SCREEN_HEIGHT // 2

# Initial snake length
snake_length = 3

# Initial snake body
snake_body = []
for i in range(snake_length):
    snake_body.append([snake_x - i * SNAKE_BLOCK_SIZE, snake_y])

print(snake_body)
print("Hello")

# Initial direction (start moving right)
direction_x = 0 #SNAKE_BLOCK_SIZE
direction_y = 0

# Initial food position
food_x, food_y = generate_food()

# Load the eating sound
eat_sound = pygame.mixer.Sound("sounds/snake.mp3")  

clock = pygame.time.Clock()

# Game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
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

        print("Update on direction",direction_x, direction_y)

    # Update snake's head position
    snake_x += direction_x
    snake_y += direction_y

 # Check for boundary collision
    if snake_x >= SCREEN_WIDTH or snake_x < 0 or snake_y >= SCREEN_HEIGHT or snake_y < 0:
        game_over = True

     # Check if snake eats the food
    if snake_x == food_x and snake_y == food_y:
        food_x, food_y = generate_food()
        snake_length += 1  # Increase snake length
        random_colour = random.choice([GREEN, WHITE, RED])
        eat_sound.play()  # Play the eating sound


    # Update snake body
    snake_head = [snake_x, snake_y]
    snake_body.append(snake_head)
    # Remove the tail if the snake's length exceeds the initial length
    if len(snake_body) > snake_length:
        del snake_body[0]

    print(f"Snake head: {snake_head} length {len(snake_body)}")
    # Check for collisions with the walls

  # Fill the background with black
    screen.fill(BLACK)

     # Draw the food
    pygame.draw.rect(screen, RED, [food_x, food_y, SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE])

    # Draw the snake
    for segment in snake_body:
        pygame.draw.rect(screen, random_colour, [segment[0], segment[1], SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE])

    # Keep the window open (we'll add drawing here later)
    pygame.display.update()
    clock.tick(SNAKE_SPEED)

# Quit Pygame
pygame.quit()