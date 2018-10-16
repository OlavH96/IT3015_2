class Move:

    def __init__(self, parent, move, result):
        self.parent = parent
        self.move = move
        self.result = result

    def __str__(self):
        return "Move: " + str(self.parent) + " -> " + str(self.move) + " -> " + str(self.result)
