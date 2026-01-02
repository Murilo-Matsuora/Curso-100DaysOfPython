import turtle as t
import time
from snake import Snake, PIXEL_SIZE
from food import  Food
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor("DarkOliveGreen")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.right, key="d")

game_over = False
speed = 0.2
while not game_over:
    screen.update()
    time.sleep(speed)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < PIXEL_SIZE / 2:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()

        if speed > 0.05:
            speed -= 0.02

    # Detect collision with wall
    if abs(snake.head.xcor()) >= 300 or abs(snake.head.ycor()) >= 300:
        scoreboard.game_over()
        game_over = True

    # Detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < PIXEL_SIZE / 2:
            scoreboard.game_over()
            game_over = True

screen.exitonclick()
