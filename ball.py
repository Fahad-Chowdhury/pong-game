from turtle import Turtle
import time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.05

    def move(self):
        """ Move the ball diagonally, by changing the value of x and y coordinates
        of the ball. """
        time.sleep(self.ball_speed)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        """ Reverse the horizontal direction of the ball by reversing the x_move value.
        If the ball was moving right, change the direction to left, and vice versa. 
        Also, increase the ball speed each time. """
        self.x_move *= -1
        self.ball_speed *= 0.8

    def bounce_y(self):
        """ Reverse the vertical direction of the ball by reversing the y_move value.
        If the ball was moving up, change the direction to down, and vice versa. """
        self.y_move *= -1

    def refresh(self):
        """ Reset the ball position to center, reset the ball speed and change the
        horizontal direction of the ball, so that the other player has a chance to play.
        """
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()
