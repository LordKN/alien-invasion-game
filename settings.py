import pygame

class Settings:
    """A class to store all settings for Alien Invasion 2."""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800

        #Background settings
        self.bg_color = (230, 230, 230)
        self.bg_image = 'space.jpg'
        self.background = pygame.image.load(self.bg_image)
        self.background_rect = self.background.get_rect()

        #rocket settings
        self.rocket_speed = 1.5
        self.rocket_limit = 3

        #Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        #Alien settings
        self.alien_speed = .07
        self.fleet_drop_speed = .05
        self.num_rows = 0

        #fleet_direction of 1 represents down; -1 represents up
        self.fleet_direction = 1

        #Number of aliens
        self.num_aliens = 80

        #How quickly the game speeds up
        self.speedup_scale = 1.1

        #How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.rocket_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed = 0.07

        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.rocket_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
