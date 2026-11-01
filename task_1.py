from bst import BinarySearchTree


def find_min(root):
    if root is None:
        return None

    current = root

    while current.left is not None:
        current = current.left

    return current.value


if __name__ == "__main__":
    tree = BinarySearchTree()

    values = [10, 5, 15, 2, 7, 12, 20]

    for value in values:
        tree.insert(value)

    print("Мінімальне значення:", find_min(tree.root))
