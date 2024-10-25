from turtle import Screen

class PongScreen:

    def __init__(self):
        self.screen = Screen()
        self._setup_screen()

    def _setup_screen(self):
        """ Setup screen. """
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Pong")
        self.screen.tracer(0)
        self.screen.listen()

    def update_screen(self):
        """ Update the screen. """
        self.screen.update()

    def listen_to_keys(self, key, fun):
        """ Map keyboard stroke to snake move. """
        self.screen.onkey(key=key, fun=fun)

    def exit_screen_on_click(self):
        """ Close screen on mouseclick. """
        self.screen.exitonclick()
