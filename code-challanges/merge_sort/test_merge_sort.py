from .merge_sort import merge_sort
import random

def test_if_merge_sorted_array():
    list_a = [12, 11, 13, 5, 6, 7]
    # assert merge_sort(list_a) == [5, 6, 7, 11, 12, 13]
    pass

def test_one_number_array():
    list_a = [7]
    assert merge_sort(list_a) == [7]
    pass

def test_empty_array():
    list_a = []
    assert merge_sort(list_a) == [] 
    pass

def test_random_number_generated_array():
    list_a = random.sample(range(1, 100), 10)
    list_b = list_a.copy()
    list_b.sort()
    # assert merge_sort(list_a) == list_b
    pass