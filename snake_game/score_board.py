from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 25, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__() # if use score = Turtle here cant have attribute score, therefore need to inherit from turtle
        self.score = 0
        # self.high_score = 0  # keep track of high scores
        # now use a txt file to keep track of the high score
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.penup()
        # self.goto(0, 270) # have to move the turtle before write
        self.color('white')
        self.hideturtle()
        self.update_scoreboard()
        # self.write(f'Score = {self.score} Highest Score = {self.high_score}', align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f'Score = {self.score} Highest Score = {self.high_score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align=ALIGNMENT, font=FONT)

    def reset_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

