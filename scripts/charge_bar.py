import pygame
from variables import *


class ChargeBar():
    def __init__(self):
        self.width = 0
        self.color = (0, 150, 240)

        self.max_charge = 500
        self.current_charge = 300
        self.charge_bar_length = WIDTH / 5
        self.charge_ratio = self.max_charge / self.charge_bar_length
        self.charge_speed = 20

    def update(self, screen, charge):
        self.width = charge / self.charge_ratio

        transition_width = 0
        transition_color = (240, 240, 240)

        if self.current_charge < charge:
            self.current_charge += 1
            transition_width = int(
                (charge - self.current_charge)/self.charge_ratio)

        elif self.current_charge > charge:
            self.current_charge -= self.charge_speed

            transition_width = int(
                (self.current_charge - charge)/self.charge_ratio)

        pygame.draw.rect(screen, self.color, (0, 20, self.width, 20))
        pygame.draw.rect(screen, transition_color,
                         (self.width, 20, transition_width, 20))
        pygame.draw.rect(screen, (50, 50, 50),
                         (0, 20, self.charge_bar_length, 20), 5)
