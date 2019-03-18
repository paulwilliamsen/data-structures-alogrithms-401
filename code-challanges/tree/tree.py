class Node():
  """

  """
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

class Queue():
    """
    """
    front = None
    rear = None
    empty = 'Empty Queue'

    def enqueue(self, node):
        """
        """
        if self.rear is None:
          self.rear = node
          self.front = node
        else:
          self.rear._next = node
          self.rear = node
       
    def dequeue(self):
        """
        """
        if self.front is not None:
          current = self.front
          self.front = self.front._next
          current._next = None
          if self.front is None:
              self.rear = None
          return current
        else:
            return None
        
       
    def peek(self):
        """
        """
        if self.front is not None:
          return self.front
        else:
          return None
        

class BinaryTree():
  """

  """
  def __init__(self):
    self.root = None

  def pre_order(self, curr=None):
    """
    NODE - LEFT - RIGHT
    """
    output_array = []
    if not curr:
      curr = self.root
    output_array.append(curr.data)
    if curr.left:
      output_array += self.pre_order(curr.left)
    if curr.right:
      output_array += self.pre_order(curr.right)
    return output_array


  def in_order(self, curr=None):
    """
    LEFT - NODE - RIGHT
    """
    output_array = []
    if not curr:
      curr = self.root
    if curr.left:
      output_array += self.in_order(curr.left)
    output_array.append(curr.data)
    if curr.right:
      output_array += self.in_order(curr.right)
    return output_array

  def post_order(self, curr=None):
    """
    LEFT - RIGHT - NODE
    """
    output_array = []
    if not curr:
      curr = self.root
    if curr.left:
      output_array += self.post_order(curr.left)
    if curr.right:
      output_array += self.post_order(curr.right)
    output_array.append(curr.data)   
    return output_array

  def get_max_value(self):
    
    self.max = 0

    def _update_max(node):
      if node.data > self.max:
        self.max = node.data
      if node.left:
        _update_max(node.left)
      if node.right:
        _update_max(node.right)

    if self.root:
      _update_max(self.root)


    return self.max

  def breadth_first(self):
      """
      """
      queue = Queue()
      array = []

      if self.root:
          queue.enqueue(self.root)

      while queue.peek():
          curr = queue.dequeue()
          x.append(curr.data)
          if curr.left:
              queue.enqueue(curr.left)
          if curr.right:
              queue.enqueue(curr.right)

      return array
  

class BinarySearchTree(BinaryTree):
  """

  """
  def add(self, data, curr=None):
    if not self.root:
      self.root = Node(data)
  
    if curr is None:
      curr = self.root
    if curr:
      if data < curr.data:
        if curr.left is None:
          curr.left = Node(data)
        else:
          self.add(data, curr.left)
      if data > curr.data:
        if curr.right is None:
          curr.right = Node(data)
        else:
          self.add(data, curr.right)
    
  def contains(self, data, curr=None):
    """

    """
    if not self.root:
      return False

    if curr is None:
      curr = self.root

    if data == curr.data:
      return True

    if data < curr.data:
      if curr.left:
        return self.contains(data, curr.left)
      
    if data > curr.data:
      if curr.right:
        return self.contains(data, curr.right)
    
    return False

