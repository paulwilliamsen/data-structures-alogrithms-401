from array_shift import insert_shift_array

def test_even_length_array():
  actual = insert_shift_array([1,2,3,4,5,6], 100)
  expected = [1,2,3,100,4,5,6]
  assert actual == expected

def test_odd_length_array():
  actual = insert_shift_array([1,2,3,4,5], 100)
  expected = [1,2,3,100,4,5]
  assert actual == expected

def test_length_array():
  actual = insert_shift_array([1,2,3,4,5,6,7,8,9,11,12,13,14,14,14,55,45,454,565,76], 100)
  expected = [1,2,3,4,5,6,7,8,9,11,100,12,13,14,14,14,55,45,454,565,76]
  assert actual == expected