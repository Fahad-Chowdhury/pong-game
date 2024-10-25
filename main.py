from pong_screen import PongScreen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard


def map_paddle_moves(right_paddle: Paddle, left_paddle: Paddle, screen: PongScreen):
    """ Map keystrokes that listened by the PongScreen class to the methods in
    right and left paddle. Map "Up" key to move up and "Down" key to move down
    the right paddle. Map  "w" key to move up and "s" key to move down the left
    paddle."""
    keystrokes = {
        "Up": right_paddle.go_up,
        "Down": right_paddle.go_down,
        "w": left_paddle.go_up,
        "s": left_paddle.go_down,
    }
    for key, fun in keystrokes.items():
        screen.listen_to_keys(key, fun)


def ball_touches_padel(ball: Ball, right_paddle: Paddle, left_paddle: Paddle):
    """ Check if ball touches or collides with left or right padel. Return True
    if ball touches any padel, else return False. """
    touch_right = ball.distance(right_paddle) < 50 and ball.xcor() > 320
    touch_left = ball.distance(left_paddle) < 50 and ball.xcor() < -320
    return touch_left or touch_right


def player_misses_ball(ball: Ball, score_board: ScoreBoard):
    """ Check if any of the player missed the ball, update the score and return
    True if ball is missed, else return False. """
    if ball.xcor() > 380:
        score_board.increase_left_score()
        return True
    elif  ball.xcor() < -380:
        score_board.increase_right_score()
        return True
    return False


def main():
    """ Main method for the Pong game.  """
    game_is_on = True
    screen = PongScreen()
    # Create right and left paddle
    right_paddle = Paddle((350, 0))
    left_paddle = Paddle((-350, 0))
    # Map right and left paddle moves to keyboard strokes
    map_paddle_moves(right_paddle, left_paddle, screen)
    ball = Ball()
    score_board = ScoreBoard()

    while game_is_on:
        screen.update_screen()
        ball.move()
        # Check for collision with the wall (y coordinates -280 to 280).
        if abs(ball.ycor()) > 280:
            ball.bounce_y()
        # Check if ball touches any paddle
        if ball_touches_padel(ball=ball, right_paddle=right_paddle,
                              left_paddle=left_paddle):
            ball.bounce_x()
        # If any player misses the ball, refresh the ball.
        if player_misses_ball(ball=ball, score_board=score_board):
            ball.refresh()
        # End game when a player reaches a score of 11
        if score_board.left_score > 10 or score_board.right_score > 10:
            score_board.display_game_over()
            game_is_on = False

    screen.exit_screen_on_click()


if __name__ == "__main__":
    main()
