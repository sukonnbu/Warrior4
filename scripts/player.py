import pygame
import random
from variables import *


mass = 2
velocity = 0

image1 = pygame.image.load("assets/1.png")
image1 = pygame.transform.scale(image1, (150, 225))
image2 = pygame.image.load("assets/3.png")
image2 = pygame.transform.scale(image2, (150, 225))
image3 = pygame.image.load("assets/2.png")
image3 = pygame.transform.scale(image3, (155, 225))
image4 = image2

image_jump = pygame.image.load("assets/jump.png")
image_jump = pygame.transform.scale(image_jump, (170, 235))


class Player():

    def __init__(self):
        self.image = ""
        self.set_img = 0

        self.rect = ""

        self.change_image = 0

        self.JUMP = 0
        self.vel = 0
        self.mass = mass

        self.hp = 5000

        self.colliding = False

    def init(self, vel):
        global velocity, image1

        self.image = image1
        self.set_img = 1

        self.rect = self.image.get_rect()

        self.rect.x = 50
        self.rect.bottom = HEIGHT - 10
        velocity = vel
        self.vel = velocity

    def draw_player(self, screen):
        screen.blit(self.image, [self.rect.x, self.rect.y])

    def jump(self, j):
        self.JUMP = j

    def update(self):
        global velocity, image1, image2, image3, image4, image_jump

        if self.JUMP > 0:

            self.image = image_jump

            if self.JUMP == 2:
                self.vel = velocity

            F = 0.5 * self.mass * self.vel ** 2
            if self.vel < 0:
                F = -F

            self.rect.y -= round(F)

            self.vel -= 1

            if self.rect.bottom > HEIGHT - 10:
                self.image = image1
                self.set_img = 1

                self.rect.bottom = HEIGHT - 10
                self.JUMP = 0
                self.vel = velocity

            if self.rect.top < 0:
                self.rect.top = 0

        elif self.JUMP == 0:
            if self.change_image == 10:
                self.change_image = 0

                if self.set_img == 1:
                    self.image = image2
                    self.set_img = 2

                elif self.set_img == 2:
                    self.image = image3
                    self.set_img = 3

                elif self.set_img == 3:
                    self.image = image4
                    self.set_img = 4

                elif self.set_img == 4:
                    self.image = image1
                    self.set_img = 1
            else:
                self.change_image += 1

    def collide(self, type: str):
        if not self.colliding:
            if type == "iron":
                self.hp -= 100
            elif type == "bullet":
                self.hp -= 250
            elif type == "tan":
                if self.hp > 1000:
                    self.hp = 1000
                else:
                    self.hp -= 700
            elif type == "anticarbon":
                rand = random.random()

                if rand <= 0.5:
                    self.hp -= 500
                elif rand <= 0.8:
                    self.hp -= 2000
                else:
                    self.hp = 0
            else:
                self.hp = 0

    def set_collide_state(self, state: bool):
        self.collideing = state
