from Node import *
from Move import *
from State import *
from Player import *


class MCTS:

    def __init__(self, statemanager, initial_state):
        self.statemanager = statemanager
        self.root = initial_state
        self.tree = Node(self.root)

    def evaluate_state(self, node, policy=None):
        game = node.content
        wins = 0
        losses = 0

        for i in range(10):  # num rollouts
            next_game = game.__copy__() # copy the initial state / game
            while not next_game.isDone():
                move = self.statemanager.random_legal_move(next_game) # use policy somehow
                if move:
                    #node.addChild(move, move.result)
                    next_game = move.result
            if next_game.winner == self.root.player:
                wins += 1
            else:
                losses += 1
        edges = node.edges
        print("Edges")
        print(edges)
        for edge in edges:
            edge.reward = (wins - losses) / (wins + losses)
        for edge in edges:
            print("Edge")
            print(edge)

        return (wins - losses) / (wins + losses)  # [1, 1], Q value

    def rollout(self, state, policy):
        print("Rolling out ", state)
        game = state.game
        initial_player = state.player

        while not game.isDone():
            game = state.game  # copy of game
            move = policy.chose(game, self.statemanager.get_moves(game))
            print("Policy took move", move)
            game.take(move.move)
            state = State(game, Player.other(state.player))
        if state.game.winner is initial_player:
            return 1
        return -1

    def tree_search(self, start_state, policy):
        man = self.statemanager

        choice = policy.chose(start_state, man.get_moves(start_state))
        return choice

    def node_expansion(self, parent):
        moves = self.statemanager.get_moves(parent.content)
        for m in moves:
            node = parent.addChild(m, m.result)
            #self.leaf_evaluation(node)
            self.node_expansion(node)

    def leaf_evaluation(self, state, policy=None):
        value = self.evaluate_state(state, policy)
        node = Node.find(state, self.tree)
        return value

    def backpropagation(self, final_node, evaluation):
        #r = self.statemanager.reward(final_node)

        # path = list of moves from start to finish
        print("Backpropagation")
        node = final_node
        while node.parent:
            print("Node",node)

            fromState = node.parent
            edge = fromState.getEdgeTo(node)
            move = edge.content
            toState = move.result
            move.reward += evaluation
            move.visits += 1
            node = node.parent

            #toState.visits += 1
            #toState.reward += evaluation
