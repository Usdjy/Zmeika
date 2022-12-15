from obj import Food, Snake, buttons
from constants import *
from text import *

pygame.init()
def getrocks(level):


def menu():
    "function responsible for the menu stage."
    menu_closed = False
    level = 0
    while not menu_closed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_closed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu_closed = True
                    gameon(level)
                if event.key == pygame.K_DOWN and level < len(buttons) - 1:
                    level += 1
                    buttons[level].chosen = True
                    buttons[level - 1].chosen = False
                if event.key == pygame.K_UP and level > 0:
                    level -= 1
                    buttons[level].chosen = True
                    buttons[level + 1].chosen = False
        dis.fill(blue)
        for b in buttons:
            b.draw()
        pygame.display.update()


def gameon(level):
    "function, which launches the gameplay."
    game_over = False

    snake = Snake()
    food = Food()

    while not game_over:

        while not snake.alive:
            dis.fill(blue)
            message("You lost, your score is " + str(snake.len - 1) + ", type C to restart, ""Q to quit", black)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        snake.alive = True
                        menu()
                    if event.key == pygame.K_c:
                        gameon(level)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            snake.turn(event)
        snake.check_border()
        snake.check_suicide()
        dis.fill(blue)
        snake.evolve()
        food.draw()
        snake.draw()
        score_write(snake.len - 1)
        pygame.display.update()

        if food.check_life(snake.Head[0], snake.Head[1]):
            snake.len += 1
            food = Food()

        clock.tick(snake_speed)

    pygame.quit()
    quit()


menu()
# gameon()
