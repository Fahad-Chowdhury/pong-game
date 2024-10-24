from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(-10, 260)
        self.left_score = 0
        self.right_score = 0
        self._update_scoreboard()

    def _update_scoreboard(self):
        """ Update the scoreboard. """
        self.clear()
        msg = f"{self.left_score} : {self.right_score}"
        self.write(msg, move=False, align=ALIGNMENT, font=FONT)

    def display_game_over(self):
        """ Display game over message at the center of the screen. """
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def increase_left_score(self):
        """ Increase the score by 1 of left player. """
        self.left_score += 1
        self._update_scoreboard()

    def increase_right_score(self):
        """ Increase the score by 1 of right player. """
        self.right_score += 1
        self._update_scoreboard()
