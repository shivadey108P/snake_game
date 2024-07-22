from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  # Removed self from super().__init__(self)
        self.color('white')
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.speed('fastest')   
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write('Game Over', align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()