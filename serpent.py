import pygame

class Serpent:
    
    def __init__(self, name, block_size, start_x, start_y):

        self._name = name
        self._block_size = block_size
        self._length = 3
        self.body = []
        for i in range(self._length):
            self.body.append([start_x - i * 20, start_y])

    def __str__(self):
        return f"Serpent: {self.name}"

    @property
    def length(self):
        return self._length

    def increment_length(self):
        self._length += 1

    @property
    def name(self):
        return self._name
    
    @property
    def body(self):
        return self._body
    
    @body.setter
    def body(self, value):
        self._body = value

    def draw(self, screen, colour):
        """Draw the serpent on the screen."""
        for segment in self.body:
            pygame.draw.rect(screen, colour, [segment[0], segment[1], self._block_size, self._block_size])

    def update(self, head):
        """Update the serpent body."""
        self.body.append(head) # Add new head to the body
        if len(self.body) > self.length:
            # Remove the tail segment if the serpent is longer than its length
            self.body.pop(0)  # Remove the tail

        
    def eat(self):
        """eat food."""
        eat_sound = pygame.mixer.Sound("sounds/snake.mp3")  
        eat_sound.play()  # Play the sound when the serpent eats food
