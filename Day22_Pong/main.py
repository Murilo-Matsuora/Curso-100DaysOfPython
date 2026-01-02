from turtle import Screen
from background import Background
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.tracer(0)

background = Background()

l_paddle = Paddle((-350, 0))
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")

r_paddle = Paddle((350, 0))
screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")

ball = Ball()
left_was_hit_last = True

scoreboard = Scoreboard()

max_points = screen.numinput(title="Select maximum of points", prompt="Choose the amount of points to win the game", minval=0)
screen.listen()
screen.tracer(0)

game_over = False
while not game_over:
    time.sleep(0.01)
    screen.update()
    ball.move()

    if ball.ball.ycor() >= 278:
        ball.bounce()
    elif ball.ball.ycor() <= - 270:
        ball.bounce()

    if abs(ball.ball.xcor()) >= 330:

        # Detects collision with left paddle
        if l_paddle.paddle.ycor() - 50 <= ball.ball.ycor() <= l_paddle.paddle.ycor() + 50 and not left_was_hit_last:
            ball.hit()
            left_was_hit_last = True

        # Detects collision with left paddle
        elif r_paddle.paddle.ycor() - 50 <= ball.ball.ycor() <= r_paddle.paddle.ycor() + 50 and left_was_hit_last:
            ball.hit()
            left_was_hit_last = False

        # If no paddle hit the ball, it waits until the ball leaves the screen and resets
        elif abs(ball.ball.xcor()) > 360:
            # Keeps moving the ball until it's offscreen
            while abs(ball.ball.xcor()) <= 400:
                screen.update()
                ball.move()

                if ball.ball.ycor() >= 278:
                    ball.bounce()
                elif ball.ball.ycor() <= - 271:
                    ball.bounce()

            # Detects if ball was missed by the left paddle
            if ball.ball.xcor() < - 400:
                scoreboard.r_points += 1
                ball.set_random_direction()
                ball.reset_speed()
                ball.reset_position(1)
                left_was_hit_last = True
            # Detects if ball was missed by the left paddle
            if ball.ball.xcor() > 400:
                scoreboard.l_points += 1
                ball.set_random_direction()
                ball.reset_speed()
                ball.reset_position(-1)
                left_was_hit_last = False

            scoreboard.update_scoreboard()

            # Detects if either player won
            if scoreboard.l_points >= max_points:
                background.reset_background()
                background.print_win_message("Player 1 wins!")
                game_over = True
            elif scoreboard.r_points >= max_points:
                background.reset_background()
                background.print_win_message("Player 2 wins!")
                game_over = True
screen.exitonclick()
