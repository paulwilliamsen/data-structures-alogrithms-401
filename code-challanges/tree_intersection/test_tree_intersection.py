from tree_intersection.tree_intersection import tree_intersection
from hashtable.hashtable import HashTable
from tree.tree import BinarySearchTree


def test_one():
    tree1 = BinarySearchTree()
    tree1.add(6)
    tree1.add(7)
    tree1.add(5)
    tree1.add(8)
    tree1.add(3)
    tree1.add(4)

    tree2 = BinarySearchTree()
    tree2.add(62)
    tree2.add(7)
    tree2.add(53)
    tree2.add(8)
    tree2.add(32)
    tree2.add(42)
    

    assert tree_intersection(tree1, tree2) == [7, 8]
