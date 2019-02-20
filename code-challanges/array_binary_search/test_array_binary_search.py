from array_binary_search import binary_search
"""
Test for binary search
"""

def test_binary_search():
  actual = binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 5)
  expected = 4
  assert expected == actual

def test_binary_search_two():
  actual = binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 2)
  expected = 1
  assert expected == actual

def test_binary_search_three():
  actual = binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 12)
  expected = 11
  assert expected == actual