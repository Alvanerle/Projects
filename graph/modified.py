import pygame
import math

pygame.init()
WIDTH = 900
HEIGHT = 300
screen = pygame.display.set_mode((1000, 500))
surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

screen.fill((255, 255, 255))
clock = pygame.time.Clock()

# text
font = pygame.font.SysFont('timesnewroman', 14, italic = True, bold = True)
font2 = pygame.font.SysFont('timesnewroman', 24, bold = True)
text1 = ['1.00', '0.75', '0.50', '0.25', '0.00', '-0.25', '-0.50', '-0.75', '-1.00']
text2 = ['-3π', '-2.5π', '-2π', '-1.5π', '-π', '-0.5π', '0', '0.5π', 'π', '1.5π', '2π', '2.5π', '3π']
axis = font2.render('X', True, (0, 0, 0))

for i in range(len(text2)):
    text2[i] = font.render(text2[i], True, (0, 0, 0))
for i in range(len(text1)):
    text1[i] = font.render(text1[i], True, (0, 0, 0))

pos_x = 5
pos_y = 94
for i in range(len(text1)):
    if i >= 0 and i <= 4:
        screen.blit(text1[i], (8, pos_y))
    else:
        screen.blit(text1[i], (4, pos_y))
    pos_y += HEIGHT / 8
pos_x = 41
pos_y = 418
for i in range(len(text2)):
    if i == 6:
        screen.blit(text2[i], (498, pos_y))
        screen.blit(axis, (493, pos_y + 20))
    elif i == 8:
        screen.blit(text2[i], (498 + WIDTH / 6, pos_y))
    else:
        screen.blit(text2[i], (pos_x, pos_y))
    pos_x += WIDTH / 12
# рисунок син, кос
image = pygame.image.load('1.png')
screen.blit(image, (666, 120))

# 4 линии вокруг графика
pygame.draw.line(surface, (0, 0, 0), (0, 0), (0, HEIGHT), 1)
pygame.draw.line(screen, (0, 0, 0), (35, 100), (WIDTH + 65, 100), 1)
# pygame.draw.line(surface, (0, 0, 0), (WIDTH - 2, 0), (WIDTH - 2, HEIGHT), 1)
pygame.draw.line(screen, (0, 0, 0), (35, HEIGHT + 100), (WIDTH + 65, HEIGHT + 100), 1)

# горизонтальная линия по середине
pygame.draw.line(screen, (0, 0, 0), (35, HEIGHT / 2 + 100), (WIDTH + 65, HEIGHT / 2 + 100), 2)

# вертикальные линии
d = WIDTH / 6
for i in range(1, 7):
    thick = 1
    if i == 3:
        thick = 2
    pygame.draw.line(screen, (0, 0, 0), (d * i + 50, 85), (d * i + 50, 415), thick)
pygame.draw.line(screen, (0, 0, 0), (50, 85), (50, 415), 1)

# горизонтальные линни
d_ = HEIGHT / 8
for i in range(1, 8):
    if i == 1:
        # место для картинка син, кос
        pygame.draw.line(screen, (0, 0, 0), (35, d_ * i + 100), (WIDTH / 2 + WIDTH / 6 + 50, d_ * i + 100), 1)
        pygame.draw.line(screen, (0, 0, 0), (WIDTH / 2 + 2 * WIDTH / 6 + 50, d_ * i + 100), (WIDTH + 65, d_ * i + 100), 1)
    else:    
        pygame.draw.line(screen, (0, 0, 0), (35, d_ * i + 100), (WIDTH + 65, d_ * i + 100), 1)

# боковые шкалы 
# 1 / 4 шкала
y__ = HEIGHT / 32 + 100
for i in range(16):
    pygame.draw.line(screen, (0, 0, 0), (35, y__), (40, y__), 1)
    y__ += HEIGHT / 16
y__ = HEIGHT / 32 + 100
for i in range(16):
    pygame.draw.line(screen, (0, 0, 0), (960, y__), (965, y__), 1)
    y__ += HEIGHT / 16
# 1 / 2 шкала
y__ = HEIGHT / 16 + 100
for i in range(8):
    pygame.draw.line(screen, (0, 0, 0), (35, y__), (45, y__), 1)
    y__ += HEIGHT / 8
y__ = HEIGHT / 16 + 100
for i in range(8):
    pygame.draw.line(screen, (0, 0, 0), (955, y__), (965, y__), 1)
    y__ += HEIGHT / 8

# сверху и снизу
# 1 / 2 шкала
x__ = WIDTH / 12 + 50
for i in range(6):
    pygame.draw.line(screen, (0, 0, 0), (x__, 85), (x__, 95), 1)
    x__ += WIDTH / 6
x__ = WIDTH / 12 + 50
for i in range(6):
    pygame.draw.line(screen, (0, 0, 0), (x__, 405), (x__, 415), 1)
    x__ += WIDTH / 6
# 1 / 4 шкала
x__ = WIDTH / 24 + 50
for i in range(12):
    pygame.draw.line(screen, (0, 0, 0), (x__, 85), (x__, 92), 1)
    x__ += WIDTH / 12
x__ = WIDTH / 24 + 50
for i in range(12):
    pygame.draw.line(screen, (0, 0, 0), (x__, 408), (x__, 415), 1)
    x__ += WIDTH / 12
# 1 / 8 шкала
x__ = WIDTH / 48 + 50
for i in range(24):
    pygame.draw.line(screen, (0, 0, 0), (x__, 85), (x__, 90), 1)
    x__ += WIDTH / 24
x__ = WIDTH / 48 + 50
for i in range(24):
    pygame.draw.line(screen, (0, 0, 0), (x__, 410), (x__, 415), 1)
    x__ += WIDTH / 24

# линни вокруг surface
pygame.draw.line(screen, (0, 0, 0), (35, 85), (965, 85), 2)
pygame.draw.line(screen, (0, 0, 0), (35, 415), (965, 415), 2)

pygame.draw.line(screen, (0, 0, 0), (35, 85), (35, 415), 2)
pygame.draw.line(screen, (0, 0, 0), (965, 85), (965, 415), 2)

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


    screen.blit(surface, (50, 100))
    # график синуса
    x = x1 + 1
    y = math.ceil(HEIGHT / 2 - HEIGHT / 2 * math.sin(-3 * math.pi + tmp))
    pygame.draw.line(surface, (255, 0, 0), (x1, y1), (x, y), 2)
    x1 = x
    y1 = y

    # график косинуса
    x_ = x2 + 1
    y_ = int(HEIGHT / 2 - HEIGHT / 2 * math.cos(-3 * math.pi + tmp))
    if x2 % 4 == 0:
        pygame.draw.line(surface, (0, 0, 255), (x2, y2), (x_, y_), 2)
    x2 = x_
    y2 = y_

    tmp += add
    
    pygame.display.flip()
    clock.tick(150)

# 3pi - (-3pi) = 6pi = 18.84
# 18.84 / 900 = 0.0209439

# 1 / (pi / 2) = 0.63662 -> HEIGHT = 0.63662 * WIDTH

# z = HEIGHT / 2
# (z - y) / z = x
# xz = z - y
# y = z - zx
