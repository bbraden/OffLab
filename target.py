import pygame, sys
from pygame.locals import *


class targets(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y, height, width):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.rect.height = height
        self.rect.width = width
