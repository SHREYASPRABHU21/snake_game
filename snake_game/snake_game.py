from turtle import *
import time
from Snake import *
from Food import *
from scoreboard import *
screen = Screen()
snake = Snake()
score = Scoreboard()
#
# ex = Turtle()
# ex.shape("square")
# ex.color("blue")

screen.setup(width=500,height= 500)

screen.bgcolor("black")
screen.title("Snake_Game")
screen.tracer(0)
screen.listen()

food = Food()

screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake_segments[0].distance(food) < 15:
        food.refresh()
        score.update()
        snake.extend()

    if snake.snake_segments[0].xcor() > 240 or snake.snake_segments[0].xcor() <-240 or snake.snake_segments[0].ycor() > 240 or snake.snake_segments[0].ycor() < -240:
        score.game_over()
        game_is_on = False

    for segment in snake.snake_segments[1:]:
        if segment.distance(snake.snake_segments[0]) < 10 :
            game_is_on = False
            score.game_over()


screen.exitonclick()