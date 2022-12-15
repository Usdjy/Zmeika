"File of constants used in the project"
import pygame
pygame.init()
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
clock = pygame.time.Clock()
snake_block = 10
snake_basespeed = 5
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 15)