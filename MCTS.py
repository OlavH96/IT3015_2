from Tree import *
from Move import *
from State import *
from Player import *


class MCTS:

    def __init__(self, statemanager, initial_state):
        self.statemanager = statemanager
        print(initial_state)
        self.root = self.statemanager.generate_initial_state(*initial_state)
        self.tree = Tree(Move(None, None, self.root))

    def generate_tree(self, state):
        self.tree = Tree(state)
        children = self.statemanager.generate_child_states(state)
        for c in children:
            child = Tree(c)
            print("added node ", child)
            self.tree.addChild(child)
            self.continue_generate_tree(c, child)

    def continue_generate_tree(self, state, tree):
        children = self.statemanager.generate_child_states(state)
        print(children)
        for c in children:
            print(c)
            child = Tree(c)
            tree.addChild(child)
            self.continue_generate_tree(c, child)
            print("added node ", child)

    def rollout(self, state, policy):

        game = state.game
        initial_player = state.player
        while not game.isDone():
            game = state.game
            move = policy.chose(game, self.statemanager.get_moves(game))
            game.take(move.move)
            state = State(game, Player.other(state.player))
        if state.player is initial_player:  # we won
            return 1
        return -1

    def tree_search(self, start_state, policy):
        man = self.statemanager

        choice = policy.chose(start_state, man.get_moves(start_state))
        return choice

    def node_expansion(self, parent):
        moves = self.statemanager.get_moves(parent.content.result)
        for m in moves:
            parent.addChild(m)
            # self.node_expansion(Tree.find(m, parent))

    def leaf_evaluation(self, state, policy):
        value = self.rollout(state, policy)
        return value
        pass

    def backpropagation(self, final_state, path):
        r = self.statemanager.reward(final_state)

        # path = list of moves from start to finish
        for move in path:
            fromState = move.parent
            toState = move.result
            move.reward += r

            toState.visits += 1
            toState.reward += r
