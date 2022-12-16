from obj import Food, Snake, buttons, Rock
from constants import *
from text import *
from maps import maps

pygame.init()


def getrocks(level):
    # The following function gets the list of rocks on the map from maps.py each level.
    # Arguments:
    #           level (int) - number of the chosen level.
    # Return value: rock - list of class Rock objects.
    rocks = list()
    for i in range(0, dis_height // snake_block):
        for j in range(0, dis_width // snake_block):
            if maps[level][i][j] == 1:
                rocks.append(Rock(j * 10, i * 10))
    return rocks


def menu():
    # The following function is responsible for the menu page.
    #
    buttons[0].chosen = True
    menu_closed = False
    level = 0
    while not menu_closed:  # This loop is responsible for scrolling between the buttons
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


def draw_stuff(snake, food, rocks):
    # The following function is responsible for drawing the objects
    # Arguments:     snake(class Snake) - the Snake
    #               food(class Food) - the Food
    #               rocks(class Rock) - the list of rocks
    dis.fill(blue)
    food.draw()
    snake.draw()
    score_write(snake.len - 1)
    for rock in rocks:
        rock.draw()
    pygame.display.update()


def gameon(level):
    # The following function is responsible for the gameplay
    # Arguments: level(int) - the chosen level
    game_over = False
    rocks = getrocks(level)
    snake = Snake()
    snake.speed += 5 * level
    food = Food(maps[level])

    while not game_over:

        while not snake.alive:  # The stage after the snake has died.
            dis.fill(blue)
            message("You lost, your score is " + str(snake.len - 1) + ", type C to restart, ""Q to quit", black,
                    dis_width / 40, dis_height / 3)
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

        for event in pygame.event.get():  # The gameplay when the game is going on
            if event.type == pygame.QUIT:
                game_over = True
            snake.turn(event)
        snake.evolve(rocks)  # Processes that happen to a snake every quantum of time
        draw_stuff(snake, food, rocks)

        if food.check_life(snake.Head[0], snake.Head[1]):  # Checks if the snake has got the food
            snake.len += 1
            snake.speed += 1
            food = Food(maps[level])

        clock.tick(snake.speed)

    pygame.quit()
    quit()


menu()
