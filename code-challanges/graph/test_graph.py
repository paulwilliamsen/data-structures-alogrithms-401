from .graph import Graph
import pytest


def test_class():
    assert Graph


def test_graph_instance():
    assert Graph()


def test_addition_of_one_vertex():
    new_graph = Graph()
    new_graph.add_vertex('red')
    assert 'red' in new_graph.new_table


def test_addition_of_two_vertices():
    new_graph = Graph()
    new_graph.add_vertex('red')
    new_graph.add_vertex('green')
    assert 'red' in new_graph.new_table
    assert 'green' in new_graph.new_table


def test_add_one_edge_with_weight():
    new_graph = Graph()
    new_graph.add_vertex('red')
    new_graph.add_vertex('green')

    new_graph.add_edge('red', 'green', 5)

    assert new_graph.new_table['red'] == {'green': 5}
    assert new_graph.new_table['green'] == {'red': 5}


def test_get_vertices():
    new_graph = Graph()
    new_graph.add_vertex('red')
    new_graph.add_vertex('green')
    new_graph.add_vertex('blue')

    assert new_graph.get_vertices() == ['red', 'green', 'blue']


def test_get_vertices_when_none():
    new_graph = Graph()
    assert new_graph.get_vertices() is None


def test_size():
    new_graph = Graph()
    new_graph.add_vertex('red')
    new_graph.add_vertex('green')
    new_graph.add_vertex('yellow')
    new_graph.add_vertex('blue')
    new_graph.add_vertex('orange')
    new_graph.add_vertex('black')
    new_graph.add_vertex('aqua')
    new_graph.add_vertex('white')
    assert new_graph.size() is 8
