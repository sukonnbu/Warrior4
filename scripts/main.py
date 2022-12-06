import pygame
import player as pl
import object
import coil
import health_bar
import button
import sqlite3
import os
from variables import *


velocity = 0
obs_speed = 0


playing = False


pygame.init()


click_sound = pygame.mixer.Sound("assets/click.mp3")
hit_sound = pygame.mixer.Sound("assets/hit.mp3")


db_path = os.getenv('APPDATA') + "\.warrior4\warrior4.db"


conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS score (Score INTEGER);")


class Text():
    def __init__(self):
        self.color = (0, 0, 0)
        self.text = ""
        self.rect = ""

    def draw_text(self, text, rect):
        self.text = def_font.render(text, True, self.color)
        self.rect = rect
        screen.blit(self.text, self.rect)

    def text_color(self, color):
        self.color = color


class Background():
    def __init__(self):
        self.image = pygame.image.load("assets/BG.png")
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.rect = (0, 0)

    def fill_bg(self):

        if self.rect[0] <= -WIDTH:
            self.rect = (WIDTH, 0)

        self.rect = (self.rect[0] - 1, self.rect[1])
        screen.blit(self.image, self.rect)


def show_title():
    global playing

    Title = title_font.render("WARRIOR4", True, (150, 150, 150))
    Title2 = title_font.render("WARRIOR4", True, (50, 50, 50))

    title_image = pygame.image.load("assets/title.png")
    title_rect = title_image.get_rect()
    title_rect.center = (WIDTH / 2, HEIGHT / 2 - 50)

    screen.fill(BG_COLOR)

    screen.blit(Title2, (65, HEIGHT - 165))
    screen.blit(Title, (60, HEIGHT - 165))

    screen.blit(title_image, title_rect)

    start_button = button.Button()
    start_button.init_button("assets/start_button_on.png",
                             "assets/start_button_off.png", (850, HEIGHT - 120))

    turn_page = False
    mouse_on = False

    while not turn_page:

        mouse_pos = pygame.mouse.get_pos()
        is_click = pygame.mouse.get_pressed()

        if start_button.rect.x + 200 > mouse_pos[0] > start_button.rect.x and start_button.rect.y + 70 > mouse_pos[1] > start_button.rect.y:
            mouse_on = True

            if is_click[0]:
                click_sound.play()
                pygame.time.wait(100)
                turn_page = True
        else:
            mouse_on = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                playing = False
                turn_page = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mouse_on = True
                    start_button.update(mouse_on)
                    start_button.draw(screen)
                    click_sound.play()

                    pygame.time.wait(100)
                    turn_page = True

                elif event.key == pygame.K_ESCAPE:

                    turn_page = True
                    playing = False

        start_button.update(mouse_on)

        start_button.draw(screen)

        pygame.display.flip()


def show_level():
    global velocity, obs_speed, playing

    screen.fill(BG_COLOR)

    easy = button.Button()
    normal = button.Button()
    hard = button.Button()

    easy.init_button("assets/easy_on.png", "assets/easy_off.png", (250, 400))
    normal.init_button("assets/norm_on.png", "assets/norm_off.png", (500, 400))
    hard.init_button("assets/hard_on.png", "assets/hard_off.png", (750, 400))

    easy_mouse_on = False
    norm_mouse_on = False
    hard_mouse_on = False

    turn_page = False

    while not turn_page:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                playing = False
                turn_page = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:

                    turn_page = True
                    playing = False

        mouse_pos = pygame.mouse.get_pos()
        is_click = pygame.mouse.get_pressed()

        if easy.rect.x + 200 > mouse_pos[0] > easy.rect.x and easy.rect.y + 70 > mouse_pos[1] > easy.rect.y:
            easy_mouse_on = True

            if is_click[0]:
                click_sound.play()
                velocity = 9
                obs_speed = 25

                turn_page = True
        else:
            easy_mouse_on = False

        if normal.rect.x + 200 > mouse_pos[0] > normal.rect.x and normal.rect.y + 70 > mouse_pos[1] > normal.rect.y:
            norm_mouse_on = True

            if is_click[0]:
                click_sound.play()
                velocity = 8
                obs_speed = 27

                turn_page = True
        else:
            norm_mouse_on = False

        if hard.rect.x + 200 > mouse_pos[0] > hard.rect.x and hard.rect.y + 70 > mouse_pos[1] > hard.rect.y:
            hard_mouse_on = True

            if is_click[0]:
                click_sound.play()
                velocity = 7
                obs_speed = 30

                turn_page = True
        else:
            hard_mouse_on = False

        easy.update(easy_mouse_on)
        normal.update(norm_mouse_on)
        hard.update(hard_mouse_on)

        easy.draw(screen)
        normal.draw(screen)
        hard.draw(screen)

        pygame.display.flip()


