import pygame
import random


def collision(x1, y1, width1, height1, x2, y2, width2, height2):
    if y1 <= y2 + height2 and y1 + height1 > y2:
        if x1 <= x2 + width2 and x1 + width1 > x2:
            return True
    return False


class player(object):
    def __init__(self, x, y, width, height, v):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.v = v


def run_all():
    pygame.init()
    win = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("First game")

    obj = player(random.randrange(100, 1720, 100), random.randrange(100, 880, 100), random.randrange(30, 200, 10),
                 random.randrange(30, 200, 10), 0)
    obj1 = player(random.randrange(100, 1720, 100), random.randrange(100, 880, 100), random.randrange(30, 200, 10),
                  random.randrange(30, 200, 10), 0)
    obj2 = player(random.randrange(100, 1720, 100), random.randrange(100, 880, 100), random.randrange(30, 200, 10),
                  random.randrange(30, 200, 10), 0)
    obj3 = player(random.randrange(100, 1720, 100), random.randrange(100, 880, 100), random.randrange(30, 200, 10),
                  random.randrange(30, 200, 10), 0)
    obj4 = player(random.randrange(100, 1720, 100), random.randrange(100, 880, 100), random.randrange(30, 200, 10),
                  random.randrange(30, 200, 10), 0)
    obj5 = player(random.randrange(100, 1720, 100), random.randrange(100, 880, 100), random.randrange(30, 200, 10),
                  random.randrange(30, 200, 10), 0)
    obj6 = player(random.randrange(100, 1720, 100), random.randrange(100, 880, 100), random.randrange(30, 200, 10),
                  random.randrange(30, 200, 10), 0)
    obj7 = player(random.randrange(100, 1720, 100), random.randrange(100, 880, 100), random.randrange(30, 200, 10),
                  random.randrange(30, 200, 10), 0)
    obj8 = player(random.randrange(100, 1720, 100), random.randrange(100, 880, 100), random.randrange(30, 200, 10),
                  random.randrange(30, 200, 10), 0)
    rn1 = player(1820, 980, 60, 60, 0)
    font = pygame.font.SysFont("freesans", 30)
    score = 0

    snake = player(0, 0, 50, 50, 3)
    accelerator = 500
    speed_counter = 0
    run = True
    counter = accelerator
    while run:
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        temp_snake_x = snake.x
        temp_snake_y = snake.y

        if counter == accelerator:
            for i in range(5):
                rn_x = random.randrange(100, 1820, 100)
                rn_y = random.randrange(100, 980, 100)
                if not collision(rn_x, rn_y, 60, 60, obj.x, obj.y, obj.width, obj.height):
                    if not collision(rn_x, rn_y, 60, 60, obj1.x, obj1.y, obj1.width, obj1.height):
                        if not collision(rn_x, rn_y, 60, 60, obj2.x, obj2.y, obj2.width, obj2.height):
                            if not collision(rn_x, rn_y, 60, 60, obj3.x, obj3.y, obj3.width, obj3.height):
                                if not collision(rn_x, rn_y, 60, 60, obj4.x, obj4.y, obj4.width, obj4.height):
                                    if not collision(rn_x, rn_y, 60, 60, obj5.x, obj5.y, obj5.width, obj5.height):
                                        if not collision(rn_x, rn_y, 60, 60, obj6.x, obj6.y, obj6.width, obj6.height):
                                            if not collision(rn_x, rn_y, 60, 60, obj7.x, obj7.y, obj7.width,
                                                             obj7.height):
                                                if not collision(rn_x, rn_y, 60, 60, obj8.x, obj8.y, obj8.width,
                                                                 obj8.height):
                                                    break
            counter = 0
        counter += 1

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and snake.x > snake.v:
            snake.x -= snake.v
        if keys[pygame.K_RIGHT] and snake.x < 1920 - snake.height - snake.v:
            snake.x += snake.v
        if keys[pygame.K_UP] and snake.y > snake.v:
            snake.y -= snake.v
        if keys[pygame.K_DOWN] and snake.y < 1080 - snake.width - snake.v:
            snake.y += snake.v

        if obj.y <= snake.y + snake.height and obj.y + obj.height > snake.y:
            if obj.x <= snake.x + snake.width and obj.x + obj.width > snake.x:
                run = False
        if obj1.y <= snake.y + snake.height and obj1.y + obj1.height > snake.y:
            if obj1.x <= snake.x + snake.width and obj1.x + obj2.width > snake.x:
                run = False
        if obj2.y <= snake.y + snake.height and obj2.y + obj2.height > snake.y:
            if obj2.x <= snake.x + snake.width and obj2.x + obj2.width > snake.x:
                run = False
        if obj3.y <= snake.y + snake.height and obj3.y + obj3.height > snake.y:
            if obj3.x <= snake.x + snake.width and obj3.x + obj3.width > snake.x:
                run = False
        if obj4.y <= snake.y + snake.height and obj4.y + obj4.height > snake.y:
            if obj4.x <= snake.x + snake.width and obj4.x + obj4.width > snake.x:
                run = False
        if obj5.y <= snake.y + snake.height and obj5.y + obj5.height > snake.y:
            if obj5.x <= snake.x + snake.width and obj5.x + obj5.width > snake.x:
                run = False
        if obj6.y <= snake.y + snake.height and obj6.y + obj6.height > snake.y:
            if obj6.x <= snake.x + snake.width and obj6.x + obj6.width > snake.x:
                run = False
        if obj7.y <= snake.y + snake.height and obj7.y + obj7.height > snake.y:
            if obj7.x <= snake.x + snake.width and obj7.x + obj7.width > snake.x:
                run = False
        if obj8.y <= snake.y + snake.height and obj8.y + obj8.height > snake.y:
            if obj8.x <= snake.x + snake.width and obj8.x + obj8.width > snake.x:
                run = False
        """
        if rn1.y <= snake.y + snake.height and rn1.y + rn1.height > snake.y:
            if rn1.x <= snake.x + snake.width and rn1.x + rn1.width > snake.x:
                run = False
        """

        if collision(rn_x, rn_y, 25, 25, rn1.x, rn1.y, rn1.width, rn1.height):
            score -= 1
            if accelerator >= 200:
                accelerator -= 5
            if speed_counter == 5:
                snake.v += 0.1
                speed_counter = 0
            if speed_counter != 5:
                speed_counter += 1
            counter = accelerator

        if (rn_y < snake.y + snake.height and rn_y + 50 > snake.y) and (
                rn_x < snake.x + snake.width and rn_x + 50 > snake.x):
            score += 1
            if accelerator >= 200:
                accelerator -= 5
            if speed_counter == 5:
                snake.v += 0.1
                speed_counter = 0
            if speed_counter != 5:
                speed_counter += 1
            counter = accelerator

        if rn1.x > rn_x:
            temp_x = rn1.x
            rn1.x = rn1.x - snake.v

        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj.x, obj.y, obj.width, obj.height):
            rn1.x = temp_x
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj1.x, obj1.y, obj1.width, obj1.height):
            rn1.x = temp_x
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj2.x, obj2.y, obj2.width, obj2.height):
            rn1.x = temp_x
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj3.x, obj3.y, obj3.width, obj3.height):
            rn1.x = temp_x
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj4.x, obj4.y, obj4.width, obj4.height):
            rn1.x = temp_x
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj5.x, obj5.y, obj5.width, obj5.height):
            rn1.x = temp_x
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj6.x, obj6.y, obj6.width, obj6.height):
            rn1.x = temp_x
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj7.x, obj7.y, obj7.width, obj7.height):
            rn1.x = temp_x
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj8.x, obj8.y, obj8.width, obj8.height):
            rn1.x = temp_x

        elif rn1.x < rn_x:
            temp_x = rn1.x
            rn1.x = rn1.x + snake.v

        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj.x, obj.y, obj.width, obj.height):
            rn1.x = temp_x
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj1.x, obj1.y, obj1.width, obj1.height):
            rn1.x = temp_x
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj2.x, obj2.y, obj2.width, obj2.height):
            rn1.x = temp_x
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj3.x, obj3.y, obj3.width, obj3.height):
            rn1.x = temp_x
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj4.x, obj4.y, obj4.width, obj4.height):
            rn1.x = temp_x
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj5.x, obj5.y, obj5.width, obj5.height):
            rn1.x = temp_x
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj6.x, obj6.y, obj6.width, obj6.height):
            rn1.x = temp_x
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj7.x, obj7.y, obj7.width, obj7.height):
            rn1.x = temp_x
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj8.x, obj8.y, obj8.width, obj8.height):
            rn1.x = temp_x

        if rn1.y > rn_y:
            temp_y = rn1.y
            rn1.y = rn1.y - snake.v

        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj.x, obj.y, obj.width, obj.height):
            rn1.y = temp_y
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj1.x, obj1.y, obj1.width, obj1.height):
            rn1.y = temp_y
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj2.x, obj2.y, obj2.width, obj2.height):
            rn1.y = temp_y
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj3.x, obj3.y, obj3.width, obj3.height):
            rn1.y = temp_y
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj4.x, obj4.y, obj4.width, obj4.height):
            rn1.y = temp_y
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj5.x, obj5.y, obj5.width, obj5.height):
            rn1.y = temp_y
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj6.x, obj6.y, obj6.width, obj6.height):
            rn1.y = temp_y
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj7.x, obj7.y, obj7.width, obj7.height):
            rn1.y = temp_y
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj8.x, obj8.y, obj8.width, obj8.height):
            rn1.y = temp_y

        elif rn1.y < rn_y:
            temp_y = rn1.y
            rn1.y = rn1.y + snake.v

        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj.x, obj.y, obj.width, obj.height):
            rn1.y = temp_y
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj1.x, obj1.y, obj1.width, obj1.height):
            rn1.y = temp_y
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj2.x, obj2.y, obj2.width, obj2.height):
            rn1.y = temp_y
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj3.x, obj3.y, obj3.width, obj3.height):
            rn1.y = temp_y
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj4.x, obj4.y, obj4.width, obj4.height):
            rn1.y = temp_y
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj5.x, obj5.y, obj5.width, obj5.height):
            rn1.y = temp_y
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj6.x, obj6.y, obj6.width, obj6.height):
            rn1.y = temp_y
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj7.x, obj7.y, obj7.width, obj7.height):
            rn1.y = temp_y
        if collision(rn1.x, rn1.y, rn1.width, rn1.height, obj8.x, obj8.y, obj8.width, obj8.height):
            rn1.y = temp_y

        win.fill((0, 0, 0))
        label = font.render("SCORE: " + str(score), True, (255, 255, 255))
        win.blit(label, (20, 20))
        pygame.draw.rect(win, (1, 255, 163), (snake.x, snake.y, snake.width, snake.height))
        pygame.draw.rect(win, (255, 0, 255), (obj.x, obj.y, obj.width, obj.height))
        pygame.draw.rect(win, (255, 0, 255), (obj1.x, obj1.y, obj1.width, obj1.height))
        pygame.draw.rect(win, (255, 0, 255), (obj2.x, obj2.y, obj2.width, obj2.height))
        pygame.draw.rect(win, (255, 0, 255), (obj3.x, obj3.y, obj3.width, obj3.height))
        pygame.draw.rect(win, (255, 0, 255), (obj4.x, obj4.y, obj4.width, obj4.height))
        pygame.draw.rect(win, (255, 0, 255), (obj5.x, obj5.y, obj5.width, obj5.height))
        pygame.draw.rect(win, (255, 0, 255), (obj6.x, obj6.y, obj6.width, obj6.height))
        pygame.draw.rect(win, (255, 0, 255), (obj7.x, obj7.y, obj7.width, obj7.height))
        pygame.draw.rect(win, (255, 0, 255), (obj8.x, obj8.y, obj8.width, obj8.height))
        pygame.draw.rect(win, (255, 51, 0), (rn1.x, rn1.y, rn1.width, rn1.height))
        pygame.draw.rect(win, (200, 200, 200), (0, 0, 10, 1080))
        pygame.draw.rect(win, (200, 200, 200), (1910, 0, 10, 1080))
        pygame.draw.rect(win, (200, 200, 200), (0, 0, 1920, 10))
        pygame.draw.rect(win, (200, 200, 200), (0, 1070, 1920, 10))

        pygame.draw.rect(win, (255, 255, 255), (rn_x, rn_y, 25, 25))

        pygame.display.update()

    pygame.quit()
