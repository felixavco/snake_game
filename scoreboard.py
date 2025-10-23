from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.print_scoreboard()

    def print_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)

    def increase_scoreboard(self):
        self.score += 10
        self.clear()
        self.print_scoreboard()

class PauseBoard(Turtle):
    def __init__(self):
        super().__init__()
        self._is_paused = False
        self.penup()
        self.hideturtle()
        self.color("green")
        self.goto(x=0, y=200)

    def print_pause(self):
        self.write('PAUSED', align=ALIGNMENT, font=FONT)

    def pause_game(self):
        self._is_paused = not self._is_paused

    def get_is_paused(self):
        return self._is_paused


