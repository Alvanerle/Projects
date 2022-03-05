import pygame, random, sys, time, math
 
# initializing
pygame.init()
pygame.mixer.init()

# resolution
WIDTH = 400
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# clock
clock = pygame.time.Clock()
FPS = 60

# colors
GREY = (144, 144, 144)
WHITE = (255, 255, 255)
GREEN = (0, 255, 77)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# variables
SPEED = 0 # speed is in random range [L, R] 
# каждую милю L и R увеличваются на 1
L = 5
R = 10
new_car = True
MILES = 0
COINS = 0
player_speed = 7

# fonts
font = pygame.font.SysFont('consolas', 20, bold = True, italic = True)
font2 = pygame.font.SysFont('aharoni', 64, bold = True, italic = False)

pygame.mixer.music.load('Mario.mp3')
pygame.mixer.music.play()

class lines():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def go_down(self):
        self.y += 5
        if self.y > HEIGHT:
            self.y = -160
    def draw(self):
        pygame.draw.rect(screen, WHITE, pygame.Rect(self.x, self.y, self.width, self.height))

class coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('coin.png')
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(x = random.randint(0, WIDTH - 50), y = random.randint(-500, -50))
    def move(self):
        self.rect.move_ip(0, player_speed - 1)
        if self.rect.y > HEIGHT:
            coins.remove(self)
            all_sprites.remove(self)
        if len(coins) < 1:
            coins.append(coin())
            all_sprites.append(coins[-1])

    
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Enemy.png')
        self.surf = pygame.Surface((57, 110))
        self.rect = self.surf.get_rect(x = random.randint(0, WIDTH - 57), y = -110)
    def move(self):
        global SPEED, MILES, new_car, L, R
        if new_car:
            new_car = False
            SPEED = random.randint(L, R)
        self.rect.move_ip(0, SPEED)
        if self.rect.y > HEIGHT:
            MILES += 1
            L += 1
            R += 1
            new_car = True
            self.rect = self.surf.get_rect(x = random.randint(0, WIDTH - 57), y = -110)
    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Player.png')
        self.surf = pygame.Surface((58, 110))
        self.rect = self.surf.get_rect(x = (WIDTH - 58) // 2, y = HEIGHT - 110)
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if self.rect.left - player_speed > 0:
                self.rect.move_ip(-player_speed, 0)
        if key[pygame.K_RIGHT]:
            if self.rect.left + 58 + player_speed < WIDTH:
                self.rect.move_ip(player_speed, 0)

# sprites         
P = Player()
E = Enemy()
coins = []
all_sprites = []
all_sprites.append(E)
all_sprites.append(P)

coins.append(coin())
all_sprites.append(coins[-1])

# road lines
line1 = lines(192, 0, 16, 140)
line2 = lines(192, 160, 16, 140)
line3 = lines(192, 320, 16, 140)
line4 = lines(192, 480, 16, 140)
line5 = lines(192, 640, 16, 140)

lines_ = [line1, line2, line3, line4, line5]

miles_traveled = 0
def draw_text_and_lines():
    global miles_traveled
    screen.fill(GREY)
    if E.rect.y > 0:
        miles_traveled = MILES + E.rect.y / HEIGHT
    else:
        miles_traveled = MILES
    miles = font.render('Miles: {:.2f}'.format(miles_traveled), True, BLACK)   
    collected_coins = font.render(f'Coins: {COINS}', True, BLACK)
    screen.blit(collected_coins, (WIDTH - 110, 8)) 
    screen.blit(miles, (8, 8))
    for line in lines_:
        line.go_down()
        line.draw()

def draw_all_sprites():
    global COINS
    for coin_ in coins:
        if coin_.rect.colliderect(P):
            pygame.mixer.Sound('coin.mp3').play()
            COINS += 1
            coins.remove(coin_)
            all_sprites.remove(coin_)
    if len(coins) == 0:
        coins.append(coin())
        all_sprites.append(coins[-1])
    for sprite in all_sprites:
        sprite.move()
        screen.blit(sprite.image, sprite.rect)

def is_this_game_over():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if E.rect.colliderect(P):
        pygame.mixer.music.stop()
        pygame.mixer.Sound('wasted.mp3').play()

        total_score = font2.render(f'Your score: {math.ceil(MILES + E.rect.y / HEIGHT + COINS)}', True, GREEN)

        screen.fill(BLACK)
        screen.blit(total_score, (25, HEIGHT // 2 - 40))

        pygame.display.flip()
        time.sleep(5.5)

        pygame.quit()
        sys.exit()         

def run_game():
    while True:
        draw_text_and_lines()
        draw_all_sprites()
        is_this_game_over()

        pygame.display.flip()
        clock.tick(FPS)

run_game()