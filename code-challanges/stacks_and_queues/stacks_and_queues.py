class Node():
    def __init__(self, data):
        self.data = data
        self.nxt = None

class Stack():
    """
    """
    top = None
    empty = 'Empty Stack'

    def push(self, new_data):
        """
        """
        new_node = Node(new_data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.nxt = self.top
            self.top = new_node
        return self.top.data

    def pop(self):
        """
        """
        if self.top is not None:
            current = self.top
            self.top = self.top.nxt
            current.nxt = None
            return current.data
        else:
            return 'Empty Stack'
        
    def peek(self):
        """
        """


class Queue():
    """
    New Queue.
    """
    front = None
    rear = None

    def enqueue(self, new_data):
        """
        """
        new_node = Node(new_data)
        if self.rear is None:
            self.rear = new_node
            self.front = new_node
        else:
            self.rear.nxt = new_node
            self.rear = new_node

    def dequeue(self):
        """
        """
        if self.front is not None:
            current = self.front
            self.front = self.front.nxt
            current.nxt = None
            if self.front is None:
                self.rear = None
            return current.data
        else:
            return None

    def peek(self):
        """
        """
        if self.front is not None:
            return self.front.data
        else:
            return None

    def __iter__(self):
        current = self.front
        while current:
            yield current.data
            current = current.nxt

    def __repr__(self):
        return f'<REPR: Queue Object with {self.front} at the front>'

    def __str__(self):
        return f'Queue with {self.front} at the front and {self.rear} at the rear.'