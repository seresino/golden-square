"""
given an empty string
function returns False
"""
from lib.challenge_3 import *

def test_empty_string_false():
    result = contains_todo("")
    assert result == False

"""
given a single string that does not contain #TODO
function returns False
"""

def test_word_not_TODO():
    result = contains_todo("hello")
    assert result == False

"""
given a single word that is #TODO 
function returns True
"""

def test_string_equals_todo_true():
    result = contains_todo("#TODO")
    assert result == True

"""
given a multi word string that contains #TODO
function returns True
"""

def test_string_contains_todo():
    result = contains_todo("I have many things #TODO today")
    assert result == True