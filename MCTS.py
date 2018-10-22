from Node import *
from Move import *
from State import *
from Player import *


class MCTS:

    def __init__(self, statemanager, initial_state, policy,default_policy, M=10 ):
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
            next_game = game.__copy__()  # copy the initial state / game
            while not next_game.isDone():
                move = self.default_policy.chose(next_game, self.statemanager.get_moves(next_game))
                #move = self.statemanager.random_legal_move(next_game)  # use policy somehow
                if move:
                    # node.addChild(move, move.result)
                    next_game = move.result
            if next_game.winnerF() == self.root.player:
                wins += 1
            else:
                losses += 1
        # print("wins", wins)
        # print("losses", losses)
        # print((wins - losses) / (wins + losses))
        return (wins - losses) / (wins + losses)  # [1, -1], Q value, 1 is all games won, -1 is all games lost, 0 is 50/50 split etc


    def tree_search(self, node, policy=None):
        if not policy: policy = self.policy
        man = self.statemanager
        game = node.content

        if len(node.edges) == 0 and not man.isWinningState(node.content):
            self.node_expansion(node)
            for edge in node.edges:
                eval = self.evaluate_state(edge.toState)
                #print("Eval for", edge, "=", eval)
                self.backpropagation(node, eval)
        else:
            eval = self.evaluate_state(node)
            self.backpropagation(node, eval)


        # print()
        choices = [e.content for e in node.edges]
        # for c in choices:
        #     print(c)
        # print()
        choice = policy.chose(game, choices)  # man.get_moves(game))  # dette må ha noe med treet å gjøre
        return choice

    def node_expansion(self, parent):
        moves = self.statemanager.get_moves(parent.content)
        for m in moves:
            node = parent.addChild(m, m.result)
            # self.leaf_evaluation(node)
            # self.node_expansion(node)

    def leaf_evaluation(self, state):
        value = self.evaluate_state(state)
        node = Node.find(state, self.tree)
        return value

    def backpropagation(self, final_node, evaluation):

        node = final_node
        #print("Doing backprop for",node,"eval",evaluation)
        while node.parent:
            fromState = node.parent
            edge = fromState.getEdgeTo(node)
         #   print("edge",edge)
            move = edge.content
            move.reward += evaluation
            move.visits += 1
            node = node.parent

            # toState.visits += 1
            # toState.reward += evaluation
