class Player:
    """
    player attribute: name, score, gamble
    Gamble keeps this history of the scores
    """

    def __init__(self):
        self.score = 0
        self.name = input("Entrez le nom du joueur:")
        # FIXME : lock the access to only the 10 values rounds[1 -> 10]
        self.gamble = [None for i in range(1, 12)]

    def set_gamble(self, round):
        try:
            gamble = int(input(f"Player {self.name}: "))
            if gamble < 0:
                raise ValueError("Enter a postive number")
            self.gamble[round] = gamble
        except ValueError as exp:
            if exp.args[0].__contains__('invalid literal for int() with base 10:'):
                print("Only the numbers are accepted")
            else:
                print(exp.args[0])
            self.set_gamble(round)

    def set_score(self):
        try:
            score = int(input(f"Entrez score du joueur {self.name}: "))
            self.score += score
        except ValueError as exp:
            if exp.args[0].__contains__('invalid literal for int() with base 10:'):
                print("Only the numbers are accepted")
            else:
                print(exp.args[0])
            self.set_score()


def player_creation():
    """
    Create the list of the players
    :return: a list of Player's object
    """
    player_list_creation = True
    players = []
    while player_list_creation:
        players.append(Player())
        if int(input("Entrez 0 pour terminer la saise des joueurs, 1 pour continuer")) == 0:
            player_list_creation = False
        else:
            player_list_creation = True
    return players


def main():
    # Game start : create player
    players = player_creation()

    for round in range(1, 3):
        # Start gambling
        # FIXME the android app won't use a loop but a clic button
        print(f"Round {round}", "Gambling !!!")
        for player in players: player.set_gamble(round)

        # Scoring
        for player in players:
            player.set_score()

    for player in players:
        print(f"fin de partie, score : \n {player.name} : {player.score}")


if __name__ == '__main__':
    main()
