class State:

    def __init__(self, game, player):
        self.game = game.__copy__()
        self.player = player

    def is_winning(self):
        return self.game.isDone()


def of(game, player):
    return State(game, player)
