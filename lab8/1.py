import pygame 
import random
pygame.init()
screen = pygame.display.set_mode((600,464))

road = pygame.image.load('road.png')
car = pygame.image.load('car.png')
enem = pygame.image.load('1enemy.png') 
enem = pygame.transform.scale(enem, (100,180))
clock = pygame.time.Clock()
gameplay = True

font = pygame.font.SysFont('Arial', 80)
font1 = pygame.font.SysFont('Arial', 30)
s = font.render(f'GAME OVER', False, (150, 0, 0))
word = font1.render('RESTART', False, (255, 255, 255))
word_rec = word.get_rect(topleft = (230, 200))

bx = 300
bgy = 0
enemies = []
timer = 0
w = 50
h = 100

running = True
while running:
    if gameplay:
        screen.blit(road,(0,bgy))
        screen.blit(road,(0,bgy-464))
        screen.blit(car, (bx, 300))
        bgy += 6
        if bgy >= 464:
            bgy = 0
        timer += 1
        if timer >= 60: 
            if random.random():  
                enemies.append({
                    'x': random.randint(120, 400),
                    'y': -200,  
                    'collision': False
                })
            timer = 0
        for enemy in enemies[:]:  
            enemy['y'] += 6 
            car_rect = pygame.Rect(bx, 300, 55, 155)
            en_rect = pygame.Rect(enemy['x'], enemy['y'], 55, 155)
            if car_rect.colliderect(en_rect) and not enemy['collision']:
                enemy['collision'] = True
                gameplay = False
            elif enemy['y'] > 464:
                enemies.remove(enemy)
        for enemy in enemies:
            screen.blit(enem, (enemy['x'], enemy['y']))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and bx > 120:
            bx -= 4
        elif keys[pygame.K_RIGHT] and bx < 400:
            bx += 4
    else:
        screen.fill((0,0,0))
        screen.blit(s, (100, 90))
        screen.blit(word, (230, 200))
        mouse = pygame.mouse.get_pos()
        if word_rec.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            bx = 300
            enemies.clear()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False      
    pygame.display.update()
    clock.tick(60)



    import pygame
import random
import time

pygame.init()

w, h = 600, 400
s = 20
sw = w // s
sh = h // s
speed= 5

white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
gray = (100, 100, 100)

screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

font = pygame.font.SysFont('arial', 20)
font1 = pygame.font.SysFont('arial', 40)

