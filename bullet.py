import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bulelts fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Create a bullet rect at (0,0) and set the correct position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = ai_game.rocket.rect.midright

        #Rotate the bullet by 90 degrees.
        self.image = pygame.Surface((self.rect.width, self.rect.height))
        self.image.fill(self.color)
        self.image = pygame.transform.rotate(self.image, 90)

        #Store the bullet's position as a decimal value
        self.x = float(self.rect.x)

    def update (self):
        """Move the bullet cross the screen"""
        #Update the decimal position of the bullet
        self.x += self.settings.bullet_speed
        #Update the rect position
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)
        

    
