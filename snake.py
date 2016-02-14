#!/usr/bin/python
import random
import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
done = False
black = (0, 0, 0)
snakeList = [(100, 100), (150, 100), (200, 100), (250, 100), (300, 100)]
direction = "right"
appleHere = False
pause = False

while not done:
    time.sleep(0.15)
    screen.fill(black)

    # calculate new Head
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                    direction = "up"
            elif event.key == pygame.K_DOWN and direction != "up":
                    direction = "down"
            elif event.key == pygame.K_LEFT and direction != "right":
                    direction = "left"
            elif event.key == pygame.K_RIGHT and direction != "left":
                    direction = "right"
            elif event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_SPACE:
                pause = True

    if pause:
        while pause:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = False

    head = snakeList[-1]
    if direction == "right":
        newHead = (head[0] + 50, head[1])
    elif direction == "up":
        newHead = (head[0], head[1] - 50)
    elif direction == "down":
        newHead = (head[0], head[1] + 50)
    elif direction == "left":
        newHead = (head[0] - 50, head[1])

    # check for bounds
    if head[0] < 0 or head[0] > 1000:
        done = True
    if head[1] < 0 or head[1] > 1000:
        done = True
    if newHead in snakeList:
        done = True

    # create Apple
    if not appleHere:
        ran = random.randint(50, 950)
        ran = ran - (ran % 50)
        ran1 = random.randint(50, 950)
        ran1 = ran1 - (ran1 % 50)

        apple = (ran, ran1)
        appleHere = True

    # append Snake
    snakeList.append(newHead)
    if newHead != apple:
        snakeList.remove(snakeList[0])
    else:
        appleHere = False

    # draw Stuff
    pygame.draw.rect(screen, (0, 255, 0), (apple[0], apple[1], 50, 50))
    for e in snakeList:
        pygame.draw.rect(screen, (255, 0, 0), (e[0], e[1], 50, 50))
    pygame.display.flip()


# Game Over
screen.fill(black)
myfont = pygame.font.SysFont("monospace", 50)
label = myfont.render("Game Over !!!", 1, (255, 255, 0))
screen.blit(label, (300, 300))
pygame.display.flip()
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            pygame.quit()
