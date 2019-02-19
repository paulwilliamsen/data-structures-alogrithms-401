one = [1, 2, 3, 4]
two = []

def reverse_array(arr):
  for i in range(len(arr), 0, -1):
    two.append(arr[i-1])
  return two
   
reverse_array(one)
print(two)
