import pygame
from variables import *


class Coil():
    def __init__(self):
        self.image = pygame.image.load("assets/spark.png")
        self.rect = self.image.get_rect()
        self.is_visible = False
        self.state = 0
        self.charge = 0

    def update(self, y):
        if self.is_visible:
            self.rect.y = y
            self.state += 1

            if self.state >= 3:
                self.state = 0
                self.is_visible = False
        elif self.charge < 500:
            self.charge += 1

    def draw_coil(self, screen):
        if self.is_visible:
            screen.blit(self.image, self.rect)

    def fire_coil(self):
        if self.charge == 500:
            self.is_visible = True
            self.charge = 0
