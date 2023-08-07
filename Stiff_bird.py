from __future__ import print_function, absolute_import
import pygame as pg
import random


def run_all():
    def collision(rect_x, rect_y, rect_width, rect_height, play_x, play_y, play_width, play_height):
        if rect_y <= play_y + play_height and rect_y + rect_height > play_y:
            if rect_x <= play_x + play_width and rect_x + rect_width > play_x:
                return True
            pass
        return False

    birb = pg.image.load("C:/Games/My_Games/birb.png")
    back = pg.image.load("C:/Games/My_Games/BACK.png")
    pg.init()
    win = pg.display.set_mode((1920, 1080), vsync=True)
    pillar_count = 0
    pillar_velocity = 1
    x_cor_0 = -100
    x_cor_1 = -100
    x_cor_2 = -100
    end = False
    pillar_count_2 = 0
    pillar_count_3 = 0
    player_y = 700
    player_x = 500
    player_height = 50
    player_width = 50
    velocity = 0
    acceleration = 0.07
    count_0 = False
    count_1 = False
    count_2 = False
    draw0 = False
    draw1 = False
    loss = False
    pillar_length_0 = 0
    pillar_length_1 = 0
    pillar_length_2 = 0
    txt = pg.font.SysFont("freesans", 150)
    txt1 = pg.font.SysFont("freesans", 100)
    while not end:
        # pg.time.delay(1)
        key = pg.key.get_pressed()

        if not loss:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    end = True
            if key[pg.K_SPACE]:
                velocity = -3
            x_cor_0 = x_cor_0 - pillar_velocity
            velocity = velocity + acceleration
            player_y = player_y + velocity
            pillar_count += 1
            win.blit(back, (0, 0))
            # win.fill((0, 0, 0))

            pillar_count_2 += 1
            pillar_count_3 += 1

            if x_cor_0 == -150:
                pillar_length_0 = random.randrange(200, 880, 100)
                count_0 = True
                x_cor_0 = 1920
            if not count_0:
                pass
            else:
                pg.draw.rect(win, (20, 184, 20), (x_cor_0, 0, 150, pillar_length_0))
                pg.draw.rect(win, (20, 184, 20), (x_cor_0, pillar_length_0 + 200, 150, 1080))

            if pillar_count_2 == 650:
                draw0 = True

            if not draw0:
                pass
            else:
                x_cor_1 = x_cor_1 - pillar_velocity
                if x_cor_1 == -150:
                    pillar_length_1 = random.randrange(200, 880, 100)
                    count_1 = True
                    x_cor_1 = 1920
                if count_1:
                    pg.draw.rect(win, (20, 184, 20), (x_cor_1, 0, 150, pillar_length_1))
                    pg.draw.rect(win, (20, 184, 20), (x_cor_1, pillar_length_1 + 200, 150, 1080))

            if pillar_count_3 == 1290:
                draw1 = True

            if draw1:
                x_cor_2 = x_cor_2 - pillar_velocity
                if x_cor_2 == -150:
                    pillar_length_2 = random.randrange(200, 880, 100)
                    count_2 = True
                    x_cor_2 = 1920
                if count_2:
                    pg.draw.rect(win, (20, 184, 20), (x_cor_2, 0, 150, pillar_length_2))
                    pg.draw.rect(win, (20, 184, 20), (x_cor_2, pillar_length_2 + 200, 150, 1080))
            win.blit(birb, (player_x, player_y))
            if collision(x_cor_0, 0, 150, pillar_length_0, player_x, player_y, player_width, player_height):
                loss = True
            if collision(x_cor_0, pillar_length_0 + 200, 150, 1080, player_x, player_y, player_width, player_height):
                loss = True
            if collision(x_cor_1, 0, 150, pillar_length_1, player_x, player_y, player_width, player_height):
                loss = True
            if collision(x_cor_1, pillar_length_1 + 200, 150, 1080, player_x, player_y, player_width, player_height):
                loss = True
            if collision(x_cor_2, 0, 150, pillar_length_2, player_x, player_y, player_width, player_height):
                loss = True
            if collision(x_cor_2, pillar_length_2 + 200, 150, 1080, player_x, player_y, player_width, player_height):
                loss = True
            if player_y + player_height >= 1080:
                loss = True
            if player_y < 0:
                loss = True
            pg.draw.rect(win, (255, 255, 255), (0, 0, 10, 1080))
            pg.draw.rect(win, (255, 255, 255), (1910, 0, 10, 1080))
            pg.draw.rect(win, (255, 255, 255), (0, 0, 1920, 10))
            pg.draw.rect(win, (255, 255, 255), (0, 1070, 1920, 10))

        else:
            pg.mouse.set_visible(True)
            mouse = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    end = True
                if event.type == pg.MOUSEBUTTONDOWN:
                    if 384 <= mouse[0] <= 684 and 720 <= mouse[1] <= 820:
                        end = True
                    if 1152 <= mouse[0] <= 1752 and 720 <= mouse[1] <= 820:
                        pillar_length_0 = 0
                        pillar_length_1 = 0
                        pillar_length_2 = 0
                        pillar_count_2 = 0
                        pillar_count_3 = 0
                        player_y = 700
                        player_x = 500
                        player_height = 50
                        player_width = 50
                        velocity = 0
                        acceleration = 0.07
                        pillar_count = 0
                        pillar_velocity = 1
                        x_cor_0 = -100
                        x_cor_1 = -100
                        x_cor_2 = -100
                        count_0 = False
                        count_1 = False
                        count_2 = False
                        draw0 = False
                        draw1 = False
                        loss = False

            win.blit(back, (0, 0))

            label = txt.render("GAME OVER!!!", True, (255, 255, 255))
            win.blit(label, (100, 100))

            pg.draw.rect(win, (255, 255, 102), (384, 720, 300, 100))
            label = txt1.render("QUIT", True, (0, 0, 0))
            win.blit(label, (434, 710))

            pg.draw.rect(win, (51, 255, 255), (1152, 720, 600, 100))
            label = txt1.render("PLAY AGAIN", True, (0, 0, 0))
            win.blit(label, (1212, 710))

            pg.draw.rect(win, (255, 255, 255), (0, 0, 10, 1080))
            pg.draw.rect(win, (255, 255, 255), (1910, 0, 10, 1080))
            pg.draw.rect(win, (255, 255, 255), (0, 0, 1920, 10))
            pg.draw.rect(win, (255, 255, 255), (0, 1070, 1920, 10))

        pg.display.update()

    pg.quit()
