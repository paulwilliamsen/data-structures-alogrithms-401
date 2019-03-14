from tree import BinarySearchTree, BinaryTree, Node


def test_emoty_tree():
    """
    Can successfully instantiate an empty tree
    """

    tree = BinaryTree()
    assert tree.root is None

def test_single_root_node():
    """
    Can successfully instantiate a tree with a single root node
    """
    tree = BinarySearchTree()
    tree.add(45)

    assert tree.root.data == 45

def test_left_add():
    """
    Can successfully add a left child and right child to a single root node
    """
    tree = BinarySearchTree()
    tree.add(6)
    tree.add(5)
    tree.add(7)
    tree.add(8)

    assert tree.root.left.data == 5
    assert tree.root.right.data == 7


def test_pre_order():
    """
    Can successfully return a collection from a preorder traversal
    """
    tree = BinarySearchTree()
    tree.add(6)
    tree.add(5)
    tree.add(7)
    tree.add(8)
    tree.add(3)
    tree.add(4)
    
    assert tree.pre_order(tree.root) == [6, 5, 3, 4, 7, 8] 
    
def test_post_order():
    """
    Can successfully return a collection from an post order traversal
    """
    tree = BinarySearchTree()
    tree.add(6)
    tree.add(5)
    tree.add(7)
    tree.add(8)
    tree.add(3)
    tree.add(4)
    
    assert tree.post_order(tree.root) == [4, 3, 5, 8, 7, 6]

def test_in_order():
    """
    Can successfully return a collection from an in Order traversal
    """
    tree = BinarySearchTree()
    tree.add(6)
    tree.add(5)
    tree.add(7)
    tree.add(8)
    tree.add(3)
    tree.add(4)
    
    assert tree.in_order(tree.root) == [3, 4, 5, 6, 7, 8]

def test_contains_true():
    """

    """
    tree = BinarySearchTree()
    tree.add(6)
    tree.add(5)
    tree.add(7)
    tree.add(8)
    tree.add(3)
    tree.add(4)

    assert tree.contains(5) is True

def test_contains_false():
    """

    """
    tree = BinarySearchTree()
    tree.add(6)
    tree.add(5)
    tree.add(7)
    tree.add(8)
    tree.add(3)
    tree.add(4)

    assert tree.contains(55) is False

def test_max():
    """

    """
    tree = BinarySearchTree()
    tree.add(6)
    tree.add(5)
    tree.add(7)
    tree.add(8)
    tree.add(3)
    tree.add(4)

    assert tree.get_max_value() == 8

def test_max():
    """

    """
    tree = BinarySearchTree()
    tree.add(364)
    tree.add(64)
    tree.add(264)
    tree.add(67)
    tree.add(164)
    tree.add(54)
    tree.add(464)
    tree.add(4)
    tree.add(53)
    tree.add(7)
    tree.add(82)
    tree.add(322)
    tree.add(489)

    assert tree.get_max_value() == 489