import pygame
import math

pygame.init()
WIDTH = 900
HEIGHT = 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill((255, 255, 255))
clock = pygame.time.Clock()

# 3pi - (-3pi) = 6pi = 18.84
# 18.84 / 900 = 0.0209439

# 1 / (pi / 2) = 0.63662 -> HEIGHT = 0.63662 * WIDTH / 6

pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, HEIGHT), 2)
pygame.draw.line(screen, (0, 0, 0), (0, 0), (WIDTH, 0), 2)
pygame.draw.line(screen, (0, 0, 0), (WIDTH, 0), (WIDTH, HEIGHT), 2)
pygame.draw.line(screen, (0, 0, 0), (0, HEIGHT), (WIDTH, HEIGHT), 2)

pygame.draw.line(screen, (0, 0, 0), (0, HEIGHT / 2), (WIDTH, HEIGHT / 2), 2)

d = WIDTH / 6
for i in range(1, 7):
    pygame.draw.line(screen, (0, 0, 0), (d * i, 0), (d * i, HEIGHT), 2)

d_ = HEIGHT / 8
for i in range(1, 9):
    pygame.draw.line(screen, (0, 0, 0), (0, d_ * i), (WIDTH, d_ * i), 2)

x1 = 0
y1 = HEIGHT / 2

x = 0
y = 0

x2 = 0
y2 = HEIGHT

x_ = 0
y_ = 0

add = 6 * math.pi / WIDTH
tmp = add
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # график синуса
    x = x1 + 1
    y = int(HEIGHT / 2 - HEIGHT / 2 * math.sin(-3 * math.pi + tmp))
    pygame.draw.line(screen, (255, 0, 0), (x1, y1), (x, y), 2)
    x1 = x
    y1 = y

    # график косинуса
    x_ = x2 + 1
    y_ = int(HEIGHT / 2 - HEIGHT / 2 * math.cos(-3 * math.pi + tmp))
    pygame.draw.line(screen, (0, 0, 255), (x2, y2), (x_, y_), 2)
    x2 = x_
    y2 = y_

    tmp += add
    
    pygame.display.flip()
    clock.tick(150)

# z = HEIGHT / 2
# (z - y) / z = x
# xz = z - y
# y = z - zx