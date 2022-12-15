from constants import *
import pygame
import random

pygame.init()


class Food:
    def __init__(self, map):
        chosen = False
        while not chosen:
            x = random.randint(0, dis_width / snake_block - 1)
            y = random.randint(0, dis_height / snake_block - 1)
            if map[y][x] == 0:
                self.x = x * 10
                self.y = y * 10
                chosen = True
        self.pts = 1
        self.eaten = False

    def check_life(self, snake_x, snake_y):
        if self.x == snake_x and self.y == snake_y:
            self.eaten = True
            return True
        return False

    def draw(self):
        if not self.eaten:
            pygame.draw.rect(dis, green, [self.x, self.y, snake_block, snake_block])


class Rock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(dis, black, [self.x, self.y, snake_block, snake_block])


class Snake:
    def __init__(self):
        self.Head = [dis_width / 2, dis_height / 2]
        self.parts = [self.Head]
        self.x = self.Head[0]
        self.y = self.Head[1]
        self.dx = 0
        self.dy = 0
        self.len = 1
        self.alive = True

    def turn(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.dx = -snake_block
                self.dy = 0
            elif event.key == pygame.K_RIGHT:
                self.dx = snake_block
                self.dy = 0
            elif event.key == pygame.K_UP:
                self.dy = -snake_block
                self.dx = 0
            elif event.key == pygame.K_DOWN:
                self.dy = snake_block
                self.dx = 0

    def evolve(self):
        self.x += self.dx
        self.y += self.dy
        self.Head = list()
        self.Head.append(self.x)
        self.Head.append(self.y)
        self.parts.append(self.Head)
        if len(self.parts) > self.len:
            del self.parts[0]

    def check_suicide(self):
        for x in self.parts[:-1]:
            if x == self.Head:
                self.alive = False

    def check_rocks(self, rocks):
        for rock in rocks:
            if rock.x  == self.Head[0] and rock.y  == self.Head[1]:
                self.alive = False

    def check_border(self):
        if self.Head[0] >= dis_width or self.Head[0] < 0 or self.Head[1] >= dis_height or self.Head[1] < 0:
            self.alive = False

    def draw(self):
        for x in self.parts:
            pygame.draw.rect(dis, red, [x[0], x[1], snake_block, snake_block])


class Button():
    def __init__(self, x=0, y=0, name="Level"):
        self.name = name
        self.chosen = False
        self.x = x
        self.y = y

    def draw(self):
        if self.chosen:
            pygame.draw.rect(dis, yellow, [self.x - 10, self.y - 10, dis_width / 4 + 20, dis_height / 8 + 20])
            pygame.draw.rect(dis, black, [self.x, self.y, dis_width / 4, dis_height / 8])
        if not self.chosen:
            pygame.draw.rect(dis, black, [self.x, self.y, dis_width / 4, dis_height / 8])


"working with buttons"
buttons = list()
buttons.append(Button(dis_width / 3, dis_height / 8, "Level 0"))
buttons.append(Button(dis_width / 3, 5 * dis_height / 16, "Level 1"))
buttons.append(Button(dis_width / 3, dis_height / 2, "Level 2"))
