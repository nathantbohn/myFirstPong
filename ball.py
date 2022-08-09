#for the ball class
from turtle import Turtle


class Ball(Turtle):
    

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = .1
    
    def move(self):
        #x_move = 10
        #y_move = 10
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        #if self.ycor() > 285 or self.ycor() < -300:
            #bounce 
        self.y_move *= -1

    def bounce_x(self):
        #if self.xcor() >350 or self.xcor() < -360:
        self.x_move *= -1
        self.move_speed *= .9

    def reset_position(self):
        #resets the ball when it misses the paddles
        self.goto(0,0)
        self.bounce_x()
    
    def increase_speed(self):
        self.x_move *- 1.05
        self.y_move *= 1.05

        

        

        