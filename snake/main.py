from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food  = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True
while game_is_on:
    
    screen.update()
    time.sleep(.1)
    snake.move()
    score.write

    #detect snake collison
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.increase_score()

    #detect wall collison
    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() >= 290 or snake.head.ycor() <= -290:
        game_is_on = False
        score.game_over()


    #detect collison with tail
    for segment in snake.segments[1:]:
       if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
      
    
   
        
      
        
























screen.exitonclick()