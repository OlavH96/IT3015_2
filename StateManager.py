from NIM import *
from Move import *

class StateManager:

    def __init__(self):
        print("init")

    def generate_initial_state(self, data):
        self.state = NIM(*data)
        return self.state
    def generate_child_states(self, state):
        out = []
        for e in state.getValidMoves():
            copy = state.__copy__()
            copy.take(e)
            out.append(copy)#Move(state, e, copy))
        return out

    def isWinningState(self, state):
        return state.isWinningState()