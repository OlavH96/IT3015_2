from Node import *
from Move import *
from State import *
from Player import *


class MCTS:

    def __init__(self, statemanager, initial_state, policy, default_policy, M=10):
        self.statemanager = statemanager
        self.root = initial_state
        self.tree = Node(self.root)
        self.M = M
        self.policy = policy
        self.default_policy = default_policy

    def evaluate_state(self, node):
        game = node.content
        wins = 0
        losses = 0

        for i in range(self.M):  # num rollouts
            thisNode = node.content
            #next_game = game.__copy__()  # copy the initial state / game
            game = thisNode.__copy__()

            while not game.isDone():
                move = self.default_policy.chose(thisNode, self.statemanager.get_moves(thisNode))
                game.take(move.move)
                thisNode = move.result
            if game.winnerF() == self.root.player:
                wins += 1
            else:
                losses += 1




            # while not next_game.isDone():
            #     move = self.default_policy.chose(next_game, self.statemanager.get_moves(next_game))
            #     # move = self.statemanager.random_legal_move(next_game)  # use policy somehow
            #     if move:
            #         # node.addChild(move, move.result)
            #         next_game = move.result
            # if next_game.winnerF() == self.root.player:
            #     wins += 1
            # else:
            #     losses += 1
        # [1, -1], Q value, 1 is all games won, -1 is all games lost, 0 is 50/50 split etc
        return (wins - losses) / (wins + losses)

    def tree_search(self, node, policy=None):
        if not policy: policy = self.policy
        man = self.statemanager

        if len(node.edges) == 0 and not man.isWinningState(node.content):
            self.node_expansion(node)  # Expand nodes one layer
            node.visits += 1
            for edge in node.edges:  # Get all the moves / edges
                toNode = edge.toState
                eval = self.evaluate_state(toNode)  # evaluate each to-node, aka the new nodes
                self.backpropagation(toNode, eval)  # Backpropagate

        # print("Choices")
        choices = [e.content for e in node.edges]
        # for c in choices:
        #     print(c)
        choice = policy.chose(node, choices)  # man.get_moves(game))  # dette må ha noe med treet å gjøre
        node.visits += 1
        # print("choice", choice)
        # print()
        return choice

    def node_expansion(self, parent):
        moves = self.statemanager.get_moves(parent.content)
        for m in moves:
            parent.addChild(m, m.result)

    def leaf_evaluation(self, state):
        value = self.evaluate_state(state)
        node = Node.find(state, self.tree)
        return value

    def backpropagation(self, node, evaluation):

        while node.parent:
            parent = node.parent
            edgeTo = parent.getEdgeTo(node)
            edgeTo.content.reward += evaluation
            edgeTo.content.visits += 1
            node = parent
