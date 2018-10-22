from Edge import *


class Node:

    def __init__(self, content, parent=None):
        self.content = content
        self.edges = set()
        self.parent = parent

    def addChild(self, edgeContent, toContent):
        toNode = Node(toContent, self)
        edge = Edge(self, toNode, edgeContent)
        self.edges.add(edge)
        return toNode

    def getChild(self, content):
        return Node.find(content, self)

    def getChildByEdge(self, edgeContent):
        print("Finding",edgeContent)
        for edge in self.edges:
            print(edge.content)
            if edge.content == edgeContent: return edge.toState

    def getEdgeTo(self, otherNode):

        for edge in self.edges:
            if edge.toState == otherNode:
                return edge
        return None

    def __str__(self):
        return "Node{content=" + str(self.content) + ", children=" + str(len(self.edges)) + "}"

    def print_entire_tree(self):
        self.print_tree(self, 0)

    def print_tree(self, node, i, edge=None):
        to_print = "|" * i
        #if edge: print(to_print, edge)
        print(to_print, node, "->", edge)
        for edge in node.edges:
            # print("Edge",edge)
            to = edge.toState
            # print("To",to)
            self.print_tree(to, i + 1, edge)

    # DFS search
    @staticmethod
    def find(content, tree):
        if tree.content == content: return tree

        for c in tree.edges:
            node = Node.find(content, c.toState)
            if node is not None:
                return node