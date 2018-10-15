from NIM import *
import random

if __name__ == '__main__':


    print("NIM simulator")

    N = 100
    K = 40

    game = NIM(N, K)

    print(game.getValidMoves())
    print(game)

    while not game.isDone():

        player_1 = game.getValidMoves()[random.randint(0, len(game.getValidMoves())-1)]

        game.take(player_1)
        print("Player 1 took",player_1)
        print(game)
        if game.isDone():
            print("Player 1 won")
            break
        player_2 = game.getValidMoves()[random.randint(0, len(game.getValidMoves())-1)]
        game.take(player_2)
        print("Player 2 took",player_2)
        print(game)
        if game.isDone():
            print("Player 2 won")
            break

