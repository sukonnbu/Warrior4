import pygame
from variables import *


class ChargeBar():
    def __init__(self):
        self.width = 0
        self.color = (0, 240, 0)

        self.max_hp = 5000
        self.current_hp = 5000
        self.hp_bar_length = WIDTH
        self.hp_ratio = self.max_hp / self.hp_bar_length
        self.hp_speed_low = 20
        self.hp_speed_high = 100

    def update(self, screen, hp):
        self.width = hp / self.hp_ratio

        transition_width = 0
        transition_color = (255, 255, 0)

        if self.current_hp < hp:
            self.current_hp += self.hp_speed_low
            transition_width = int((hp - self.current_hp)/self.hp_ratio)

        elif self.current_hp > hp:
            if self.current_hp - hp >= 500:
                self.current_hp -= self.hp_speed_high
            else:
                self.current_hp -= self.hp_speed_low

            transition_width = int((self.current_hp - hp)/self.hp_ratio)

        pygame.draw.rect(screen, self.color, (0, 0, self.width, 20))
        pygame.draw.rect(screen, transition_color,
                         (self.width, 0, transition_width, 20))
        pygame.draw.rect(screen, (50, 50, 50), (0, 0, WIDTH, 20), 5)
