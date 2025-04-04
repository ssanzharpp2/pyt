import pygame 
import random
pygame.init()
screen = pygame.display.set_mode((600,464))

road = pygame.image.load('C:/Users/Admin/work/lab8/road.png')
car = pygame.image.load('C:/Users/Admin/work/lab8/car.png')
enem = pygame.image.load('C:/Users/Admin/work/lab8/1enemy.png') 
coin = pygame.image.load('C:/Users/Admin/work/coin.png')
coin = pygame.transform.scale(coin, (40,40))
enem = pygame.transform.scale(enem, (100,180))
clock = pygame.time.Clock()
gameplay = True # check for game over

font = pygame.font.SysFont('Arial', 80)
font1 = pygame.font.SysFont('Arial', 30)
s = font.render(f'GAME OVER', False, (150, 0, 0))
word = font1.render('RESTART', False, (255, 255, 255))
word_rec = word.get_rect(topleft = (230, 250))
# Variables
bx = 300 # player initial position
bgy = 0 # for move background
coins = []
enemies = []
enem_timer = 0
coin_timer = 0
w = 50
h = 100
score = 0 # Counter for score
ssc = 0 # For showing current score
en_sp = 6 # enemies speed
hscore = 0 # The highest score in one game session
pl_sp = 4 # Player speed

running = True
while running:
    if gameplay:
        screen.blit(road,(0,bgy))
        screen.blit(road,(0,bgy-464))
        screen.blit(car, (bx, 300))
        # moving of 
        bgy += 6
        if bgy >= 464:
            bgy = 0
        # Random enemies
        enem_timer += 1
        if enem_timer >= 60: 
            if random.random():  
                enemies.append({
                    'x': random.randint(120, 400),
                    'y': -200,  
                    'collision': False
                })
            enem_timer = 0
        for enemy in enemies[:]:  
            enemy['y'] += en_sp 
            car_rect = pygame.Rect(bx, 300, 55, 155)
            en_rect = pygame.Rect(enemy['x'], enemy['y'], 55, 155)
            if car_rect.colliderect(en_rect) and not enemy['collision']:
                enemy['collision'] = True
                gameplay = False
            elif enemy['y'] > 464:
                enemies.remove(enemy)
        for enemy in enemies:
            screen.blit(enem, (enemy['x'], enemy['y']))
        # random coins
        coin_timer += 1
        if coin_timer >= 60:
            if random.random():
                coins.append({
                    'x': random.randint(120,400),
                    'y': -100,
                    'col': False
                })
            coin_timer = 0
        for cn in coins[:]:
            cn['y'] += 5 
            car_rect = pygame.Rect(bx, 300, 55, 155)
            coin_rect = pygame.Rect(cn['x'], cn['y'], 20, 20)
            if car_rect.colliderect(coin_rect) and not cn['col']:
                cn['col'] = True
                score += 1
                ssc = score
                if score % 3 == 0:
                    en_sp += 1
                    pl_sp += 1
                coins.remove(cn)
            elif cn['y'] > 464:
                coins.remove(cn)
        for cn in coins:
            screen.blit(coin, (cn['x'], cn['y']))
        cnum = font1.render(f'Score: {score}', False, (255,255,255))
        cnum_rect = cnum.get_rect(topleft = (20,20))
        screen.blit(cnum, cnum_rect)
        # Movement of player's car
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and bx > 120:
            bx -= pl_sp
        elif keys[pygame.K_RIGHT] and bx < 400:
            bx += pl_sp
    else:
        # game over screen
        screen.fill((0,0,0))
        screen.blit(s, (100, 90))
        screen.blit(word, (230, 270))
        show_score = font1.render(f'Your score: {ssc}', False, (255,255,255))
        screen.blit(show_score, (210,200))
        hscore = max(hscore, ssc)
        high_score = font1.render(f'Record: {hscore}', False, (255,255,255))
        screen.blit(high_score, (450, 10))
        mouse = pygame.mouse.get_pos()
        if word_rec.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            bx = 300
            enemies.clear()
        score = 0
        en_sp = 6
        pl_sp = 4
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False      
    pygame.display.update()
    clock.tick(60)



import pygame
import random
import time

pygame.init()

# Variables
w, h = 600, 400
s = 20
sw = w // s
sh = h // s
speed= 5
sb = 40
ft = time.time()
food_visible = True

# colors
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
gray = (100, 100, 100)
yellow = (255, 255, 0)

screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

