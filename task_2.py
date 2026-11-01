from bst import BinarySearchTree


def sum_tree(root):
    if root is None:
        return 0

    return (
        root.value
        + sum_tree(root.left)
        + sum_tree(root.right)
    )


if __name__ == "__main__":
    tree = BinarySearchTree()

    values = [10, 5, 15, 2, 7, 12, 20]

    for value in values:
        tree.insert(value)

    print("Сума всіх значень:", sum_tree(tree.root))
