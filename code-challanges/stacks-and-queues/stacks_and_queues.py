class Node():
    def __init__(self, data):
        self.data = data
        self._next = None

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
            new_node._next = self.top
            self.top = new_node
        return self.top.data

    def pop(self):
        """
        """
        if self.top is not None:
            current = self.top
            self.top = self.top._next
            current._next = None
            return current.data
        else:
            return 'Empty Stack'
        
    def peek(self):
        """
        """
       
class Queue():
    """
    """
    front = None
    rear = None
    empty = 'Empty Queue'

    def enqueue(self, new_data):
        """
        """
       
    def dequeue(self):
        """
        """
       
    def peek(self):
        """
        """
        
