import random
from turtle import Turtle, Screen

def create_turtles(colors):
    turtles = []
    i = 0
    for color in colors:
        obj = Turtle("turtle")
        turtles.append(obj)
        obj.color(color)
        obj.pu()
        obj.goto(x=-230, y=-100 + i*40)
        i += 1

    return turtles

def begin_game():
    screen = Screen()
    screen.setup(width=500,height=400)
    colors = ["red","orange","yellow","green","blue","purple"]

    user_bet = screen.textinput(title="Make your bet",prompt="Which turtle do you think is going to win?:\n"
                                                             "  - Red\n  - Orange\n  - Yellow\n  - Green\n"
                                                             "  - Blue\n  - Purple")

    if user_bet.lower() in colors:
        is_race_on = True
    else:
        print("Not a valid input.")
        screen.bye()
        is_race_on = False

    turtles = create_turtles(colors)

    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print("You've won!")
                else:
                    print("You lost!")
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

    screen.exitonclick()

begin_game()
