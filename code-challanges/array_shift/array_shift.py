"""
information later
"""

from math import ceil

def insert_shift_array(array, value):
  mid = ceil(len(array) / 2)
  new_arr = []
  for i in range(0, mid):
    new_arr.append(array[i])
  new_arr.append(value)
  for i in range(mid, len(array)):
    new_arr.append(array[i]) 
  return new_arr

