import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('line - 1, rect - 2, circle - 3, eraser - 4, clean the screen - 5, save - s. Bigger size - key up, smaller - key down')

surface = pygame.Surface((800, 480))
surface.fill((255, 255, 255))

screen.fill((255, 255, 255))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 20, 147)

class Button():
    def __init__(self, color, x, y, width, height, text='', text_color = (0, 0, 0)):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = text_color

    def draw(self, screen, outline = None):
        if outline:
            pygame.draw.rect(screen, outline, (self.x - 2,self.y - 2, self.width + 4,self.height + 4), 0)
            
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if self.text != '':
            font = pygame.font.SysFont('consolas', 30)
            text = font.render(self.text, True, self.text_color)
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False


def draw_rect(screen, color, x, y, width, height):
    pygame.draw.rect(screen, color, (x - width // 2, y - height // 2, width, height), 3)

def draw_circle(screen, color, x, y, radius):
    pygame.draw.circle(screen, color, (x, y), radius, 3)

def draw_line(screen, color, start_pos, end_pos, width):
    pygame.draw.line(screen, color, (start_pos[0], start_pos[1] - 160), (end_pos[0], end_pos[1] - 160), width)

def erase(screen, color, x, y, width, height):
    pygame.draw.rect(screen, color, (x - width // 2, y - height // 2, width, height))

def save(screen):
    pygame.image.save(screen, 'image.png')

red = Button(RED, 0, 0, 160, 160, 'Red', BLACK)
green = Button(GREEN, 160, 0, 160, 160, 'Green', BLACK)
blue = Button(BLUE, 320, 0, 160, 160, 'Blue', BLACK)
black = Button(BLACK, 480, 0, 160, 160, 'Black', WHITE)
pink = Button(PINK, 640, 0, 160, 160, 'Pink', WHITE)

def run_prog():
    size = 10
    pen_color = BLACK
    last_key = '0'
    is_pressed = False
    prev_point = (0, 0)
    cur_point = (0, 0)
    run = True
    while run:  
        screen.blit(surface, (0, 160))
        red.draw(screen)
        green.draw(screen)
        blue.draw(screen)
        black.draw(screen)
        pink.draw(screen)


        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit() 

            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if red.isOver(pos):
                    pen_color = RED
                elif green.isOver(pos):
                    pen_color = GREEN
                elif blue.isOver(pos):
                    pen_color = BLUE
                elif black.isOver(pos):
                    pen_color = BLACK
                elif pink.isOver(pos):
                    pen_color = PINK
                else:
                    is_pressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                is_pressed = False

            keys = pygame.key.get_pressed()
            if(keys[pygame.K_UP]):
                size += 1
                size = min(size, 100)
            elif(keys[pygame.K_DOWN]):
                size -= 1
                size = max(size, 10)   

            if keys[pygame.K_1]:
                last_key = '1'
            elif keys[pygame.K_2]:
                last_key = '2'
            elif keys[pygame.K_3]:
                last_key = '3'
            elif keys[pygame.K_4]:
                last_key = '4'
            elif keys[pygame.K_5]:
                surface.fill((255, 255, 255))
            elif keys[pygame.K_s]:
                save(surface)
            prev_point = cur_point
            cur_point = pos

            if last_key == '1' and is_pressed:
                draw_line(surface, pen_color, prev_point, cur_point, max(size // 10, 1))
            elif last_key == '2' and is_pressed:
                draw_rect(surface, pen_color, pos[0], pos[1] - 160, size, size)
            elif last_key == '3' and is_pressed:
                draw_circle(surface, pen_color, cur_point[0], cur_point[1] - 160, size)
            elif last_key == '4' and is_pressed:
                erase(surface, WHITE, pos[0], pos[1] - 160, size, size)

        pygame.display.update()

run_prog()