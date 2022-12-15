from obj import Food, Snake
from constants import *

pygame.init()


def message(str, color):
   msg = font_style.render(str, True, color)
   dis.blit(msg, [dis_width/40, dis_height / 3])


def score_write(score):
   value = score_font.render("Your Score: " + str(score), True, yellow)
   dis.blit(value, [0, 0]) #- отображение счета.


def gameon():
    "function, which launches the gameplay."
    game_over = False


    snake = Snake()
    food = Food()

    while not game_over:

        while not snake.alive:
            dis.fill(blue)
            message("You lost, your score is " + str(snake.len -1) + ", type C to restart, ""Q to quit", black)
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
        score_write(snake.len - 1)
        pygame.display.update()

        if food.check_life(snake.Head[0], snake.Head[1]):
            snake.len += 1
            food = Food()

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameon()
