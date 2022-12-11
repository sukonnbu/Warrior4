import pygame

pygame.init()


screen_size = WIDTH, HEIGHT = 1000, 600
BG_COLOR = (255, 255, 255)

title_font = pygame.font.SysFont('freesanbold', 150, True)
def_font = pygame.font.SysFont('freesanbold.ttf', 75)

click_sound = pygame.mixer.Sound("assets/click.mp3")
hit_sound = pygame.mixer.Sound("assets/hit.mp3")