def show_score(score):
    global playing

    scores = c.execute("SELECT SCORE FROM score;")
    max_score = 0

    for i in scores:
        if i[0] > max_score:
            max_score = i[0]

    score_text = def_font.render("score: %d" % score, True, (0, 240, 0))
    score_rect = score_text.get_rect()
    score_rect.center = (WIDTH / 2, HEIGHT / 2 + 80)

    max_score_text = def_font.render(
        "max score: %d" % max_score, True, (0, 0, 240))
    max_score_rect = max_score_text.get_rect()
    max_score_rect.center = (WIDTH / 2, HEIGHT / 2 + 140)

    gameover_text = title_font.render("Game Over", True, (240, 0, 0))
    gameover_rect = gameover_text.get_rect()
    gameover_rect.center = (WIDTH / 2, HEIGHT / 2 - 100)

    screen.fill(BG_COLOR)

    screen.blit(gameover_text, gameover_rect)
    screen.blit(score_text, score_rect)
    screen.blit(max_score_text, max_score_rect)

    start_button = button.Button()
    start_button.init_button("assets/start_button_on.png",
                             "assets/start_button_off.png", (850, HEIGHT - 120))  # replay

    turn_page = False
    mouse_on = False

    playing = True

    while not turn_page:

        mouse_pos = pygame.mouse.get_pos()
        is_click = pygame.mouse.get_pressed()

        if start_button.rect.x + 200 > mouse_pos[0] > start_button.rect.x and start_button.rect.y + 70 > mouse_pos[1] > start_button.rect.y:
            mouse_on = True

            if is_click[0]:
                click_sound.play()
                pygame.time.wait(100)
                turn_page = True
        else:
            mouse_on = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                playing = False
                turn_page = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mouse_on = True
                    start_button.update(mouse_on)
                    start_button.draw(screen)
                    click_sound.play()

                    pygame.time.wait(100)
                    turn_page = True

                elif event.key == pygame.K_ESCAPE:

                    turn_page = True
                    playing = False

        start_button.update(mouse_on)

        start_button.draw(screen)

        pygame.display.flip()


def main():
    global screen, WIDTH, HEIGHT, playing, velocity

    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Warrior4")
    pygame.display.set_icon(pygame.image.load("assets/icon.png"))

    playing = True
    replay = True

    show_title()
    if not playing:
        return
    show_level()
    if not playing:
        return

    BG1 = Background()
    BG2 = Background()
    BG2.rect = (WIDTH, 0)

    score = 0
    clock = pygame.time.Clock()

    player = pl.Player()
    player.init(velocity)

    score_text = Text()
    score_text.text_color((0, 0, 255))

    hp_bar = health_bar.HPBar()

    object1 = object.Object()
    object1.init(0, 500)
    object1.set_speed(obs_speed)

    object2 = object.Object()
    object2.init(1500, 2000)
    object2.set_speed(obs_speed)

    spark = coil.Coil()

    pygame.mixer.music.load("assets/bg.mp3")
    pygame.mixer.music.play(-1)

    while playing:
        keys = pygame.key.get_pressed()

        is_click = pygame.mouse.get_pressed()

        if keys[pygame.K_UP] or is_click:
            if player.JUMP == 2:
                player.jump(3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                playing = False
                replay = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if player.JUMP == 0:
                        player.jump(1)
                    elif player.JUMP == 1:
                        player.jump(2)
                if event.key == pygame.K_m:
                    if pygame.mixer.music.get_volume() == 0:
                        pygame.mixer.music.set_volume(1)
                        hit_sound.set_volume(1)
                    else:
                        pygame.mixer.music.set_volume(0)
                        hit_sound.set_volume(0)

                if event.key == pygame.K_SPACE:
                    spark.fire_coil()

                if event.key == pygame.K_ESCAPE:
                    playing = False
                    replay = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if player.JUMP == 0:
                        player.jump(1)
                    elif player.JUMP == 1:
                        player.jump(2)
                if event.button == 3:
                    spark.fire_coil()

        is_collide1 = pygame.Rect.colliderect(player.rect, object1.rect)
        is_collide2 = pygame.Rect.colliderect(player.rect, object2.rect)

        if is_collide1:
            hit_sound.play()
            player.collide(object1.type)
            object1.collide()

        if is_collide2:
            hit_sound.play()
            player.collide(object2.type)
            object2.collide()

        if not is_collide1 and not is_collide2:
            player.colliding = False

        if player.hp <= 1000:
            hp_bar.color = (240, 0, 0)

            if player.hp <= 0:
                playing = False

        player.hp -= 1

        player.update()
        object1.update(clock.get_time())
        object2.update(clock.get_time())

        spark.update(player.rect.centery)

        score += 10

        BG1.fill_bg()
        BG2.fill_bg()

        player.draw_player(screen)
        object1.draw_object(screen)
        object2.draw_object(screen)
        spark.draw_coil(screen)

        hp_bar.update(screen, player.hp)
        score_text.draw_text("score: %d" % score, (670, 30))

        clock.tick(60)
        pygame.display.flip()

    pygame.mixer.music.stop()

    c.execute("INSERT INTO score VALUES (%d);" % (score))
    conn.commit()

    if replay:
        show_score(score)

        if playing:
            main()

    conn.close()
    pygame.quit()


if __name__ == '__main__':
    main()
