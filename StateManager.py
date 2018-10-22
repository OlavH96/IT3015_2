from NIM import *
from Move import *
import random


class StateManager:

    def __init__(self):
        pass

    def generate_initial_state(self, data, player):
        self.initial_player = player
        self.game = NIM(*data, player=player)
        return self.game

    def get_current_player(self):
        return self.game.player

    def generate_child_states(self, state):
        out = []
        for e in state.getValidMoves():
            copy = state.__copy__()
            copy.take(e)
            out.append(copy)  # Move(state, e, copy))
        return out

    def get_moves(self, state):
        out = []
        for e in state.getValidMoves():
            copy = state.__copy__()
            out.append(Move(state, e, copy.take(e), state.player))
        return out

    def random_legal_move(self, state):
        moves = self.get_moves(state)
        if len(moves) == 0: return None
        return moves[random.randint(0, len(moves) - 1)]

    def isWinningState(self, state):
        return state.isWinningState()

    def reward(self, state):
        return 1 if state.isWinningState() and state.player else -1
