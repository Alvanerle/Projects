d = WIDTH / 6
for i in range(1, 7):
    thick = 1
    if i == 3:
        thick = 2
    if i >= 2 and i <= 5:
        coordinates.append(d * i)
    pygame.draw.line(surface, (0, 0, 0), (d * i, 0), (d * i, HEIGHT), thick)