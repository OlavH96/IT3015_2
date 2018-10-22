from Player import *
from NIM import *
import random
from StateManager import *
from MCTS import *
from Policy import *
from RandomPolicy import *


def play_game(mcts):
    start = mcts.tree
    state = start
    game = start.content.__copy__()

    while not game.isDone():

        choice = mcts.tree_search(state)
        # print("choice is",choice)
        # print(game)
        game.take(choice.move)  # take real move
        # print(game)

        state = state.getChildByEdge(choice)

        if game.isDone():
            if verbose:
                print(game.winner, "Won!")
            break

        # eval = mcts.evaluate_state(state)
        # mcts.backpropagation(state, eval)
        # state = State(game, Player.other(game.player))#state.getChild(choice)

    if verbose:

        print("\nHistory\n")
        history = []
        while state.parent:
            history.append(state.parent.getEdgeTo(state).content)  # traverse in reverse order
            state = state.parent
        history.reverse()
        for h in history:
            print(h)
        print()
    return game.winner


if __name__ == '__main__':
    verbose = True
    G = 100
    M = 100

    N = 11
    K = 5

    init_player = Player.PLAYER_1
    policy = Policy(init_player)
    random_policy = RandomPolicy(init_player)

    stateman = StateManager()
    game = stateman.generate_initial_state([N, K], player=init_player)

    wins = 0
    losses = 0

    mcts = MCTS(statemanager=stateman, initial_state=game, policy=policy, default_policy=random_policy, M=M)
    for i in range(G):
        winner = play_game(mcts)
        #mcts.tree.print_entire_tree()
        if winner == init_player: wins+=1
        else: losses +=1

    if verbose:
        mcts.tree.print_entire_tree()

    print("Wins",wins)
    print("Losses",losses)
    print("Winrate", (wins / G) * 100, "%")

