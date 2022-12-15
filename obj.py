from constants import *
import pygame
import random


class Food:
    def __init__(self):
        self.x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        self.y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
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

    def check_border(self):
        if self.Head[0] >= dis_width or self.Head[0] < 0 or self.Head[1] >= dis_height or self.Head[1] < 0:
            self.alive = False

    def draw(self):
        for x in self.parts:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
