from turtle import Turtle


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pensize(7)
        self.hideturtle()
        self.pencolor('#445451')
        self.goto(-246, -438)
        self.pendown()
        # Main border
        self.goto(-246, 446) # Left border | Top Left corner
        self.goto(238, 446) # Top border | Top right corner
        self.goto(238, -438) # Right border | bottom right corner
        self.goto(-246, -438) # Bottom border | bottom left corner
        # Score | Lifes border
        self.goto(-246, 400)
        # self.goto(0, 400)
        # self.goto(0, 446)
        # self.goto(0, 400)
        self.goto(246, 400)