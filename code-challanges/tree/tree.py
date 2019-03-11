class Node():
  """

  """
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

class BinaryTree():
  """

  """
  def __init__(self):
    self.root = None

  def pre_order(self, node):
    """
    NODE - LEFT - RIGHT
    """
    output_array = []
    output_array.append(node.data)
    if node.left:
      output_array += self.pre_order(node.left)
    if node.right:
      output_array += self.pre_order(node.right)
    return output_array


  def in_order(self, node):
    """
    LEFT - NODE - RIGHT
    """
    output_array = []
    if node.left:
      output_array += self.in_order(node.left)
    output_array.append(node.data)
    if node.right:
      output_array += self.in_order(node.right)
    return output_array

  def post_order(self, node):
    """
    LEFT - RIGHT - NODE
    """
    output_array = []
    if node.left:
      output_array += self.post_order(node.left)
    if node.right:
      output_array += self.post_order(node.right)
    output_array.append(node.data)   
    return output_array
    

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
      if data >= curr.data:
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

    if curr.left:
      self.contains(data, curr.left)

    if curr.right:
      self.contains(data, curr.right)

    return False