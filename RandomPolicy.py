import random

from State import *
from Move import *

from math import sqrt, log10


class RandomPolicy:

    def __init__(self, player):
        self.player = player
        self.c = 0.5  # exploration factor

    def chose(self, state, actions):  # action, list of moves

        return actions[random.randint(0, len(actions) - 1)]
