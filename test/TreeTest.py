from Tree import *

if __name__ == '__main__':
    root = 1
    tree = Tree(root)

    for i in range(2,10):

        node = tree.addChild(i)
        if i == 8:
            node.addChild(20)

    tree.print_entire_tree()

    t = Tree.find(20, tree)



