import pygame
from pygame.locals import *
import sys

# 初始化pygame

pygame.init()

size = (800, 600)

# 设置屏幕宽高
screen = pygame.display.set_mode(size)
# 设置屏幕标题
pygame.display.set_caption("my first game")

black = 0, 0, 0
clock = pygame.time.Clock()

listLeft = [pygame.image.load('./feiji/enemy0.png'.format(i)).convert_alpha() for i in range(1, 10)]
listRight = [pygame.image.load('./feiji/enemy0_down1.png'.format(i)).convert_alpha() for i in range(1, 10)]
imgHero = pygame.image.load('./feiji/enemy0_down2.png').convert_alpha()

xPos = 100
speed = 2
# 左direction = 1，右direction = 2，前direction = 0
direction = 0
indexLeft = 0
indexRight = 0
while True:
    clock.tick(10)
    # 启动消息队列，获取消息并处理
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[K_LEFT]:
        direction = 1
        xPos -= speed
        print('left')
    elif keys[K_RIGHT]:
        direction = 2
        xPos += speed
        print('right')
    else:
        direction = 0

    screen.fill((0, 0, 0))
    if direction == 0:
        screen.blit(imgHero, (xPos, 100))
    elif direction == 1:
        screen.blit(listLeft[indexLeft % 9], (xPos, 100))
        indexLeft += 1
    elif direction == 2:
        screen.blit(listRight[indexRight % 9], (xPos, 100))
        indexRight += 1

    pygame.display.update()
