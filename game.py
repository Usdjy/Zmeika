from obj import Food, Snake
from constants import *

pygame.init()


def gameon():
    "function, which launches the gameplay."
    game_over = False

    snake = Snake()
    food = Food()

    while not game_over:

        while not snake.alive:
            dis.fill(blue)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        snake.alive = True
                    if event.key == pygame.K_c:
                        gameon()

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

        pygame.display.update()

        if food.check_life(snake.Head[0], snake.Head[1]):
            snake.len += 1
            food = Food()

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameon()
