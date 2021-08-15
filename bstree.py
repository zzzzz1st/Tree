def maxDepth(node):
    if node is None:
        return 0
    else:
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
        if lDepth > rDepth:
            return lDepth + 1
        else:
            return rDepth + 1


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    # Il metodo insert per inserire un dato.
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Il metodo search per trovare un dato.
    def search(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval) + " non trovato"
            return self.left.search(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval) + " non trovato"
            return self.right.search(lkpval)
        else:
            print(str(self.data) + ' è stato trovato')

    # Il metodo printTree per stampare tutti i valori dell'albero.
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()
