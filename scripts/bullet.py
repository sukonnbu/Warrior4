import pygame
import random
from variables import *

speed = 0


class Bullet():
    def __init__(self):
        self.image = pygame.image.load("assets/bullet.png")
        self.image = pygame.transform.scale(self.image, (150, 50))
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT - 70

        self.is_visible = True

    def set_speed(self, obs_speed):
        global speed
        speed = obs_speed

    def init_pos(self, start=500, end=2000):
        setting = random.random()

        bottom = 0  # init

        if setting <= 0.5:
            self.type = "iron"
            self.image = pygame.transform.scale(
                pygame.image.load("assets/bullet.png"), (150, 75))
            bottom = HEIGHT - 5

        elif setting <= 0.8:
            self.type = "bullet"
            self.image = pygame.transform.scale(
                pygame.image.load("assets/bullet.png"), (150, 50))
            bottom = HEIGHT - 70

        elif setting <= 0.9:
            self.type = "tan"
            self.image = pygame.transform.scale(
                pygame.image.load("assets/bullet.png"), (100, 100))
            bottom = HEIGHT - 50

        elif setting <= 0.95:
            self.type = "anticarbon"
            self.image = pygame.transform.scale(
                pygame.image.load("assets/bullet.png"), (100, 100))
            bottom = HEIGHT - 50

        else:
            self.type = "nuclear"
            self.image = pygame.transform.scale(
                pygame.image.load("assets/bullet.png"), (150, 75))
            bottom = HEIGHT - 50

        self.rect = self.image.get_rect()

        self.rect.bottom = bottom
        self.rect.x = WIDTH + random.randint(start, end)

    def draw_bullet(self, screen):
        if self.is_visible:
            screen.blit(self.image, [self.rect.x, self.rect.y])
        else:
            self.init_pos()
            self.is_visible = True

    def update(self):
        global speed

        self.rect.x -= speed
        if self.rect.x < 0:
            self.is_visible = False

    def collide(self):
        self.is_visible = False
