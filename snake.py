from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake() # create snake when create a snake object
        self.head = self.segments[0] # have a head attribute to simply the code
        # head has to be after self.create_snake() because segments is empty before self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position) # move the code here to add_segment because we'r gonna need add_segment later on

    def add_segment(self, position): # create a method that can be reused
        new_turtle = Turtle(shape='square')
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)
        # print(turtle_1.shapesize())
        new_turtle.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=0.5)
        # turtle_1.penup()

    def extend(self):
        self.add_segment(self.segments[-1].position())
        # add one more segment at the end of snake (last segment of snake)

    def reset_snake(self):
        for segment in self.segments:
            segment.clear()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def forward(self):
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].goto(self.segments[i-1].xcor(), self.segments[i-1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # when snake is moving down , it can not go up
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)


