from linked_list import LinkedList
"""

Will return true when finding a value within the linked list that exists
Will return false when searching for a value in the linked list that does not exist
Can properly return a collection of all the values that exist in the linked list
"""

def test_exists():
    assert LinkedList

def test_instantiation():
    """
    Can successfully instantiate an empty linked list
    """
    assert LinkedList()

def test_insert_one():
    """
    Can properly insert into the linked list
    The head property will properly point to the first node in the linked list
    """
    fruits = LinkedList()
    fruits.insert('pears')

    expected = 'pears'
    actual = fruits.head.value

    assert expected == actual

def test_insert_two():
    """
    Can properly insert multiple nodes into the linked list
    """
    fruits = LinkedList()
    fruits.insert('pears')
    fruits.insert('watermelon')

    assert fruits.head.value == 'pears'

    assert fruits.head._next.value == 'watermelon'

def test_insert_three():
    """
    Can properly insert multiple nodes into the linked list
    """
    fruits = LinkedList()
    fruits.insert('pears')
    fruits.insert('watermelon')
    fruits.insert('pineapple')

    assert fruits.head.value == 'pears'

    assert fruits.head._next.value == 'watermelon'

    assert fruits.head._next._next.value == 'pineapple'

def test_includes():
    fruits = LinkedList()
    fruits.insert('pears')
    fruits.insert('watermelon')
    fruits.insert('pineapple')

    assert fruits.includes('watermelon')

def test_not_includes():
    fruits = LinkedList()
    fruits.insert('pears')
    fruits.insert('watermelon')
    fruits.insert('pineapple')

    assert not fruits.includes('zucchini')

def test_print():

    fruits = LinkedList()
    fruits.insert('pears')
    fruits.insert('watermelon')
    fruits.insert('pineapple')

    assert fruits.print() == 'pears,watermelon,pineapple,'

def test_append_item():

    fruits = LinkedList()
    fruits.insert('pears')
    fruits.insert('watermelon')
    fruits.insert('pineapple')

    assert fruits.print() == 'pears,watermelon,pineapple,'

def test_insert_before():

    fruits = LinkedList()
    fruits.insert('pears')
    fruits.insert('watermelon')
    fruits.insert('pineapple')

    fruits.insert_before('pineapple','poptart')

    assert fruits.print() == 'pears,watermelon,poptart,pineapple,'


def test_insert_before_2():

    fruits = LinkedList()
    fruits.insert('pears')
    fruits.insert('watermelon')
    fruits.insert('pineapple')
    fruits.insert('grapes')
    fruits.insert('berry')
    fruits.insert('cherries')
    fruits.insert('orange')
    fruits.insert('apple')

    fruits.insert_before('orange','blackberry')

    assert fruits.print() == 'pears,watermelon,pineapple,grapes,berry,cherries,blackberry,orange,apple,'

def test_insert_after():

    fruits = LinkedList()
    fruits.insert('pears')
    fruits.insert('watermelon')
    fruits.insert('pineapple')
    fruits.insert('grapes')
    fruits.insert('berry')
    fruits.insert('cherries')
    fruits.insert('orange')
    fruits.insert('apple')

    fruits.insert_after('watermelon','blackberry')

    assert fruits.print() == 'pears,watermelon,blackberry,pineapple,grapes,berry,cherries,orange,apple,'

