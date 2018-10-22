from Edge import *
from Node import *

if __name__ == '__main__':

    root = 1
    tree = Node(1)

    tree.addChild(1, 2)
    node = tree.addChild(2, 3)

    node.addChild(1, 4)
    tree.print_entire_tree()

    findNode = Node.find(3, tree)
    print(findNode)
    print()
    for edge in findNode.edges:
        print(edge)
    parent = findNode.parent
    print()
    for edge in parent.edges:
        print(edge)
