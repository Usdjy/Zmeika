# FILE in which all the functions for working with text messages are stored.
import pygame

pygame.init()
from constants import *


def message(str, color, x, y):
    msg = font_style.render(str, True, color)
    dis.blit(msg, [x, y])


def score_write(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])  # - отображение счета.
