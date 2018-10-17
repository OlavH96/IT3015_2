class Tree:

    def __init__(self, content):
        self.content = content
        self.children = []
        self.parent = None

    def addChild(self, child):
        node = Tree(child)
        node.parent = self
        self.children.append(node)
        return node

    def getChild(self, content):
        return Tree.find(content, self)

    def __str__(self):
        return "Tree: content=" + str(self.content) + ", children=" + str(len(self.children))

    def print_entire_tree(self):
        self.print_tree(self, 0)

    def print_tree(self, node, i):
        to_print = " " * i
        print(to_print, node)
        for c in node.children:
            self.print_tree(c, i + 1)

    # DFS search
    @staticmethod
    def find(node, tree):

        if tree.content == node: return tree

        for c in tree.children:
            node = Tree.find(node, c)

        return node
