from left_join.left_join import left_join
from hashtable.hashtable import HashTable


def test_if_function_exists():
    assert left_join


def test_one():
    def ht1():
        ht1 = Hashtable()
        ht1.add('D', 'A')
        ht1.add('E', 'B')
        ht1.add('F', 'C')
        ht1.add('G', 'D')
        return ht1


    def ht2():
        ht2 = Hashtable()
        ht2.add('D', 'A')
        ht2.add('E', 'B')
        ht2.add('F', 'C')
        ht2.add('G', 'D')
        return ht2

    dict = {
        'D': ['A', 'A'],
        'E': ['B', 'B'],
        'F': ['C', 'C'],
        'G': ['D', 'D'],
    }
    pass
