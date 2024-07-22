from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('Snaky Sneaky')

segments = []

for i in range(3):
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(-20 * i, 0)
    segments.append(new_segment)

game_on =  True

while





screen.exitonclick()