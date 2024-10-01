import random

from flask import Flask, render_template

app = Flask(__name__)

class Game():
    def __init__(self):
        self.options = ['Rock', 'Paper', 'Scissors', 'PickaxePikachu']
        self.playerChoice = None
        self.computerChoice = None
        self.wins = 0
        self.losses = 0
        self.avg = 0

    def setPlayerChoice(self, choice):
        self.playerChoice = choice + '.jpeg'

    def setComputerChoice(self, ):
        self.computerChoice = random.choice(self.options)

    def determineWinner(self):
        if self.playerChoice == self.computerChoice:
            return "It's a tie!"

        winner = {
            'Rock': ['Scissors'],
            'Paper': ['Rock'],
            'Scissors': ['Paper', 'PickaxePikachu'],
            'PickaxePikachu': ['Rock', 'Scissors'],
        }

        if self.computerChoice in winner[self.playerChoice]:
            self.wins += 1
            return winner[self.playerChoice] + " is the winner!"
        else:
            self.losses += 1
            return winner[self.computerChoice] + " is the winner!"

game = Game()

@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html')

if __name__ == '__main__':
    app.run()
