from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over - Snakey Endsu!!!", align=ALIGNMENT, font=FONT)

    def increase_score(self, snake, increase):
        """increases the score by the given integer and the speed of the given snake object"""
        self.score += increase
        self.update_scoreboard()

    def update_scoreboard(self):
        """clears and updates the scoreboard"""
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    