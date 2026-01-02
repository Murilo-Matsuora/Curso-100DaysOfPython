import turtle
import pandas as pd

def draw_state_on_map(state):
    state_data = states_data[states_data["state"] == state]
    x = state_data["x"].item()
    y = state_data["y"].item()
    tim.goto(x, y)
    tim.write(arg=state, align="center", font=("Arial", 8, "normal"))

def generate_csv(states):
    missed_states = [state for state in all_states if state not in states]
    missed_states = states_data[states_data["state"].isin(missed_states)]["state"]
    missed_states.to_csv("states_missed.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

tim = turtle.Turtle()
tim.hideturtle()
tim.pu()

states_data = pd.read_csv("./50_states.csv")
all_states = states_data["state"].tolist()
guessed_states = []


guess_number = 0
while guess_number < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another State's name?").title()

    if answer_state == "Exit":
        generate_csv(guessed_states)
        tim.goto(0, 0)
        tim.color("black")
        tim.write(arg="Secret...\nshhh...", align="center", font=("Arial", 15, "bold"))
        game_over = True
        break

    if answer_state in guessed_states:
        print(f"State {answer_state} was already guessed!")
        continue

    guessed_states.append(answer_state)
    if answer_state in all_states:
        print("You got it!")
        draw_state_on_map(answer_state)
        guess_number += 1
    else:
        print("You lost!")
        tim.goto(0, 0)
        tim.color("red")
        tim.write(arg="GAME OVER\n:(", align="center", font=("Arial", 25, "bold"))
        game_over = True


if guess_number >= 50:
    print("You won!")
    tim.goto(0, 0)
    tim.color("LightGreen")
    tim.write(arg="YOU WIN!!!\n:D", align="center", font=("Arial", 30, "bold"))

screen.exitonclick()

