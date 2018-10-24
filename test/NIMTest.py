from NIM import *
from Player import *
import random

if __name__ == '__main__':

    N = 100
    K = 20
    initial_player = Player.PLAYER_1

    game = NIM(N, K, initial_player)

    while not game.isDone():
        moves = game.getValidMoves()
        rand_choice = moves[random.randint(0, len(moves) - 1)]
        game.take(rand_choice)

    print("Winner is", game.winner)
