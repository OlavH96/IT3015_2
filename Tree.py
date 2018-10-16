class Tree:

    def __init__(self, parent):
        self.parent = parent
        self.children = []

    def addChild(self, child):
        self.children.append(Tree(child))

    def __str__(self):
        return "Tree: root="+str(self.parent)+", children="+str(len(self.children))

    def print_entire_tree(self):
        pass
