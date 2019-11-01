class Node(object):

    def __init__(self, data, l_child=None, r_child=None):
        self.Data = data
        self.l_child = l_child
        self.r_child = r_child


class BTree(object):
    binary_tree = []

    def __init__(self, root=None):
        self.root = root

    def add(self, new_node):
        node = Node(new_node)

        if self.root == None:
            self.root = node
            binary_tree
