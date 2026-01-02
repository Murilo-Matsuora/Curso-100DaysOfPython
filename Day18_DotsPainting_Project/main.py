import colorgram as cg
import turtle as t
import random

HEIGHT = 9
WIDTH = 12
SPACING = 50
DOT_SIZE = 21

def draw_point(color):
    tim.pd()
    tim.dot(DOT_SIZE, color)
    tim.pu()
    tim.forward(SPACING)


colors = cg.extract("./ZeldaLandscapeBeautifulPalette.jpg", 10)
t.colormode(255)
tim = t.Turtle()
tim.speed(0)
tim.hideturtle()
tim.teleport(- (WIDTH - 1) * SPACING / 2, HEIGHT * SPACING / 2)

for i in range(HEIGHT):
    for j in range(WIDTH):
        rand_color = random.choice(colors).rgb
        draw_point(rand_color)
    even = 1 if i % 2 == 0 else -1
    tim.right(90 * even)
    tim.pu()
    tim.forward(SPACING)
    tim.right(90 * even)
    tim.forward(SPACING)
    tim.pd()


screen = t.Screen()
screen.exitonclick()
