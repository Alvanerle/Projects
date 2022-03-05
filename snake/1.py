import pygame
import sys
import random
import json
import hashlib
from functools import cmp_to_key

#-------------------
#--ALL--VARIABLES---
#-------------------

all_walls = []
foods = []
level_num = 1
single_player = True

#-------------------
#-------------------
#-------------------

class Objects():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

class Snake():
    def __init__(self, x = 64, y = 64, color = (0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color
        self.speed_ = 14
        self.speed = [12, 0]
        self.radius = 12
        self.score = 0
        self.size = 1
        self.hitbox = pygame.Rect(self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)
        self.hitbox_coord = [[self.x-self.radius, self.y-self.radius]]
        self.elements = [[self.x, self.y, self.hitbox]]
        self.left = False
        self.right = True
        self.up = False
        self.down = False

    def add_tail(self):
        self.size += 1
        self.hitbox = pygame.Rect(self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)
        self.hitbox_coord.append([self.x-self.radius, self.y-self.radius])
        self.elements.append([self.x, self.y, self.hitbox])
    
    def draw(self):
        for part in self.elements:
            pygame.draw.circle(screen, self.color, part[0:2], self.radius)
            # pygame.draw.rect(screen, (255, 0, 0), part[2]) # hitbox
        
    def move(self):
        for i in range(1, self.size):
            self.elements[self.size - i][0] = self.elements[self.size - i - 1][0]
            self.elements[self.size - i][1] = self.elements[self.size - i - 1][1]
            self.elements[self.size - i][2][0] = self.elements[self.size - i - 1][2][0]
            self.elements[self.size - i][2][1] = self.elements[self.size - i - 1][2][1]
            self.hitbox_coord[self.size - i][0] = self.hitbox_coord[self.size - i - 1][0]
            self.hitbox_coord[self.size - i][1] = self.hitbox_coord[self.size - i - 1][1]
        self.elements[0][0] += self.speed[0]
        self.elements[0][1] += self.speed[1]
        self.elements[0][2][0] += self.speed[0]
        self.elements[0][2][1] += self.speed[1]
        self.hitbox_coord[0][0] += self.speed[0]
        self.hitbox_coord[0][1] += self.speed[1]

    def restart(self, hitbox_coord, score, size, left, right, up, down):
        self.hitbox_coord = hitbox_coord
        self.score = score
        self.size = size
        self.hitbox = []
        self.elements = []
        for i in range(self.size):
            self.hitbox.append(pygame.Rect(hitbox_coord[i][0], hitbox_coord[i][1], self.radius*2, self.radius*2))
            self.elements.append([hitbox_coord[i][0]+self.radius, hitbox_coord[i][1]+self.radius, self.hitbox[i]])
        self.left = left
        self.right = right
        self.up = up
        self.down = down

class Walls(Objects):
    def __init__(self, x, y, color, width = 32, height = 32):
        Objects.__init__(self, x, y, color)
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.image.load('pictures/stone.jpg')
    
    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class Food(Objects):
    def __init__(self, x, y, color):
        Objects.__init__(self, x, y, color)
        self.width = 28
        self.height = 28
        self.image = pygame.image.load('pictures/peach.png')
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class Button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen,outline=None):
        if outline:
            pygame.draw.rect(screen, outline, (self.x - 2,self.y - 2, self.width + 4,self.height + 4), 0)
            
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if self.text != '':
            font = pygame.font.SysFont('consolas', 30)
            text = font.render(self.text, 1, (0, 0, 0))
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

def create_map(level):
    global all_walls
    with open (f'maps/map_{level}.txt', mode = 'r', encoding = 'utf-8') as walls:
        row_index = 0
        column_index = 0
        for row in walls:
            for wall in row:
                if wall == '1':
                    all_walls.append(Walls(column_index*32, row_index*32, (200, 50, 40)))
                column_index += 1
            column_index = 0
            row_index += 1

def food_spawner():
    if len(foods) < 5:
        x = random.randrange(0, screen_width)
        y = random.randrange(0, screen_height)
        tmp = pygame.Rect(x, y, 28, 28)
        ok = True
        for wall in all_walls:
            if tmp.colliderect(wall.hitbox):
                ok = False
                break
        for tail in snake_1.elements:
            if tmp.colliderect(tail[2]):
                ok = False
                break
        if single_player == False:
            for tail in snake_2.elements:
                if tmp.colliderect(tail[2]):
                    ok = False
                    break
        for food in foods:
            if tmp.colliderect(food.hitbox):
                ok = False
        if ok:
            foods.append(Food(x, y, (255, 0, 0)))
        else:
            food_spawner()
                

def screen_update():
    screen.blit(bg, (0, 0))
    for wall in all_walls:
        wall.draw()
    for food in foods:
        food.draw()
    snake_1.move()
    snake_1.draw()
    if single_player == False:
        snake_2.move()
        snake_2.draw()

def snake_move(keys):
    if keys[pygame.K_d] and not snake_1.left:
        snake_1.right = True
        snake_1.down = snake_1.up = snake_1.left = False
        snake_1.speed = [snake_1.speed_, 0]
    elif keys[pygame.K_a] and not snake_1.right:
        snake_1.left = True 
        snake_1.down = snake_1.up = snake_1.right = False 
        snake_1.speed = [-snake_1.speed_, 0]
    elif keys[pygame.K_w] and not snake_1.down:
        snake_1.up = True
        snake_1.down = snake_1.right = snake_1.left = False
        snake_1.speed = [0, -snake_1.speed_]
    elif keys[pygame.K_s] and not snake_1.up:
        snake_1.down = True
        snake_1.right = snake_1.up = snake_1.left = False 
        snake_1.speed = [0, snake_1.speed_]
    else:
        if snake_1.left:
            snake_1.speed = [-snake_1.speed_, 0]
        elif snake_1.right:
            snake_1.speed = [snake_1.speed_, 0]
        elif snake_1.up:
            snake_1.speed = [0, -snake_1.speed_]
        elif snake_1.down:
            snake_1.speed = [0, snake_1.speed_]
    
    if single_player == False:
        if keys[pygame.K_RIGHT] and not snake_2.left:
            snake_2.right = True
            snake_2.down = snake_2.up = snake_2.left = False
            snake_2.speed = [snake_2.speed_, 0]
        elif keys[pygame.K_LEFT] and not snake_2.right:
            snake_2.left = True 
            snake_2.down = snake_2.up = snake_2.right = False 
            snake_2.speed = [-snake_2.speed_, 0]
        elif keys[pygame.K_UP] and not snake_2.down:
            snake_2.up = True
            snake_2.down = snake_2.right = snake_2.left = False
            snake_2.speed = [0, -snake_2.speed_]
        elif keys[pygame.K_DOWN] and not snake_2.up:
            snake_2.down = True
            snake_2.right = snake_2.up = snake_2.left = False 
            snake_2.speed = [0, snake_2.speed_]
        else:
            if snake_2.left:
                snake_2.speed = [-snake_2.speed_, 0]
            elif snake_2.right:
                snake_2.speed = [snake_2.speed_, 0]
            elif snake_2.up:
                snake_2.speed = [0, -snake_2.speed_]
            elif snake_2.down:
                snake_2.speed = [0, snake_2.speed_]

def show_score():
    font = pygame.font.SysFont('consolas', italic = True, bold = True, size = 24)
    score_1_text = font.render(f'Score: {snake_1.score}', True, (0, 0, 0))
    screen.blit(score_1_text, (40, 40))
    if single_player == False: 
        score_2_text = font.render(f'Score: {snake_2.score}', True, (0, 0, 0))
        screen.blit(score_2_text, (650, 40))

    

def snake_collide(): # all collisions with snakes
    for food in foods:
        if snake_1.elements[0][2].colliderect(food.hitbox):
            snake_1.score += 1
            foods.remove(food)
            snake_1.add_tail()
        if single_player == False:
            if snake_2.elements[0][2].colliderect(food.hitbox):
                snake_2.score += 1
                foods.remove(food)
                snake_2.add_tail()
    for wall in all_walls:
        if snake_1.elements[0][2].colliderect(wall.hitbox):
            if single_player:
                final_scene('3')
            else:
                final_scene('1')
        if single_player == False:
            if snake_2.elements[0][2].colliderect(wall.hitbox):
                final_scene('2')
    if single_player:
        head_1 = snake_1.elements[0][2]
        for i in range(3, snake_1.size):
            if head_1.colliderect(snake_1.elements[i][2]):
                final_scene('3')
    elif single_player == False:
        head_1 = snake_1.elements[0][2]
        head_2 = snake_2.elements[0][2]
        for i in range(3, snake_1.size):
            if head_1.colliderect(snake_1.elements[i][2]):
                final_scene('1')
        for i in range(3, snake_2.size):
            if head_2.colliderect(snake_2.elements[i][2]):
                final_scene('2')
        for tail in snake_1.elements:
            if head_2.colliderect(tail[2]):
                final_scene('2')
        for tail in snake_2.elements:
            if head_1.colliderect(tail[2]):
                final_scene('1')



def choose_level():
    global level_num, FPS, save
    save = False
    screen.fill((255, 255, 255))
    level_1 = Button((0, 50, 255), 30, 360, 180, 80, 'Level 1')
    level_2 = Button((0, 50, 255), 300, 360, 180, 80, 'Level 2')
    level_3 = Button((0, 50, 255), 550, 360, 180, 80, 'Level 3')
    single_text = Button((0, 50, 255), 140, 40, 240, 80, 'Single Player')
    two_text = Button((0, 50, 255), 480, 40, 200, 80, 'Two Players')
    quit_text = Button((0, 50, 255), 320, 520, 140, 80, 'Quit')
    last_saving_text = Button((0, 50, 255), 290, 200, 210, 80, 'Last Savings')
    run = True
    while run:
        global single_player
        level_1.draw(screen, 1)
        level_2.draw(screen, 1)
        level_3.draw(screen, 1)
        single_text.draw(screen, 1)
        two_text.draw(screen, 1)
        quit_text.draw(screen, 1)
        last_saving_text.draw(screen, 1)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if single_text.isOver(pos):
                    single_player = True
                    single_text.color = (0, 255, 0)
                    two_text.color = (0, 50, 255)
                elif two_text.isOver(pos):
                    single_player = False
                    two_text.color = (0, 255, 0)
                    single_text.color = (0, 50, 255)
                elif level_1.isOver(pos):
                    level_num = 1
                    FPS = 16
                    run = False
                elif level_2.isOver(pos):
                    level_num = 2
                    FPS = 18
                    run = False
                elif level_3.isOver(pos):
                    level_num = 3
                    FPS = 20
                    run = False
                elif quit_text.isOver(pos):
                    run = False
                    pygame.quit()
                    sys.exit()
                elif last_saving_text.isOver(pos):
                    save = True
                    run = False
                    start_from_savings()

        pygame.display.update()
        clock.tick(FPS)
    
def final_scene(x):
    # 1 - snake_1 lost, 2 - snake_2 lost, 3 - snake_1 lost single player
    save_score()

    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('consolas', 70)
    font_2 = pygame.font.SysFont('consolas', 30)

    text_1 = font.render('Player 1 Lost', True, (0, 255, 0))
    text_2 = font.render('Player 2 Lost', True, (0, 255, 0))
    text_3 = font.render(f'Your Score: {snake_1.score}', True, (0, 255, 0))
    score_1 = font_2.render(f'Player 1: {snake_1.score}', True, (0, 255, 0))
    if single_player == False: score_2 = font_2.render(f'Player 2: {snake_2.score}', True, (0, 255, 0))

    menu_text = Button((0, 255, 0), 320, 350, 180, 80, 'Menu')
    quit_text = Button((0, 255, 0), 320, 450, 180, 80, 'Quit')

    run = True
    while run:
        if x == '1':
            screen.blit(text_1, (160, 100))
            screen.blit(score_1, (180, 240))
            screen.blit(score_2, (450, 240))
        elif x == '2':
            screen.blit(text_2, (160, 100))
            screen.blit(score_1, (180, 240))
            screen.blit(score_2, (450, 240))
        else:
            screen.blit(text_3, (140, 160))
        quit_text.draw(screen)
        menu_text.draw(screen)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_text.isOver(pos):
                    initialize()
                if quit_text.isOver(pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        clock.tick(FPS)


def pause_game():
    screen.fill((0, 0, 0))
    continue_text = Button((0, 255, 0), 300, 150, 200, 80, 'Continue')
    save_the_game_text = Button((0, 255, 0), 280, 260, 240, 80, 'Save the game')
    quit_text = Button((0, 255, 0), 320, 380, 160, 80, 'Quit')
    run = True
    while run:
        save_the_game_text.draw(screen)
        quit_text.draw(screen)
        continue_text.draw(screen)

        for event in pygame.event.get():

            pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_text.isOver(pos):
                    run = False
                elif save_the_game_text.isOver(pos):
                    save_the_game()
                    run = False
                elif quit_text.isOver(pos):
                    run = False
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        clock.tick(FPS)

def comparator(a, b):
    if a['score'] > b['score']:
        return -1
    if a['score'] < b['score']:
        return 1
    
    if a['login'] > b['login']:
        return 1
    if a['login'] < b['login']:
        return -1

    return 0
    

def save_score():
    found = False
    for i in range(len(score_data['users'])):
        if score_data['users'][i]['login'] == login:
            old_score = score_data['users'][i]['score']
            score_data['users'][i]['score'] = max(snake_1.score, old_score)
            found = True
            break

    if not found:
        score_data['users'].append({'login':login, 'score':snake_1.score})

    score_data['users'] = sorted(score_data['users'], key=cmp_to_key(comparator))
    with open('user data/score.txt', 'w') as f:
        json.dump(score_data, f, indent = 2)

def save_the_game():
    global foods, FPS, snake_1, snake_2, level_num, single_player
    food = []

    save_score()

    for item in foods:
        food.append([item.x, item.y])
    data = {
        'foods' : food,
        'fps' : FPS, 
        'snake_1' : snake_1.hitbox_coord,
        'snake_1_score_and_size' : [snake_1.score, snake_1.size],
        'snake_1_left' : snake_1.left,
        'snake_1_right' : snake_1.right,
        'snake_1_up' : snake_1.up,
        'snake_1_down' : snake_1.down,
        'level' : level_num,
        'player_mode' : single_player
    }
    if single_player == False: 
        data['snake_2'] = snake_2.hitbox_coord
        data['snake_2_score_and_size'] = [snake_2.score, snake_2.size]
        data['snake_2_left'] = snake_2.left
        data['snake_2_right'] = snake_2.right
        data['snake_2_up'] = snake_2.up
        data['snake_2_down'] = snake_2.down
    with open('data.txt', 'w') as f:
        json.dump(data, f, indent = 4)

def start_from_savings():
    global foods, FPS, snake_1, snake_2, level_num, single_player   

    with open('data.txt', 'r') as file_:
        f = json.load(file_)
        for item in f['foods']:
            foods.append(Food(item[0], item[1], (255, 0, 0)))
        FPS = f['fps']
        level_num = f['level']
        single_player = f['player_mode']
    initialize_snakes()
    snake_1.restart(f['snake_1'], f['snake_1_score_and_size'][0], f['snake_1_score_and_size'][1], f['snake_1_left'], f['snake_1_right'], f['snake_1_up'], f['snake_1_down'])
    if single_player == False:
        snake_2.restart(f['snake_2'],  f['snake_2_score_and_size'][0], f['snake_2_score_and_size'][1], f['snake_2_left'], f['snake_2_right'], f['snake_2_up'], f['snake_2_down'])


def initialize_snakes():
    global snake_1, snake_2
    snake_1 = Snake(x = 64, y = 580, color = (0, 255, 102))
    if single_player == False: snake_2 = Snake(x = 320, y = 400, color = (51, 153, 0))   

def run_game():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pause_game()

        food_spawner()
        snake_move(keys)
        snake_collide()
        screen_update()

        show_score()

        pygame.display.update()
        clock.tick(FPS)



def log():
    logged = False

    while not logged:
        global login, password

        login = input('login: ').strip()
        password = input('password: ').strip()
        password = hashlib.md5(password.encode('utf-8')).hexdigest()

        find = False
        correct = False

        f = open('user data/user_info.txt', 'r')
        data = json.loads(f.read())
        f.close()

        for user in data['users']:    
            log, pas = user['login'], user['password']
            if log == login and password == pas:
                logged = True
                correct = True
                break
            elif log == login:
                find = True
                break
        
        if not find and not correct:
            data['users'].append({'login' : login, 'password' : password})
            with open('user data/user_info.txt', 'w') as f:
                json.dump(data, f, indent = 2)
            logged = True
        elif not correct:
            print('Wrong password!')

    global score_data
    f = open('user data/score.txt', 'r')
    score_data = json.loads(f.read())
    f.close()

    initialize()

def initialize():
    global screen_width, screen_height, screen, bg, clock, FPS

    pygame.init()

    screen_width = 800
    screen_height = 640

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Snake')
    bg = pygame.image.load('pictures/grass.jpg')

    clock = pygame.time.Clock()
    FPS = 16

    run_the_game()


def run_the_game():
    all_walls.clear()
    foods.clear()
    choose_level()
    if save == False:           
        initialize_snakes()
    create_map(level_num)
    run_game()

log()