font = pygame.font.SysFont('arial', 20)
font1 = pygame.font.SysFont('arial', 40)

restart_text = font.render("Press SPACE to restart", True, white)
restart_rect = restart_text.get_rect(center=(w//2, h//2 + 50))

# snake
class Snake:
    def __init__(self):
        self.pos = [(sw // 2, sh // 2)]
        self.D = (1, 0)
        self.length = 1
        self.score = 0
        self.level = 1
    
    # snake's head tracking
    def headpos(self):
        return self.pos[0]
    
    # adding snake's body
    def update(self):
        head = self.headpos()
        x, y = self.D
        new_head = ((head[0] + x) % sw, (head[1] + y) % sh)

        if new_head[0] < 0 or new_head[0] >= sw or new_head[1] < 0 or new_head[1] >= sh:
            return True 

        if new_head in self.pos[1:]:
            return True  
            
        self.pos.insert(0, new_head)
        if len(self.pos) > self.length:
            self.pos.pop()
        return False
    
    # back to start
    def reset(self):
        self.pos = [(sw // 2, sh // 2)]
        self.D = (1, 0)
        self.length = 1
        self.score = 0
        self.level = 1
    
    # drawing snake 
    def render(self, surface):
        for i, p in enumerate(self.pos):
            color = green if i == 0 else blue  
            rect = pygame.Rect((p[0] * s, p[1] * s), (s, s))
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, black, rect, 1)

# food
class Food:
    def __init__(self, s_pos):
        self.position = (0, 0)
        self.food_pos(s_pos)
        self.color = red
    
    # randomizing food's position
    def food_pos(self, s_pos):
        while True:
            self.position = (random.randint(0, sw - 1), random.randint(0, sh - 1))
            if self.position not in s_pos:
                break
    
    # drawing food
    def render(self, surface):
        rect = pygame.Rect((self.position[0] * s, self.position[1] * s), (s, s))
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, black, rect, 1)

# special food with time disappearing
class SpFood():
    def __init__(self, s_pos):
        self.pos = (0,0)
        self.sp = time.time()
        self.app = False
        self.col = yellow

    # randomizing special food's position 
    def spawn(self, s_pos):
        self.pos = (random.randint(0, sw - 1), random.randint(0, sh - 1))
        while self.pos in s_pos:
            self.pos = (random.randint(0, sw - 1), random.randint(0, sh - 1))
        self.sp = time.time()
        self.app = True

    # timer for food
    def appear(self):
        if self.app and (time.time() - self.sp > 3):
            self.app = False

    # drawing special food
    def rend(self, surface):
        if self.app:
            rect = pygame.Rect((self.pos[0] * s, self.pos[1] * s), (s, s))
            pygame.draw.rect(surface, self.col, rect)
            pygame.draw.rect(surface, black, rect, 1)

# drawing field
def draw_grid(surface):
    for y in range(0, h, s):
        for x in range(0, w, s):
            rect = pygame.Rect((x, y), (s, s))
            pygame.draw.rect(surface, gray, rect, 1)

# game over screen
def show_game_over(surface):
    surface.fill(black)
    text = font1.render("GAME OVER", True, red)
    text_rect = text.get_rect(center=(w//2, h//2 - 50))
    surface.blit(text, text_rect)
    
    
    surface.blit(restart_text, restart_rect)
    
    pygame.display.update()

def main():
    snake = Snake()
    food = Food(snake.pos)
    spfood = SpFood(snake.pos)
    current_speed= speed
    game_over = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if not game_over:
                    if event.key == pygame.K_UP and snake.D != (0, 1):
                        snake.D = (0, -1)
                    elif event.key == pygame.K_DOWN and snake.D != (0, -1):
                        snake.D = (0, 1)
                    elif event.key == pygame.K_LEFT and snake.D != (1, 0):
                        snake.D = (-1, 0)
                    elif event.key == pygame.K_RIGHT and snake.D != (-1, 0):
                        snake.D = (1, 0)
        mouse = pygame.mouse.get_pos()
        if game_over and restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            snake.reset()
            food.food_pos(snake.pos)
            current_speed= speed
            game_over = False
        
        if not game_over:
            game_over = snake.update()

            # checking for eating food
            if snake.headpos() == food.position:
                snake.length += 1
                snake.score += 10
                food.food_pos(snake.pos)

                if snake.length % 6 == 0:
                    snake.level += 1
                    current_speed+= 2  

            # checking for eating special food
            spfood.appear()
            if snake.headpos() == spfood.pos and spfood.app:
                snake.length += 3  
                snake.score += 30
                spfood.app = False

            # condition when special food appear
            if snake.length % 6 ==0  and not spfood.app:
                spfood.spawn(snake.pos)
            

            screen.fill(black)
            draw_grid(screen)
            snake.render(screen)
            food.render(screen)
            spfood.rend(screen)
            
        

            score_text = font.render(f"Score: {snake.score}", True, white)
            level_text = font.render(f"Level: {snake.level}", True, white)
            screen.blit(score_text, (10, 10))
            screen.blit(level_text, (10, 40))
            
            pygame.display.update()
            clock.tick(current_speed)
        else:
            show_game_over(screen)

if __name__ == "__main__":
    main()





import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    # variables
    tools = ['pen', 'rectangle', 'circle', 'eraser', 'square', 'rtriangle', 'etriangle', 'rhombus']
    current_tool = 'pen'
    color_mode = 'blue'
    radius = 5
    drawing = False
    start_pos = (0, 0)
    points = []
    shapes = []
    
    colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'yellow': (255, 255, 0),
        'cyan': (0, 255, 255),
        'magenta': (255, 0, 255)
    }

    font = pygame.font.SysFont('Arial', 18)

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                
                # keys for functions
                if event.key == pygame.K_p:
                    current_tool = 'pen'
                elif event.key == pygame.K_r:
                    current_tool = 'rectangle'
                elif event.key == pygame.K_c:
                    current_tool = 'circle'
                elif event.key == pygame.K_e:
                    current_tool = 'eraser'
                elif event.key == pygame.K_s:
                    current_tool = 'square'
                elif event.key == pygame.K_t:
                    current_tool = 'rtriangle'
                elif event.key == pygame.K_y:
                    current_tool = 'etriangle'
                elif event.key == pygame.K_u:
                    current_tool = 'rhombus'
                
                # keys for colors
                if event.key == pygame.K_1:
                    color_mode = 'red'
                elif event.key == pygame.K_2:
                    color_mode = 'green'
                elif event.key == pygame.K_3:
                    color_mode = 'blue'
                elif event.key == pygame.K_4:
                    color_mode = 'black'
                elif event.key == pygame.K_5:
                    color_mode = 'white'
                elif event.key == pygame.K_6:
                    color_mode = 'yellow'
                elif event.key == pygame.K_7:
                    color_mode = 'cyan'
                elif event.key == pygame.K_8:
                    color_mode = 'magenta'

            # determining start and end positions
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = pygame.mouse.get_pos()
                if current_tool == 'pen':
                    points.append(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                end = event.pos
                w = end[0] - start_pos[0]
                h = end[1] - start_pos[1]
                # save drawing shapes
                shape = (current_tool, start_pos, end, color_mode, radius)
                if current_tool in ['rectangle', 'circle', 'square', 'rtriangle', 'etriangle', 'rhombus', 'eraser']:
                    shapes.append(shape)

            # this part need for remember drawing
            if event.type == pygame.MOUSEMOTION and drawing:
                if current_tool == 'pen':
                    points.append(event.pos)
                    points = points[-128:] 

        screen.fill((0, 0, 0))

        # drawing by pen
        if len(points) > 1 and current_tool == 'pen':
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, color_mode, colors)
                i += 1

        # save drawing shapes
        for tool, start, end, col, rad in shapes:
            w = end[0] - start[0]
            h = end[1] - start[1]
            if tool == 'rectangle':
                rect = pygame.Rect(min(start[0], end[0]), min(start[1], end[1]), abs(w), abs(h))
                pygame.draw.rect(screen, colors[col], rect,2)
            elif tool == 'circle':
                radius_circle = int(((end[0] - start[0])**2 + (end[1] - start[1])**2)**0.5)
                pygame.draw.circle(screen, colors[col], start, radius_circle, 2)
            elif tool == 'rtriangle':
                pygame.draw.polygon(screen, colors[col], [(start[0], start[1]), (end[0], start[1]), (end[0], end[1])], 2)
            elif tool == 'etriangle':
                height = abs(w) * math.sqrt(3) / 2 * (-1 if h < 0 else 1)
                points_triangle = [(start[0], start[1]), (start[0] + w, start[1]), (start[0] + w / 2, start[1] - height)]
                pygame.draw.polygon(screen, colors[col], points_triangle, 2)
            elif tool == 'square':
                size = min(abs(w), abs(h)) * (1 if w >= 0 else -1)
                pygame.draw.rect(screen, colors[col], pygame.Rect(start[0], start[1], size, size), 2)
            elif tool == 'rhombus':
                mid_x, mid_y = (start[0] + end[0]) // 2, (start[1] + end[1]) // 2
                points_rhombus = [(mid_x, start[1]), (end[0], mid_y), (mid_x, end[1]), (start[0], mid_y)]
                pygame.draw.polygon(screen, colors[col], points_rhombus, 2)
            elif tool == 'eraser':
                rect = pygame.Rect(min(start[0], end[0]), min(start[1], end[1]), abs(w), abs(h))
                pygame.draw.rect(screen, colors['black'], rect)


        # drawing shapes
        if drawing and current_tool in ['rectangle', 'circle', 'square', 'rtriangle', 'etriangle', 'rhombus', 'eraser']:
            current_pos = pygame.mouse.get_pos()
            w1 = current_pos[0] - start_pos[0]
            h1 = current_pos[1] - start_pos[1]
            if current_tool == 'rectangle':
                rect = pygame.Rect( min(start_pos[0], current_pos[0]),min(start_pos[1], current_pos[1]), abs(current_pos[0] - start_pos[0]),abs(current_pos[1] - start_pos[1]))
                pygame.draw.rect(screen, colors[color_mode], rect, 2)
            elif current_tool == 'circle':
                radius_preview = int(((current_pos[0]-start_pos[0])**2 + (current_pos[1]-start_pos[1])**2)**0.5)
                pygame.draw.circle(screen, colors[color_mode], start_pos, radius_preview, 1)
            elif current_tool == 'rtriangle':
                pygame.draw.polygon(screen, colors[color_mode], [(start_pos[0], start_pos[1]), (current_pos[0], start_pos[1]), (current_pos[0], current_pos[1])], 2)
            elif current_tool == 'etriangle':
                height = abs(w1) * math.sqrt(3) / 2 * (-1 if h1 < 0 else 1)
                points = [(start_pos[0], start_pos[1]), (start_pos[0] + w1, start_pos[1]), (start_pos[0] + w1 / 2, start_pos[1] - height)]
                pygame.draw.polygon(screen, colors[color_mode], points, 2)
            elif current_tool == 'square':
                size = min(abs(w1), abs(h1)) * (1 if w1 >= 0 else -1)
                pygame.draw.rect(screen, colors[color_mode], pygame.Rect(start_pos[0], start_pos[1], size, size), 2)
            elif current_tool == 'rhombus':
                mid_x, mid_y = (start_pos[0] + current_pos[0]) // 2, (start_pos[1] + current_pos[1]) // 2
                points = [(mid_x, start_pos[1]), (current_pos[0], mid_y), (mid_x, current_pos[1]), (start_pos[0], mid_y)]
                pygame.draw.polygon(screen, colors[color_mode], points, 2)
            elif current_tool == 'eraser':
                rect = pygame.Rect(
                    min(start_pos[0], current_pos[0]),
                    min(start_pos[1], current_pos[1]),
                    abs(current_pos[0] - start_pos[0]),
                    abs(current_pos[1] - start_pos[1])
                )
                pygame.draw.rect(screen, colors['black'], rect)

        # manual for users
        draw_ui(screen, font, current_tool, color_mode, radius, colors)
        
        pygame.display.flip()
        clock.tick(60)

# function for pen drawing 
def drawLineBetween(screen, index, start, end, width, color_mode, colors):
    color = colors[color_mode]
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

# function for manual
def draw_ui(screen, font, current_tool, color_mode, radius, colors):

    tool_text = font.render(f"Tool: {current_tool} (P=Pen, R=Rectangle, C=Circle, E=Eraser, T=Rigt triangle, Y=Equilateral triangle, S=Square, U=Rhombus)", True, (255, 255, 255))
    color_text = font.render(f"Color: {color_mode} (1-8 to change)", True, (255, 255, 255))

    
    screen.blit(tool_text, (10, 10))
    screen.blit(color_text, (10, 30))


    for i, (name, color) in enumerate(colors.items()):
        pygame.draw.rect(screen, color, (10 + i*30, 100, 25, 25))
        if name == color_mode:
            pygame.draw.rect(screen, (255, 255, 255), (10 + i*30, 100, 25, 25), 2)

if __name__ == "__main__":
    main()
