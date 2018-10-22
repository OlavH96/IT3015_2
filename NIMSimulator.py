from Player import *
from NIM import *
import random
from StateManager import *
from MCTS import *
from Policy import *

if __name__ == '__main__':

    N = 5
    K = 2
    init_player = Player.PLAYER_1
    policy = Policy(init_player)

    stateman = StateManager()
    game = stateman.generate_initial_state([N, K], player=init_player)

    mcts = MCTS(stateman, game)
    # print(mcts.evaluate_state(mcts.tree))
    mcts.node_expansion(mcts.tree)
    mcts.tree.print_entire_tree()
    start = mcts.tree
    state = start
    game = start.content.__copy__()

    print("start", start)
    print("state", state)
    print("game", game)

    while not game.isDone():

        choice = mcts.tree_search(game.__copy__(), policy)
        print("choice is",choice)
        print(game)
        game.take(choice.move)  # take real move
        print(game)

        if game.isDone():
            print(state.content.player, "Won!")
            break

        state = state.getChildByEdge(choice)
        print("child", state)
        eval = mcts.evaluate_state(state)
        mcts.backpropagation(state, eval)
        # state = State(game, Player.other(game.player))#state.getChild(choice)

    print("History")
    for h in game.history:
        print(h)
    mcts.tree.print_entire_tree()