class Node:
    def __init__(self, value):
        self.value: int = value
        self.left: Node | None = None
        self.right: Node | None = None


class BinarySearchTree:
    def __init__(self):
        self.root: Node | None = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
