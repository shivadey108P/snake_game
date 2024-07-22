from turtle import Screen
import time
from snake import Snake
from message_box import Pop_up

screen = Screen()
pop = Pop_up()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('Snaky Sneaky')
pop.open_pop_up('Welcome to snake game', 'Use arrow keys to move the snake')
screen.tracer(0)

snake = Snake()

game_on =  True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()