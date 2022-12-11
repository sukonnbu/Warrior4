import pygame
from variables import *


class Background():
    def __init__(self, screen):
        self.image = pygame.image.load("assets/BG.png")
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.rect = (0, 0)

        self.screen = screen

    def fill_bg(self):

        if self.rect[0] <= -WIDTH:
            self.rect = (WIDTH, 0)

        self.rect = (self.rect[0] - 1, self.rect[1])
        self.screen.blit(self.image, self.rect)
