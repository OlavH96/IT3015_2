from Move import *
from Player import *
class NIM:

    def __init__(self, N, K, player):
        self.player = player
        self.N = N  # Pieces on the board
        self.K = K  # max pieces you can take, you can take less, but not more.
        self.visits = 0
        self.history = []
        self.winner = None

    def take(self, number):

        if not self.isValidMove(number):
            raise Exception("Invalid move", number, "for game", self)

        before = self.__copy__()
        self.N -= number
        after = self.__copy__()

        self.history.append(Move(before, number, after, self.player))
        if self.isDone():
            self.winner = self.player
        self.player = Player.other(self.player)

        return self

    def isValidMove(self, number):

        return number <= self.K and self.N - number >= 0

    def getValidMoves(self):

        if self.K > self.N:
            return list(range(1, self.N + 1))

        return list(range(1, self.K + 1))

    def isDone(self):

        return self.N <= 0

    def __str__(self):
        return "N=" + str(self.N) + ", K=" + str(self.K)

    def __copy__(self):

        return NIM(self.N, self.K, self.player)

    def __eq__(self, other):

        return self.K == other.K and self.N == other.N and self.player == other.player
