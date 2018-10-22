from Player import Player
from State import *
from Move import *

from math import sqrt, log10


class Policy:

    def __init__(self, player):
        self.player = player
        self.c = 1  # exploration factor

    def Q(self, state, move, z=0):
        # print("Reward is",move.reward)
        # print(move)
        return move.reward

    def u(self, node, action):
        Ns = node.visits
        Nsa = action.visits

        return self.c * sqrt(log10(Ns) / (1 + Nsa))

    def chose(self, node, actions):  # action, list of moves
        state = node.content
        options = []
        for action in actions:
            Q = self.Q(node, action)
            u = self.u(node, action)

            if state.player == self.player:
                sum = Q + u
            else:
                sum = Q - u
            options.append(PolicyChoice(state, action, sum))

        if state.player == self.player:
            return max(options, key=lambda e: e.QuSum).move
        else:
            return min(options, key=lambda e: e.QuSum).move


class PolicyChoice:

    def __init__(self, state, move, QuSum):
        self.state = state
        self.move = move
        self.QuSum = QuSum

    def __str__(self):
        return "State=" + str(self.state) + ", move=" + str(self.move) + ", quSum=" + str(self.QuSum)
