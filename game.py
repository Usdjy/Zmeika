from obj import Food, Snake, buttons, Rock
from constants import *
from text import *
from maps import maps

pygame.init()


def getrocks(level):
    rocks = list()
    for i in range(0, dis_height // snake_block):
        for j in range(0, dis_width // snake_block):
            if maps[level][i][j] == 1:
                rocks.append(Rock(j * 10, i * 10))
    return rocks


def menu():
    "function responsible for the menu stage."
    buttons[0].chosen = True
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
    rocks = getrocks(level)
    snake = Snake()
    food = Food(maps[level])

    while not game_over:

        while not snake.alive:
            dis.fill(blue)
            message("You lost, your score is " + str(snake.len - 1) + ", type C to restart, ""Q to quit", black, dis_width / 40, dis_height / 3)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        snake.alive = True
                        buttons[level].chosen = False
                        menu()
                    if event.key == pygame.K_c:
                        gameon(level)
                if event.type == pygame.QUIT:
                    game_over = True
                    snake.alive = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            snake.turn(event)
        snake.check_border()
        snake.check_suicide()
        snake.check_rocks(rocks)
        dis.fill(blue)
        snake.evolve()
        food.draw()
        snake.draw()
        score_write(snake.len - 1)
        for rock in rocks:
            rock.draw()
        pygame.display.update()

        if food.check_life(snake.Head[0], snake.Head[1]):
            snake.len += 1
            food = Food(maps[level])

        clock.tick(snake_speed)

    pygame.quit()
    quit()


menu()
# gameon()