restart_text = font.render("Press SPACE to restart", True, white)
restart_rect = restart_text.get_rect(center=(w//2, h//2 + 50))

class Snake:
    def __init__(self):
        self.pos = [(sw // 2, sh // 2)]
        self.D = (1, 0)
        self.length = 1
        self.score = 0
        self.level = 1
        
    def headpos(self):
        return self.pos[0]
    
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
    
    def reset(self):
        self.pos = [(sw // 2, sh // 2)]
        self.D = (1, 0)
        self.length = 1
        self.score = 0
        self.level = 1
    
    def render(self, surface):
        for i, p in enumerate(self.pos):
            color = green if i == 0 else blue  
            rect = pygame.Rect((p[0] * s, p[1] * s), (s, s))
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, black, rect, 1)

class Food:
    def __init__(self, s_pos):
        self.position = (0, 0)
        self.food_pos(s_pos)
        self.color = red
    
    def food_pos(self, s_pos):
        while True:
            self.position = (random.randint(0, sw - 1), random.randint(0, sh - 1))
            if self.position not in s_pos:
                break
    
    def render(self, surface):
        rect = pygame.Rect((self.position[0] * s, self.position[1] * s), (s, s))
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, black, rect, 1)

def draw_grid(surface):
    for y in range(0, h, s):
        for x in range(0, w, s):
            rect = pygame.Rect((x, y), (s, s))
            pygame.draw.rect(surface, gray, rect, 1)

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

            if snake.headpos() == food.position:
                snake.length += 1
                snake.score += 10
                food.food_pos(snake.pos)

                if snake.length % 6 == 0:
                    snake.level += 1
                    current_speed+= 2  

            screen.fill(black)
            draw_grid(screen)
            snake.render(screen)
            food.render(screen)

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

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    tools = ['pen', 'rectangle', 'circle', 'eraser']
    current_tool = 'pen'
    color_mode = 'blue'
    radius = 15
    drawing = False
    start_pos = (0, 0)
    points = []
    
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
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                if event.key == pygame.K_p:
                    current_tool = 'pen'
                elif event.key == pygame.K_r:
                    current_tool = 'rectangle'
                elif event.key == pygame.K_c:
                    current_tool = 'circle'
                elif event.key == pygame.K_e:
                    current_tool = 'eraser'
                
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

                if event.key == pygame.K_DELETE:
                    screen.fill((0, 0, 0))

            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = pygame.mouse.get_pos()
                if current_tool == 'pen':
                    points.append(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False 
                start_pos = pygame.mouse.get_pos()
                
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                if current_tool == 'rectangle':
                    end_pos = event.pos
                    rect = pygame.Rect(
                        min(start_pos[0], end_pos[0]),
                        min(start_pos[1], end_pos[1]),
                        abs(end_pos[0] - start_pos[0]),
                        abs(end_pos[1] - start_pos[1])
                    )
                    pygame.draw.rect(screen, colors[color_mode], rect, radius if radius < 10 else 3)
                elif current_tool == 'circle':
                    end_pos = event.pos
                    center = start_pos
                    radius_circle = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)**0.5)
                    pygame.draw.circle(screen, colors[color_mode], center, radius_circle, radius if radius < 10 else 3)
            
            if event.type == pygame.MOUSEMOTION and drawing:
                if current_tool == 'pen':
                    points.append(event.pos)
                    points = points[-512:] 
                elif current_tool == 'eraser':
                    pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)

        screen.fill((0, 0, 0))

        if len(points) > 1 and current_tool == 'pen':
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, color_mode, colors)
                i += 1

        if drawing and current_tool in ['rectangle', 'circle']:
            current_pos = pygame.mouse.get_pos()
            if current_tool == 'rectangle':
                rect = pygame.Rect(
                    min(start_pos[0], current_pos[0]),
                    min(start_pos[1], current_pos[1]),
                    abs(current_pos[0] - start_pos[0]),
                    abs(current_pos[1] - start_pos[1])
                )
                pygame.draw.rect(screen, colors[color_mode], rect, 1)
            elif current_tool == 'circle':
                radius_preview = int(((current_pos[0]-start_pos[0])**2 + (current_pos[1]-start_pos[1])**2)**0.5)
                pygame.draw.circle(screen, colors[color_mode], start_pos, radius_preview, 1)

        draw_ui(screen, font, current_tool, color_mode, radius, colors)
        
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode, colors):
    if color_mode == 'eraser':
        color = (0, 0, 0)
    else:
        color = colors[color_mode]
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def draw_ui(screen, font, current_tool, color_mode, radius, colors):

    tool_text = font.render(f"Tool: {current_tool} (P=Pen, R=Rectangle, C=Circle, E=Eraser)", True, (255, 255, 255))
    color_text = font.render(f"Color: {color_mode} (1-8 to change)", True, (255, 255, 255))
    size_text = font.render(f"Size: {radius} (Left/Right click to change)", True, (255, 255, 255))
    clear_text = font.render("Press DELETE to clear", True, (255, 255, 255))
    
    screen.blit(tool_text, (10, 10))
    screen.blit(color_text, (10, 30))
    screen.blit(size_text, (10, 50))
    screen.blit(clear_text, (10, 70))

    for i, (name, color) in enumerate(colors.items()):
        pygame.draw.rect(screen, color, (10 + i*30, 100, 25, 25))
        if name == color_mode:
            pygame.draw.rect(screen, (255, 255, 255), (10 + i*30, 100, 25, 25), 2)

if __name__ == "__main__":
    main()
