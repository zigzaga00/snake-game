from time import sleep
from turtle import Screen, Turtle

# set starting positions as a class attribute
# every snake instantiated from this class
# will have the same starting coordinates
START_POS = [(0, 0), (-20, 0), (-40, 0)]

# set heading directions as class attributes
# to help avoid confusion
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180

class Snake:
    def __init__(self, speed):
        self.speed = speed
        self.segs = []
        self._create_snake()
        self.head = self.segs[0]

    def _add_segment(self, pos):
        seg = Turtle(shape="square")
        seg.color("white")
        seg.penup()
        seg.goto(pos)
        self.segs.append(seg)

    def _create_snake(self):
        """creates a snake using turtle objects"""
        for pos in START_POS:
            self._add_segment(pos)
    
    def extend_snake(self, num):
        """adds segments to the snake"""
        for i in range(num):
            self._add_segment(self.segs[-1].position())
    
    def increase_speed(self):
        self.speed += 1

    def move(self):
        """moves the snake segments"""
        for i in range(len(self.segs)-1, 0, -1): # snake segs chase each other
            new_x = self.segs[i-1].xcor()
            new_y = self.segs[i-1].ycor()
            self.segs[i].goto(new_x, new_y)
        self.head.fd(self.speed) # head seg moves outside loop - fd() arg determines speed
    
    # methods to control changes in direction
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
