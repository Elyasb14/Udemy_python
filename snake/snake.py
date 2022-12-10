from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# make a class Snake
class Snake:
    # initialize attributes
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[len(self.segments) - 1]

    # creates a snake object that is three 20x20 squares in length
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
            
    # method to add a segment to end of snake object
    def add_segment(self):
        new_segment = Turtle
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto((self.segments[len(self.segments) - 1].xcor(), self.segments[len(self.segments) - 1].ycor()))
        self.segments.append(new_segment)
        
    # method to move snake forward 
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
    # method to move snake up 
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            
    # method to move snake down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            
    # method to move snake to left
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            
    # method to move snake right
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
