from .radix import radix_sort


def test_sorted_array_is_sorted():
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert radix_sort(sorted_list) == sorted_list


def test_empty():
    assert radix_sort([]) == []


def test_single_element():
    assert radix_sort([6]) == [6]


def test_unsorted_returns_sorted():
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mixed_list = [7, 5, 2, 4, 3, 8, 9, 10, 1, 6]
    assert radix_sort(mixed_list) == sorted_list

