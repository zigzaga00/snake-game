from food import Food
from scoreboard import ScoreBoard
from snake import Snake
from time import sleep
from turtle import Screen

# set up the screen object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake on a Screen!")
screen.tracer(0) # 0 switches tracer() off

# create the snake
snake = Snake(10) # int arg determines the starting speed

# create the food
food = Food()

# create the scoreboard
scoreboard = ScoreBoard()

# create event listeners to detect changes in direction
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# move the snake
game_on = True
while game_on:
    sleep(0.025)
    screen.update() # updates the screen after moves - screen.tracer() must be off
    snake.move()

    # detect collisions with food objects
    if snake.head.distance(food) < 20:
        food.move_food()
        scoreboard.increase_score(snake, 1)
        snake.extend_snake(10)
        snake.increase_speed()
    
    # detect collisions with tail
    for seg in snake.segs[1:]: # slices out index 0 which is snake.head
        if snake.head.distance(seg) < 3:
            game_on = False
            scoreboard.game_over()
    
    # detect collisions with walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_on = False

screen.exitonclick()
