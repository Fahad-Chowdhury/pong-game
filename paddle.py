from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.paddle = None
        self._create_paddle()

    def _create_paddle(self):
        """ Create a paddle of size 20 X 100, white color and in the given position. """
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(self.position)

    def go_up(self):
        """ Move paddle up by 20 co-ordinates. """
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """ Move paddle down by 20 co-ordinates. """
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
