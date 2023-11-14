from lib.count_words import *

"""
Given an empty string
Return 0
"""
def test_empty_string_return_0():
    result = count_words("")
    assert result == 0

"""
Given a one word string
Return 1
"""
def test_one_word_string_return_1():
    result = count_words("Hello")
    assert result == 1

"""
Given a 3 word string
Return 3
"""
def test_three_word_string_return_3():
    result = count_words("Hello, I'm Ruby.")
    assert result == 3