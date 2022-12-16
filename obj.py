from constants import *
import pygame
import random
from text import *

pygame.init()


class Food:
    # This class represents the food that is eaten by the snake
    # Attributes:
    #               pts(int) - the amount of points that is given for eating this type of food
    #               x(int) - x coordinate of food's position
    #               y(int) - y coordinate of food's position
    #               eaten(bool) - variable that is False if the piece is eaten, False otherwise
    def __init__(self, level_map):
        pos_chosen = False
        while not pos_chosen:
            # Food spawns randomly, but avoiding the rocks and the part of the screen where the score is shown.
            x = random.randint(6, dis_width / snake_block - 1)
            y = random.randint(3, dis_height / snake_block - 1)
            if level_map[y][x] == 0:
                self.x = x * 10
                self.y = y * 10
                pos_chosen = True
        self.pts = 1
        self.eaten = False

    def check_life(self, snake_x, snake_y):
        # Checks if the snake has eaten the food
        # Arguments:     snake_x(int) - snake's x coordinate
        #                snake_y(int) - snake's y coordinate
        if self.x == snake_x and self.y == snake_y:
            self.eaten = True
            return True
        return False

    def draw(self):
        # Draws the food as a green pygame.rectangle in (x,y) at the size of one snake_block
        if not self.eaten:
            pygame.draw.rect(dis, green, [self.x, self.y, snake_block, snake_block])


class Rock:
    # This class represents rocks, that serve as obstacles on snake's way
    # Attributes:   x(int) - x coordinate of rock's position
    #               y(int) - y coordinate of rock's position
    def __init__(self, x, y):  # Takes x and y coordinates of rock's position
        self.x = x
        self.y = y

    def draw(self):
        # Draws the rock as a black pygame.rectangle in (x,y) at the size of one snake_block
        pygame.draw.rect(dis, black, [self.x, self.y, snake_block, snake_block])


class Snake:
    # Class that represents the snake, which is the main object of the game
    # Attributes:   Head([int, int]) - list with x and y coordinates of snake's head position
    #               parts(list) - 2D list of the coordinates of each piece of the snake
    #               x(int) - x coordinate of new head's position
    #               y(int) - y coordinate of new head's position
    #               dx(int) - "x component of snake's velocity": negative when it's moving to the left,
    #                                                            positive when it's moving to the right,
    #                                                            0 when it's moving vertically
    #               dy(int) - same as dx, but for y-axis
    #               len(int) - the current length of the snake
    #               alive(bool) - variable that is False when the snake is dead, True otherwise
    #               speed(int) - the speed of the snake. Rises when the snake eats food (obviously, it gains energy);
    #                            the base speed depends on the chosen level
    def __init__(self):
        self.Head = [dis_width / 2, dis_height / 2]  # Snake spawns in the middle of the screen
        self.parts = [self.Head]
        self.x = self.Head[0]
        self.y = self.Head[1]
        self.dx = 0
        self.dy = 0
        self.len = 1
        self.alive = True
        self.speed = snake_basespeed

    def turn(self, event):
        # The following function is responsible for snake's turns when keys WASD are pressed
        # Arguments:    event(pygame.event) - the Event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.dx = -snake_block
                self.dy = 0
            elif event.key == pygame.K_d:
                self.dx = snake_block
                self.dy = 0
            elif event.key == pygame.K_w:
                self.dy = -snake_block
                self.dx = 0
            elif event.key == pygame.K_s:
                self.dy = snake_block
                self.dx = 0

    def evolve(self, rocks):
        # The following function is responsible for snake's evolution at every quantum of time
        # Arguments:    rocks(list() - list of class Rock objects, that represent the rock displaced on the map
        self.check_suicide()
        self.check_rocks(rocks)
        self.check_border()
        if self.alive:  # If the snake has survived, changes its coordinates and moves it by updating the head
            # and removing the last piece
            self.x += self.dx
            self.y += self.dy
            self.Head = list()
            self.Head.append(self.x)
            self.Head.append(self.y)
            self.parts.append(self.Head)
            if len(self.parts) > self.len:
                del self.parts[0]

    def check_suicide(self):
        # The following function checks if the snake has crossed itself
        for x in self.parts[:-1]:
            if x == self.Head:
                self.alive = False

    def check_rocks(self, rocks):
        # The following function checks if the snake has hit any rocks
        # Arguments:    rocks(list) - list of class Rock objects, which represents all the rocks displaced on the map
        for rock in rocks:
            if rock.x == self.Head[0] and rock.y == self.Head[1]:
                self.alive = False

    def check_border(self):
        # The following function checks if the snake has hit the border of the closed subset of R^2 (aka the map),
        # where the game takes place
        if self.Head[0] >= dis_width or self.Head[0] < 0 or self.Head[1] >= dis_height or self.Head[1] < 0:
            self.alive = False

    def draw(self):
        # The following function draws every piece of the snake as a red pygame.rect at the size of one snake_block
        for x in self.parts:
            pygame.draw.rect(dis, red, [x[0], x[1], snake_block, snake_block])


class Button:
    # This class represents the buttons, that are used as a form of interactive interaction with the user
    # Attributes:   name(str) - "name" of the button - the phrase which is written on it
    #               chosen(bool) - the variable that is True when the button is "active" (it is lit), False otherwise
    #               x(int) - x coordinate of the top left corner of the button
    #               y(int) - y coordinate of the top left corner of the button
    def __init__(self, x=0, y=0, name="Level"):
        self.name = name
        self.chosen = False
        self.x = x
        self.y = y

    def draw(self):
        # The following function draws the button as a pygame.rect located in (x,y),
        # at the size of (dis_width / 4, dis_height / 8)
        # if the button is "active" adds a yellow border around it
        if self.chosen:
            pygame.draw.rect(dis, yellow, [self.x - 10, self.y - 10, dis_width / 4 + 20, dis_height / 8 + 20])
            pygame.draw.rect(dis, black, [self.x, self.y, dis_width / 4, dis_height / 8])
            message(self.name, white, self.x + 40, self.y + 10)
        if not self.chosen:
            pygame.draw.rect(dis, black, [self.x, self.y, dis_width / 4, dis_height / 8])
            message(self.name, white, self.x + 20, self.y + 20)


# The list of the buttons corresponding to available levels (currently 3)
buttons = list()
buttons.append(Button(dis_width / 3, dis_height / 8, "Level 0"))
buttons.append(Button(dis_width / 3, 5 * dis_height / 16, "Level 1"))
buttons.append(Button(dis_width / 3, dis_height / 2, "Level 2"))
