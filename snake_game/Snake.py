from turtle import *

UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270



snake_cor = [(20, 0), (0, 0), (-20, 0)]


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.createSnake()

    def createSnake(self):
        for cor in snake_cor:
            self.addsegment(cor)

    def addsegment(self,cor):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(cor)
        self.snake_segments.append(snake)
    def move(self):
        for cor in range(len(self.snake_segments) - 1, 0, -1):
            self.snake_segments[cor].goto((self.snake_segments[cor - 1].xcor()), (self.snake_segments[cor - 1].ycor()))
        self.snake_segments[0].forward(20)

    def up(self):
        if self.snake_segments[0].heading() != DOWN:
            self.snake_segments[0].setheading(UP)


    def down(self):
        if self.snake_segments[0].heading() != UP:
            self.snake_segments[0].setheading(DOWN)

    def left(self):
        if self.snake_segments[0].heading() != RIGHT:
            self.snake_segments[0].setheading(LEFT)

    def right(self):
        if self.snake_segments[0].heading() != LEFT:
            self.snake_segments[0].setheading(RIGHT)

    def extend(self):
        self.addsegment(self.snake_segments[-1].position())