import random


class Game:
    def __init__(self):
        self.options = ['Rock', 'Paper', 'Scissors', 'PickaxePikachu']
        self.player_choice = str
        self.computer_choice = str
        self.wins = 0
        self.losses = 0
        self.avg = 0
        self.decision = str

    def set_player_choice(self, choice):
        self.player_choice = choice

    def set_computer_choice(self):
        self.computer_choice = random.choice(self.options)

    def determine_winner(self):
        winner = {
            'Rock': ['Scissors'],
            'Paper': ['Rock'],
            'Scissors': ['Paper', 'PikachuPickaxe'],
            'PikachuPickaxe': ['Rock', 'Scissors'],
        }

        if self.computer_choice in winner[self.player_choice]:
            self.wins += 1
            self.decision = f"{self.player_choice} is the winner!"
        elif self.player_choice == self.computer_choice:
            self.decision = "It's a tie!"
        else:
            self.losses += 1
            self.decision = f"{self.computer_choice} is the winner!"
