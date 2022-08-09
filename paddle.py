#The Class for my pong paddle, to hit the ball back toward the opposing side. 
from turtle import Turtle

class Paddle(Turtle):

    magenta = (199,36,177)

    def __init__(self,position):
       super().__init__()    
        
        #paddle.hideturtle()
        #outline.hideturtle()
       self.shape("square")
       self.color("magenta")
       #self.shape("square")
       #self.color("white")
       self.shapesize(stretch_wid=5.2,stretch_len=1.2)
       self.shapesize(stretch_wid=5,stretch_len=1)
       self.penup()
       self.goto(position)


    
    def go_up(self):
        new_y = self.ycor() + 20
        if self.ycor() < 240:
            self.goto(self.xcor(),new_y)
            self.goto(self.xcor(),new_y)
    
    def go_down(self):
        new_y = self.ycor() - 20
        if self.ycor() > -240:
            self.goto(self.xcor(),new_y)
            self.goto(self.xcor(),new_y)


    
    

