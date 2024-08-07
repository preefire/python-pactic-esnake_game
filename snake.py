from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
TURN_DEGREE = 90
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        # we can put the below lines here in this init function or put them in a new function too
        # for snake_index in range(3):
        #     self.segments.append(Turtle("square"))
        #     self.segments[snake_index].penup()
        #     self.segments[snake_index].color("pink")
        #     self.segments[snake_index].goto(START_POSITIONS[snake_index])

    def create_snake(self):
        for snake_index in range(3):
            self.segments.append(Turtle("square"))
            self.segments[snake_index].penup()
            self.segments[snake_index].color("pink")
            self.segments[snake_index].goto(START_POSITIONS[snake_index])


    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
    def extend(self):
        direction=self.segments[-1].heading()
        x = self.segments[-1].xcor()
        y = self.segments[-1].ycor()
        self.segments.append(Turtle("square"))

        self.segments[-1].penup()
        self.segments[-1].color("pink")
        self.segments[-1].setheading(direction)
        # if direction == 0:
        #     self.segments[-1].goto(x-20,y)
        # if direction == 180:
        #     self.segments[-1].goto(x-20,y)
        # if direction == 90:
        #     self.segments[-1].goto(x,y-20)
        # if direction == 270:
        #     self.segments[-1].goto(x,y+20)
        self.segments[-1].goto(x,y)



    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].fd(MOVE_DISTANCE)

    def left(self):
        direction = self.segments[0].heading()
        # new_direction = (direction+90)%360
        # self.segments[0].setheading(new_direction)
        if direction == 90:
            self.segments[0].lt(TURN_DEGREE)
        elif direction == 270:
            self.segments[0].rt(TURN_DEGREE)

    def right(self):
        direction = self.segments[0].heading()
        # new_direction = (direction-90)%360
        # self.segments[0].setheading(new_direction)
        if direction == 90:
            self.segments[0].rt(TURN_DEGREE)
        elif direction == 270:
            self.segments[0].lt(TURN_DEGREE)
    def up(self):
        direction = self.segments[0].heading()
        if direction == 0:
            self.segments[0].left(TURN_DEGREE)
        elif direction == 180:
            self.segments[0].right(TURN_DEGREE)

    def down(self):
        direction = self.segments[0].heading()
        if direction == 0:
            self.segments[0].right(TURN_DEGREE)
        elif direction == 180:
            self.segments[0].left(TURN_DEGREE)






