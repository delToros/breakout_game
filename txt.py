from turtle import Turtle

FONT = ('Small Fonts', 25, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('#303B39')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-230, 400)
        self.write(f'Score: {self.score}', align='left', font=FONT)

    def update_score(self):
        self.score += 5
        self.clear()
        self.goto(-230, 400)
        self.write(f'Score: {self.score}', align='left', font=FONT)


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color('#303B39')
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(0, 400)
        self.write(f'{self.level}', align='left', font=FONT)

    def update_level(self):
        self.level += 1
        self.clear()
        self.goto(0, 400)
        self.write(f'{self.level}', align='left', font=FONT)

class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color('#303B39')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-125, 0)
        self.write('Game over', align='left', font=('Small Fonts', 50, 'normal'))