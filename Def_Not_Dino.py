from __future__ import print_function, absolute_import
import pygame as pg
import random


class Bot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def run_all():
    def collision(rect_x, rect_y, rect_width, rect_height, play_x, play_y, play_width, play_height):
        if rect_y <= play_y + play_height and rect_y + rect_height > play_y:
            if rect_x <= play_x + play_width and rect_x + rect_width > play_x:
                return True
            pass
        return False

    pg.init()
    win = pg.display.set_mode((1920, 1080))
    back = pg.image.load("C:/Games/My_Games/Background.png")
    char = pg.image.load("C:/Games/My_Games/Char.png")
    obs1 = pg.image.load("C:/Games/My_Games/obs1.png")
    obs2 = pg.image.load("C:/Games/My_Games/obs2.png")

    velocity = 0
    acceleration = 0.3
    draw = 0
    draw1 = 0
    rand = 0

    obstacle_velocity = 5
    obstacle_x1 = 1920
    obstacle_width1 = 200
    obstacle_width2 = 150
    obstacle_x2 = 1920
    move = False
    end = False
    loss = False
    pause = False

    bot = Bot(200, 735)

    while not end:
        pg.time.delay(1)
        keys = pg.key.get_pressed()

        if not loss and not pause:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    end = True

            if keys[pg.K_ESCAPE]:
                pause = True

            if obstacle_velocity < 10:
                obstacle_velocity += 0.0001

            if collision(obstacle_x1, 785, obstacle_width1, 100, bot.x, bot.y, 90, 150):
                end = True

            if bot.y > 735:
                bot.y = 735
            if bot.y == 735:
                velocity = 0

                if keys[pg.K_SPACE]:
                    velocity = -14

            bot.y = bot.y + velocity
            velocity = velocity + acceleration

            win.blit(back, (0, 0))
            win.blit(char, (bot.x, bot.y))
            # pg.draw.rect(win, (0, 0, 0), (200, bot.y, 90, 150))

            if obstacle_x1 < (-obstacle_width1):
                obstacle_x1 = 1920

            if obstacle_x2 < (-obstacle_width2):
                rand = random.randrange(-200, 200)
                obstacle_x2 = 1920

            draw += 1
            draw1 += 1
            if draw > 500:
                obstacle_x1 = obstacle_x1 - obstacle_velocity

                win.blit(obs1, (obstacle_x1, 785))

            if draw1 > 700 + rand:
                obstacle_x2 = obstacle_x2 - obstacle_velocity

                win.blit(obs2, (obstacle_x2, 735))

        elif not loss and pause:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    end = True

            if keys[pg.K_SPACE]:
                pause = False

            win.fill((100, 100, 100))
            pg.draw.rect(win, (255, 255, 255), (0, 0, 10, 1080))
            pg.draw.rect(win, (255, 255, 255), (1910, 0, 10, 1080))
            pg.draw.rect(win, (255, 255, 255), (0, 0, 1920, 10))
            pg.draw.rect(win, (255, 255, 255), (0, 1070, 1920, 10))

        pg.display.update()

    pg.quit()