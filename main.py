from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game ")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

play_on = True
while play_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    #Detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
        screen.update()

    #Detect collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        score.reset()
        snake.reset()
        #play_on = False

    #Detect collision with tail
    # for segment in snake.segments:
    #     if segment == snake.segments[0]:
    #         pass
    #     elif snake.segments[0].distance(segment) < 5:
    #         score.game_over()
    #         play_on = False
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            score.reset()
            snake.reset()
            #play_on = False
screen.exitonclick()

