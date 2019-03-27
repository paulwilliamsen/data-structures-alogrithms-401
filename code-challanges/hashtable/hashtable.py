from linked_list.linked_list import LinkedList 

class HashTable(object):
    """
    HashTable creation
    """
    def __init__(self):

        self._array = [LinkedList()] * 1024
        # self._array = [None] * 1024

    def hash(self, key):
        """
        hash: takes in an arbitrary key and returns an index in the collection.
        """
        index = int(str(key), 36) * 599 // 1024
        return index

    def add(self, key, value):
        """
        add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
        """
        index = self.hash(key)
        self._array[index].insert((key, value))

        # if not self._array[index]:
        #   self._array[index] =  LinkedList()

        

    def get(self, key):
        """
        get: takes in the key and returns the value from the table.
        """
        index = self.hash(key)
        array = []
        if self._array[index].head:
            current = self._array[index].head
            while current:
                if current.data[0] == key:
                    array.append(current.data[1])
                    current = current._next
                else:
                    current = current._next
        return array

    def contains(self, key):
        """
        contains: takes in the key and returns a boolean, indicating if the key exists in the table already.
        """
        index = self.hash(key)
        if self._array[index].head:
            current = self._array[index].head
            while current:
                if current.data[0] == key:
                    return True
                else:
                    current = current._next
        return False

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
    def __init__(self, data):
        self.data = data
        self._next = None


