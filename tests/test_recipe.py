import pytest
from lib.recipe_one import *

"""
Given an empty string
Returns error message "No text!"
"""
def test_empty_string_error():
    with pytest.raises(Exception) as e:
        reading_time("")
    assert str(e.value) == "No text!"


"""
Given a string of 600 words
Returns correct reading time of 3 (minutes)
"""
def test_600_words():
    result = reading_time("a a a a a a a a a a " * 60)
    assert result == 3


"""
Given a string of 620 words
Returns correct reading time of 4 (minutes)
"""
def test_620_words():
    result = reading_time("a a a a a a a a a a " * 62)
    assert result == 4


"""
Given a non-string input
Return error message "Wrong data type."
"""
def test_non_string():
    assert reading_time(12.75) == "Wrong data type."