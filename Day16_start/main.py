# import turtle
#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkGreen", "LightGreen")
# timmy.pensize(50)
# for i in range(1, 73):
#     timmy.forward(5)
#     timmy.circle(10,5)
#
# screen = Screen()
# print(screen.canvheight)
# screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])
table.align = "l"
# table.attributes("Alignment","CenterAligned")
print(table)
