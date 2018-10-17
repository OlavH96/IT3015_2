class Move:

    def __init__(self, parent, move, result, player):
        self.parent = parent
        self.move = move
        self.result = result
        self.player = player
        self.visits = 0
        self.reward = 0

    def __str__(self):
        return "Move: " + str(self.parent) + " -> " + str(self.move) + " -> " + str(self.result) +" by "+ str(self.player)
