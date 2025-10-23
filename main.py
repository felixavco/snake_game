from turtle import Screen

from scoreboard import Scoreboard, PauseBoard
from snake import Snake
from food import Food
import time

pause = PauseBoard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

game_is_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(pause.pause_game, "space")

while game_is_on:
    screen.update()
    time.sleep(0.1)

    if pause.get_is_paused():
        pause.print_pause()
    else:
        pause.clear()
        snake.move()

    def set_game_over():
        global  game_is_on
        game_is_on = False
        scoreboard.game_over()

    #detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_scoreboard()
        snake.extend()

    #detect collision with wall
    xcor = snake.head.xcor()
    ycor = snake.head.ycor()
    if xcor > 280 or xcor < -280 or ycor > 280 or ycor < -280:
        set_game_over()

    #detect collision with any segment in the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            set_game_over()



screen.exitonclick()
