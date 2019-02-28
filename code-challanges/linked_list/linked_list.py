class LinkedList():

    head = None

    def append_item(self, new_value):
      
      current = self.head
      node = Node(new_value)

      while current._next:
        current = current._next
      current._next = node


    def insert(self, value):
        
      node = Node(value)

      if not self.head:
        self.head = node
      else:
        current = self.head

        while current._next:
          current = current._next

        current._next = node
        

    def insert_before(self, value, new_value):
      current = self.head
      node = Node(new_value)
      while current._next:
        if current._next.value == value:
          node._next = current._next
          current._next = node
          break
        else:
          current = current._next

    def insert_after(self, value, new_value):
      current = self.head
      node = Node(new_value)
      while current._next:
        if current._next.value == value:
          node._next = current._next._next
          current = current._next
          current._next = node
          break
        else:
          current = current._next


    def includes(self, value):
      current = self.head

      while current:
        if current.value == value:
          return True

        current = current._next

      return False

    def find_from_end(self,value):
      length = 0
      curr = self.head
      while curr:
          length += 1
          curr = curr._next
      distance = length - value -1
      curr = self.head
      if length > value :
          for x in range (0,distance):
              curr = curr._next
          return curr.value
      else:
          return 'exception'


    def print(self):
        output = ''
        current = self.head
        while current:
          output += current.value + ','
          current = current._next
        
        return output

    

class Node():
    def __init__(self, value):
        self.value = value
        self._next = None

