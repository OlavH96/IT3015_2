from Player import *
from NIM import *
import random
from StateManager import *
from MCTS import *
from Policy import *

if __name__ == '__main__':

    N = 100
    K = 20
    init_player = Player.PLAYER_1
    policy = Policy()

    stateman = StateManager()
    game = stateman.generate_initial_state([N, K], player=init_player)

    mcts = MCTS(stateman, [N, K, init_player])
    print(mcts.root)
    mcts.node_expansion(mcts.tree)

    print(mcts.rollout(State(mcts.root, init_player), policy))

    mcts.tree.print_entire_tree()

    exit(1)
    initial_state = State(game, Player.PLAYER_1)
    state = initial_state

    while not game.isDone():

        init_player = state.player
        choice = mcts.tree_search(state.game, policy)
        game.take(choice.move)
        print(choice)
        print(game)

        if game.isDone():
            print(state.player, "Won!")
            break
        other = Player.other(state.player)
        state = State(game, other)
