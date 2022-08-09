#Here is my code for Pong. I want to make it look kind of vaperwave, and rather 1980s
from turtle import * 
import turtle 
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

#parameters for the pong game screen and window
pong_window = turtle.Screen()
pong_window.setup(width=800,height=600)
pong_window.bgcolor("black")
pong_window.title("Pong")
pong_window.tracer(0)

#create a paddle
left_paddle = Paddle((-350,0))

#create the other paddle
right_paddle = Paddle((350,0))

#create the ball
ball = Ball()


#create the scoreboard 
scoreboard = Scoreboard()

#listen for commands
pong_window.listen()
pong_window.onkey(left_paddle.go_up,"w")
pong_window.onkey(left_paddle.go_down,"s")
pong_window.onkey(right_paddle.go_up,"Up")
pong_window.onkey(right_paddle.go_down,"Down")



game_is_running = True




while game_is_running:
    time.sleep(ball.move_speed)
    pong_window.update()
    ball.move()


    #detect collision with the wall 
    if ball.ycor() > 280 or ball.ycor() < -280:
        #bounce 
        ball.bounce_y()
        #print("bounce")
    #if ball.xcor() > 360 or ball.xcor() < -360: 
       # ball.bounce_x()

    #detect collision with the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.increase_speed()
    
    #detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.r_point()
    #scoreboard.update_score()


turtle.done()

