from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.ht()
        self.goto(x=0, y=260)
        self.color("white")
        self.write(f"Score = {self.score} High Score: {self.high_score}", align="center", font=("Arial", 15, "bold"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", align="center",font=("Arial",15,"bold"))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
                # we can use f-string to achive the above too file.write(f"{self.high_score}")
        self.score=0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(x=0, y=-230)
    #     self.write("Game Over", align="center", font=("Arial", 35, "bold"))

