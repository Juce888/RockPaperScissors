import random

from flask import Flask, render_template, request, session

from models.Game import Game

app = Flask(__name__)
app.secret_key = "Secret"

gaming = Game()

@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/result')
def result():
    choice = request.args.get('id')

    gaming.set_player_choice(choice)
    gaming.set_computer_choice()
    gaming.determine_winner()

    session['win'] = gaming.wins
    session['loss'] = gaming.losses
    session['decision'] = gaming.decision

    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
