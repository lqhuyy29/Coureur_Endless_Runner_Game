import pygame

coureur_images = [pygame.image.load(f'assets/coureur/{i}.png') for i in range(1, 13)]

COUREUR_WIDTH = 156
COUREUR_HEIGHT = 122

class Player:
    """
    Represents the player character in the game.
    """
    def __init__(self):
        self.images = coureur_images
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (360, (240 + 720) // 2)
        self.speed = 5
        self.limit_left = 0
        self.limit_right = 1280
        self.limit_top = 360 - COUREUR_HEIGHT + 4
        self.limit_bottom = 720 - 4
        self.frame_count = 0

    def move(self, dx, dy):
        """
        Moves the player character by the specified amount while ensuring it stays within the movement limits.
        """
        self.rect.x += dx
        self.rect.y += dy
        if self.rect.left < self.limit_left:
            self.rect.left = self.limit_left
        if self.rect.right > self.limit_right:
            self.rect.right = self.limit_right
        if self.rect.top < self.limit_top:
            self.rect.top = self.limit_top
        if self.rect.bottom > self.limit_bottom:
            self.rect.bottom = self.limit_bottom

    def update(self, keys):
        """
        Updates the state of the player character based on the pressed keys and manages the animation.
        """
        dx, dy = 0, 0
        if keys[pygame.K_UP]:
            dy = -self.speed
        if keys[pygame.K_DOWN]:
            dy = self.speed
        if keys[pygame.K_LEFT]:
            dx = -self.speed
        if keys[pygame.K_RIGHT]:
            dx = self.speed
        self.move(dx, dy)
        self.frame_count += 1
        if self.frame_count % 5 == 0:
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
            self.frame_count = 0