from State import *
from Move import *

from math import sqrt, log10


class Policy:

    def __init__(self, player):
        self.player = player
        self.c = 0.5  # exploration factor

    def Q(self, state, move, z=0):
        return move.reward

    def u(self, state, action):
        Ns = state.visits
        Nsa = action.visits

        return self.c * sqrt(log10(Ns + 1) / (1 + Nsa))

    def chose(self, state, actions):  # action, list of moves

        options = []
        for action in actions:
            Q = self.Q(state, action)
            u = self.u(state, action)

            if state.player == self.player:
                sum = Q + u
            else:
                sum = Q - u
            options.append(PolicyChoice(state, action, sum))

        # print("Options")
        # for o in options:
        #     print(o)
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
