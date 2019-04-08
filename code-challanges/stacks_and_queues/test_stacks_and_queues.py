from stacks_and_queues import Node, Stack


def test_stack_push():
    colors = Stack()
    colors.push('red')

    assert colors.top.data == 'red'

def test_stack_push_two():
    colors = Stack()
    colors.push('red')
    colors.push('blue')

    assert colors.top.data == 'blue'


def test_stack_push_two_return_first():
    colors = Stack()
    colors.push('red')
    colors.push('blue')

    assert colors.top._next.data == 'red'

def test_stack_pop_one():
    colors = Stack()
    colors.push('red')
    colors.push('yellow')
    colors.push('orange')
    colors.push('green')
    colors.pop()

    assert colors.top.data == 'orange'


def test_stack_pop_three():
    colors = Stack()
    colors.push('red')
    colors.push('orange')
    colors.push('green')
    colors.push('blue')
    colors.pop()
    colors.pop()
    colors.pop()

    assert colors.top.data == 'red'


def test_stack_pop_return_value():
    colors = Stack()
    colors.push('orange')
    colors.push('red')

    assert colors.pop() == 'red'


def test_stack_pop_all_return():
    colors = Stack()
    colors.push('red')
    colors.pop()

    assert colors.pop() == 'Empty Stack'


def test_stack_pop_all_top():
    colors = Stack()
    colors.push('red')
    colors.push('blue')
    colors.pop()
    colors.pop()

    assert colors.top is None