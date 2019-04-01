from .insertion_sort import insertion_sort
import random

"""
Testing Insertion Sort
"""

def test_if_sorted_array():
    list_a = [2,4,6,8,10,12,14,16]
    assert insertion_sort(list_a) == list_a

def test_two_sorted_array_with_one_number_change():
    list_a = [2,4,6,8,12,14,16,10]
    list_b = [2,4,6,8,10,12,14,16]
    assert insertion_sort(list_a) == list_b

def test_three_backwards_array():
    list_a = [2,4,6,8,10,12,14,16]
    list_b = [16,14,12,10,8,6,4,2]
    assert insertion_sort(list_b) == list_a

def test_one_number_array():
    list_a = [7]
    assert insertion_sort(list_a) == [7]

def test_empty_array():
    list_a = []
    assert insertion_sort(list_a) == [] 

def test_random_number_generated_array():
    list_a = random.sample(range(1, 100), 10)
    list_b = list_a.copy()
    list_b.sort()
    assert insertion_sort(list_a) == list_b

