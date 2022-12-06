import pygame
from variables import *

class Button():
    def __init__(self):
        self.image = ""
        self.image_on = ""
        self.image_off = ""
        self.rect = ""
    
    def init_button(self, on_dir:str, off_dir:str, pos: tuple):
        self.image_on = pygame.image.load(on_dir)
        self.image_on = pygame.transform.scale(self.image_on, (200, 70))
        self.image_off = pygame.image.load(off_dir)
        self.image_off = pygame.transform.scale(self.image_off, (200, 70))

        self.image = self.image_off
        self.rect = self.image.get_rect()

        self.rect.center = pos


    def update(self, mouse_on = False):
        if mouse_on:
            self.image = self.image_on
        else:
            self.image = self.image_off
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
