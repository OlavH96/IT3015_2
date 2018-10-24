from Node import *
from Move import *
from Player import *


class MCTS:

    def __init__(self, statemanager, initial_state, policy, default_policy, M=10):
        self.statemanager = statemanager
        self.root = initial_state
        self.tree = Node(self.root)
        self.M = M
        self.policy = policy
        self.default_policy = default_policy

    def leaf_evaluation(self, node):
        wins = 0
        losses = 0

        initial_state = node.content

        for i in range(self.M):  # num rollouts
            state = initial_state.__copy__()

            while not self.statemanager.is_final_state(state):
                move = self.default_policy.chose(state, self.statemanager.get_moves(state))
                state = self.statemanager.do_move(state, move)

            if self.statemanager.is_win(state):  # state.winnerF() == self.root.player:
                wins += 1
            else:
                losses += 1

        # [1, -1], Q value, 1 is all games won, -1 is all games lost, 0 is 50/50 split etc
        # print(node)
        # print("wins",wins)
        # print("losses",losses)
        return (wins - losses) / (wins + losses)

    def tree_search(self, node, policy=None):
        if not policy: policy = self.policy
        man = self.statemanager

        if len(node.edges) == 0 and not man.is_final_state(node.content):
            self.node_expansion(node)  # Expand nodes one layer
            node.visits += 1
            for edge in node.edges:  # Get all the moves / edges
                to_node = edge.toNode
                evaluation = self.leaf_evaluation(to_node)  # evaluate each to-node, aka the new nodes
                self.backpropagation(to_node, evaluation)  # Backpropagate
        else:
            node.visits += 1

        choices = [e.content for e in node.edges]
        # for c in choices:
        #     print(c)
        choice = policy.chose(node, choices)
        # print("choice", choice)
        return choice

    def node_expansion(self, node):
        moves = self.statemanager.get_moves(node.content)
        for m in moves:
            node.addChild(m, m.result)

    def backpropagation(self, node, evaluation):

        while node.parent:
            parent = node.parent
            edge_to = parent.getEdgeTo(node)
            edge_to.content.reward += evaluation
            edge_to.content.visits += 1
            node = parent
