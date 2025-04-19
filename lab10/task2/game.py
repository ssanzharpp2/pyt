import pygame
import random
import time
import psycopg2
from pconfig import load_config


def user(username):
    config = load_config()
    conn = psycopg2.connect(**config)
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    row = cur.fetchone()
    if row:
        user_id = row[0]
        cur.execute("SELECT level, score FROM user_score WHERE user_id = %s", (user_id,))
        score_row = cur.fetchone()
        if score_row:
            level, score = score_row
        else:
            level, score = 1, 0
            cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)",
                        (user_id, level, score))
            conn.commit()
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        level, score = 1, 0
        cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)",
                    (user_id, level, score))
        conn.commit()

    return conn, cur, user_id, level, score

def save(cur, conn, user_id, level, score):
    cur.execute("UPDATE user_score SET level = %s, score = %s, saved_at = NOW() WHERE user_id = %s",
                (level, score, user_id))
    conn.commit()


pygame.init()
w, h = 600, 400
s = 20
sw = w // s
sh = h // s
speed = 5
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 20)
font1 = pygame.font.SysFont('arial', 40)

white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
gray = (100, 100, 100)
yellow = (255, 255, 0)

restart_text = font.render("Press to restart", True, white)
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

class SpFood:
    def __init__(self, s_pos):
        self.pos = (0, 0)
        self.sp = time.time()
        self.app = False
        self.col = yellow

    def spawn(self, s_pos):
        self.pos = (random.randint(0, sw - 1), random.randint(0, sh - 1))
        while self.pos in s_pos:
            self.pos = (random.randint(0, sw - 1), random.randint(0, sh - 1))
        self.sp = time.time()
        self.app = True

    def appear(self):
        if self.app and (time.time() - self.sp > 3):
            self.app = False

    def rend(self, surface):
        if self.app:
            rect = pygame.Rect((self.pos[0] * s, self.pos[1] * s), (s, s))
            pygame.draw.rect(surface, self.col, rect)
            pygame.draw.rect(surface, black, rect, 1)

def draw_grid(surface):
    for y in range(0, h, s):
        for x in range(0, w, s):
            rect = pygame.Rect((x, y), (s, s))
            pygame.draw.rect(surface, gray, rect, 1)

def show_game_over(surface):
    surface.fill(black)
    text = font1.render("GAME OVER", True, red)
    text_rect = text.get_rect(center=(w // 2, h // 2 - 50))
    surface.blit(text, text_rect)
    surface.blit(restart_text, restart_rect)
    pygame.display.update()

def main():
    username = input("Nickname: ")
    conn, cur, user_id, saved_level, saved_score = user(username)

    snake = Snake()
    snake.level = saved_level
    snake.score = saved_score

    food = Food(snake.pos)
    spfood = SpFood(snake.pos)
    current_speed = speed + (snake.level - 1) * 2
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save(cur, conn, user_id, snake.level, snake.score)
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
                    elif event.key == pygame.K_p:
                        print("Pause. Your progress has been saved.")
                        save(cur, conn, user_id, snake.level, snake.score)
                        paused = True
                        while paused:
                            for pause_event in pygame.event.get():
                                if pause_event.type == pygame.KEYDOWN and pause_event.key == pygame.K_p:
                                    paused = False

        mouse = pygame.mouse.get_pos()
        if game_over and restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            snake.reset()
            food.food_pos(snake.pos)
            current_speed = speed
            game_over = False

        if not game_over:
            game_over = snake.update()

            if snake.headpos() == food.position:
                snake.length += 1
                snake.score += 10
                food.food_pos(snake.pos)
                if snake.length % 6 == 0:
                    snake.level += 1
                    current_speed += 2

            spfood.appear()
            if snake.headpos() == spfood.pos and spfood.app:
                snake.length += 3
                snake.score += 30
                spfood.app = False

            if snake.length % 6 == 0 and not spfood.app:
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
            save(cur, conn, user_id, snake.level, snake.score)
            show_game_over(screen)

if __name__ == "__main__":
    main()
