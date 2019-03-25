from .repeated_word import repeated_word
import pytest


def test_exists():
    assert repeated_word


def test_instantiation():
    """
    """
    assert repeated_word('the quick brown fox jumps over the lumpy log')

def test_first():
    """
    """
    actual = repeated_word('the quick brown fox jumps over the lumpy log')
    expected = 'the'
    assert actual == expected

def test_second():
    """
    """
    actual = repeated_word('a quick brown fox and a cat, jump over a lumpy log')
    expected = 'a'
    assert actual == expected

def test_third():
    """
    """
    actual = repeated_word('no and no and no no')    
    expected = 'no'
    assert actual == expected

def test_fourth():
    """
    """
    actual = repeated_word('no and yes or but so')    
    expected = False
    assert actual == expected

def test_fifth():
    """
    """
    actual = repeated_word('')    
    expected = False
    assert actual == expected


"""
FOR THE FUTURE

"""

def test_sixth():
    """
    """
    pass

def test_seventh():
    """
    """
    pass

def test_eighth():
    """
    """
    pass

def test_ninth():
    """
    """
    pass

def test_tenth():
    """
    """
    pass
