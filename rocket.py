import pygame
from pygame.sprite import Sprite

class Rocket(Sprite):
    """A class to manage the rocket."""

    def __init__(self, ai_game):
        """Initialize the rocket and set its starting position."""
        super().__init__()  # Call the __init__ method of the Sprite class
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the rocket and get its rect.
        self.image = pygame.image.load('rocket2.bmp')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()

        # Start each new rocket at the bottom left of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the rocket's vertical position
        self.y = float(self.rect.y)

        # Set the rocket speed
        self.rocket_speed = 1.5

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def center_rocket(self):
        """Center the rocket on the screen"""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

    def update(self):
        """Update the rocket's position based on the movement flag."""
        # Update the rocket's y value, not the rect.
        if self.moving_up and self.rect.top > 0:
            self.y -= self.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.rocket_speed

        # Update rect object
        self.rect.y = self.y

    def blitme(self):
        """Draw the image at its current location."""
        self.screen.blit(self.image, self.rect)
