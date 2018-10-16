from Tree import *

class MCTS:

    def __init__(self, statemanager):
        self.statemanager = statemanager

    def generate_tree(self, state):
        self.tree = Tree(state)
        children = self.statemanager.generate_child_states(state)
        for c in children:
            child = Tree(c)
            print("added node ",child)
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
            print("added node ",child)

    def rollout(self, state, policy):

        pass

    def tree_search(self, policy):
        pass

    def node_expansion(self, parent):
        pass

    def leaf_evaluation(self, policy):
        pass

    def backpropagation(self, final_state):
        pass
