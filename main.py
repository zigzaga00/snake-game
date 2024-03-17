from snake import Snake
from time import sleep
from turtle import Screen, Turtle

# set up the screen object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake on a Screen!")
screen.tracer(0) # 0 switches tracer() off

# create the snake
snake = Snake(5) # int arg determines the starting speed

# create event listeners to detect changes in direction
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# move the snake
game_on = True
while game_on:
    sleep(0.1)
    screen.update() # updates the screen after moves - screen.tracer() must be off
    snake.move()

screen.exitonclick()