import pygame
import random
import time
import p2
from color_palette import *  # предполагается, что там определены colorGRAY, colorRED и т.д.

pygame.init()
WIDTH = 600
HEIGHT = 600
CELL = 30

font = pygame.font.SysFont("Verdana", 30)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

image_new_level = font.render("NEW LEVEL! +2 TO SPEED", True, "black")         
image_new_level_rect = image_new_level.get_rect(center=(WIDTH // 2, HEIGHT // 2))
image_vse = font.render("Game Over", True, "black")
image_vse_rect = image_vse.get_rect(center=(WIDTH // 2, HEIGHT // 2))

clock = pygame.time.Clock()
fps = 5

score = 0
level = 0
level_up_shown = False
paused = True
running = True

# Классы
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        if self.body[0].x > 19 or self.body[0].x < 0:
            return False
        if self.body[0].y < 0:
            self.body[0].y = 19
        if self.body[0].y > 19:
            self.body[0].y = 0

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))
            food.generate_random_pos()
            return True

class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self):
        self.pos.x = random.randint(0, 19)
        self.pos.y = random.randint(0, 19)

# Сетка
def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)


p2.input_user()
snake = Snake()
food = Food()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            if event.key == pygame.K_p:
                paused = not paused
            if event.key == pygame.K_s and paused:
                p2.process_score(score)

    if not paused:
        screen.fill("black")
        draw_grid()

        if snake.move() == False:
            time.sleep(1)
            screen.fill("red")
            screen.blit(image_vse, image_vse_rect)
            pygame.display.flip()
            p2.process_score(score)
            time.sleep(2)
            running = False

        if snake.check_collision(food):
            score += 1
            level_up_shown = False

        if score != 0 and score % 4 == 0 and not level_up_shown:
            screen.fill("red")
            screen.blit(image_new_level, image_new_level_rect)
            pygame.display.flip()
            time.sleep(1)
            fps += 2
            level += 1
            level_up_shown = True
            p2.process_score(score)

        image_counter = font.render(f"Score: {score}", True, "red")
        image_counter_rect = image_counter.get_rect(center=(450, 20))
        screen.blit(image_counter, image_counter_rect)

        image_level_cnt = font.render(f"Level: {level}", True, "red")
        image_level_cnt_rect = image_level_cnt.get_rect(center=(150, 20))
        screen.blit(image_level_cnt, image_level_cnt_rect)

        snake.draw()
        food.draw()
        pygame.display.flip()
        clock.tick(fps)

pygame.quit()
print(f"{p2.current_user}'s final score: {score}, level: {level}")