"""

"""
from tree.tree import BinarySearchTree, Node


def repeated_word(str):
    tree = BinarySearchTree()
    array = str.split(' ')
    node = Node(array[0])
    tree.root = node    
    curr = tree.root

    def _check(curr, node):
        if node.data == curr.data:
            return curr.data

        if node.data < curr.data:
            if not curr.left:
                curr.left = node
            else:
                return _check(curr.left, node)

        if node.data > curr.data:
            if not curr.right:
                curr.right = node
            else:
                return _check(curr.right, node)

        return False

    result = False


    for i in range(1, len(array)):
        node = Node(array[i])
        result = _check(curr, node)
        if result is not False: 
            break

    return result

