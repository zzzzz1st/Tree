import time


class Node:
    RED = True
    BLACK = False

    def __init__(self, key, color=RED):
        if not type(color) == bool:
            raise TypeError("Il tipo sbagliato, serve True/False però è stato dato %s" % color)
        self.color = color
        self.key = key
        self.left = self.right = self.parent = NilNode.instance()

    def __nonzero__(self):
        return True

    def __bool__(self):
        return True


# La classe NilNode per introdurre un nodo Null
class NilNode(Node):
    __instance__ = None

    @classmethod
    def instance(cls):
        if cls.__instance__ is None:
            cls.__instance__ = NilNode()
        return cls.__instance__

    def __init__(self):
        self.color = Node.BLACK
        self.key = None
        self.left = self.right = self.parent = None

    def __nonzero__(self):
        return False

    def __bool__(self):
        return False


class RedBlackTree:
    def __init__(self):
        self.root = NilNode.instance()
        self.size = 0

    # Il metodo add per inserire un dato.
    def add(self, key):
        self.insert(Node(key))

    # Il metodo insert per inserire un nodo.
    def insert(self, x):
        self.__insert_helper(x)

        x.color = Node.RED
        while x != self.root and x.parent.color == Node.RED:
            if x.parent == x.parent.parent.left:
                y = x.parent.parent.right
                if y and y.color == Node.RED:
                    x.parent.color = Node.BLACK
                    y.color = Node.BLACK
                    x.parent.parent.color = Node.RED
                    x = x.parent.parent
                else:
                    if x == x.parent.right:
                        x = x.parent
                        self.__left_rotate(x)
                    x.parent.color = Node.BLACK
                    x.parent.parent.color = Node.RED
                    self.__right_rotate(x.parent.parent)
            else:
                y = x.parent.parent.left
                if y and y.color == Node.RED:
                    x.parent.color = Node.BLACK
                    y.color = Node.BLACK
                    x.parent.parent.color = Node.RED
                    x = x.parent.parent
                else:
                    if x == x.parent.left:
                        x = x.parent
                        self.__right_rotate(x)
                    x.parent.color = Node.BLACK
                    x.parent.parent.color = Node.RED
                    self.__left_rotate(x.parent.parent)
        self.root.color = Node.BLACK

    def minimum(self, x=None):
        if x is None:
            x = self.root
        while x.left:
            x = x.left
        return x

    def maximum(self, x=None):
        if x is None:
            x = self.root
        while x.right:
            x = x.right
        return x

    def successor(self, x):
        if x.right:
            return self.minimum(x.right)
        y = x.parent
        while y and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self, x):
        if x.left:
            return self.maximum(x.left)
        y = x.parent
        while y and x == y.left:
            x = y
            y = y.parent
        return y

    def inorder_walk(self, x=None):
        if x is None:
            x = self.root
        x = self.minimum()
        while x:
            yield x.key
            x = self.successor(x)

    # Il metodo search per trovare un dato.
    def search(self, key, x=None):
        if x is None:
            x = self.root
        while x and x.key != key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        if x:
            print(str(key) + ' è stato trovato')
            return x

    def is_empty(self):
        return bool(self.root)

    def __left_rotate(self, x):
        if not x.right:
            raise Exception("x.right è nil!")
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        else:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        y.left = x
        x.parent = y

    def __right_rotate(self, x):
        if not x.left:
            raise Exception("x.left è nil!")
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        else:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        y.right = x
        x.parent = y

    def __insert_helper(self, z):
        y = NilNode.instance()
        x = self.root
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if not y:
            self.root = z
        else:
            if z.key < y.key:
                y.left = z
            else:
                y.right = z

        self.size += 1
