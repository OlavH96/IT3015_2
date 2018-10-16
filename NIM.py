class NIM:

    def __init__(self, N, K):
        self.N = N  # Pieces on the board
        self.K = K  # max pieces you can take, you can take less, but not more.

    def take(self, number):

        if not self.isValidMove(number):
            return False

        self.N -= number
        return True

    def isValidMove(self, number):

        return number <= self.K and self.N - number >= 0

    def getValidMoves(self):

        if self.K > self.N - self.K:

            return list(range(1, self.N))

        return list(range(1, self.K+1))

    def isDone(self):

        return self.N <= 0

    def __str__(self):
        return "N="+str(self.N)+", K="+str(self.K)

    def __copy__(self):

        return NIM(self.N, self.K)