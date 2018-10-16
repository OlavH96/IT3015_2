from NIM import *
import random
from StateManager import *
from MCTS import *
if __name__ == '__main__':

    N = 3
    K = 2
    stateman = StateManager()
    game = stateman.generate_initial_state([N, K])
    print("Valid moves")
    print(game.getValidMoves())
    print(game)

    for g in stateman.generate_child_states(game):
        print(g)


    mcts = MCTS(stateman)
    mcts.generate_tree(game)
    pass
    exit(1)
    while not game.isDone():

        player_1 = game.getValidMoves()[random.randint(0, len(game.getValidMoves()) - 1)]

        game.take(player_1)
        print("Player 1 took", player_1)
        print(game)
        if game.isDone():
            print("Player 1 won")
            break
        player_2 = game.getValidMoves()[random.randint(0, len(game.getValidMoves()) - 1)]
        game.take(player_2)
        print("Player 2 took", player_2)
        print(game)
        if game.isDone():
            print("Player 2 won")
            break
