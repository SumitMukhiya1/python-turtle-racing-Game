from turtle import Turtle, Screen
import random

colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "gray", "brown", "cyan"]
positions = [-225, -175, -125, -75, -25, 25, 75, 125, 175, 225]
all_turtles = []
is_game_over = False

screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor("black")
users_bet = screen.textinput(title="Which Color Of Turtle Wins The Game?", prompt="Type a color: ")


tim = Turtle()

for turtle in range(10):
    tim = Turtle("turtle")
    tim.color(colors[turtle])
    tim.penup()
    tim.goto(x=-290, y=positions[turtle])
    tim.pendown()
    all_turtles.append(tim)


if users_bet:
    is_game_over = False

while not is_game_over:
    for turtle in all_turtles:
        random_move = random.randint(0, 10)
        turtle.penup()
        turtle.forward(random_move)

        if turtle.xcor() > 290:
            winner_color = turtle.pencolor().lower()
            print(f"The winner Turtle Is: {winner_color}")

            if users_bet.lower() == winner_color:
                print("You Win!")
            else:
                print("You Lose!")

            is_game_over = True
