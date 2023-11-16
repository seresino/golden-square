from lib.grammar import GrammarStats
import pytest


def test_instantiation():
    grammarinfo = GrammarStats()
    assert isinstance(grammarinfo, GrammarStats)

"""
Given an empty string, 
returns error
"""
def test_empty_string_error():
    grammarinfo = GrammarStats()
    with pytest.raises(Exception) as e:
        grammarinfo.check("")
    error = str(e.value)
    assert error == "No text!"


"""
Given a text that begins with a capital letter and ends with a sentence-ending punctuation mark,
returns true
"""
def test_return_true():
    grammarinfo = GrammarStats()
    result = grammarinfo.check("Hello, I'm Ruby.")
    assert result == True


"""
Given a text that begins with a capital letter but ends with a letter,
return false
"""
def test_return_true():
    grammarinfo = GrammarStats()
    result = grammarinfo.check("Hello, I'm Ruby")
    assert result == False

"""
Given a text that begins with a capital letter but ends with a colon,
return false
"""
def test_return_true():
    grammarinfo = GrammarStats()
    result = grammarinfo.check("Hello, I'm Ruby:")
    assert result == False

"""
Given a text that doesn't begin with a capital letter but does end with a question mark,
return false
"""
def test_return_true():
    grammarinfo = GrammarStats()
    result = grammarinfo.check("hello, I'm Ruby?")
    assert result == False

"""
Given a text that doesn't begin with a capital letter but does end with an exclamation mark,
return false
"""
def test_return_true():
    grammarinfo = GrammarStats()
    result = grammarinfo.check("hello, I'm Ruby!")
    assert result == False

"""
Given 0 texts,
percentage returns error
"""
def test_zero_error():
    grammarinfo = GrammarStats()
    with pytest.raises(Exception) as e:
        grammarinfo.percentage_good()
    error = str(e.value)
    assert error == "No texts given!"

"""
Given 1 texts, 1 of which pass
returns 50
"""
def test_50_percent():
    grammarinfo = GrammarStats()
    grammarinfo.check("hello, I'm Ruby!")
    grammarinfo.check("Hello, I'm Ruby!")
    result = grammarinfo.percentage_good()
    assert result == 50

"""
Given 10 texts, 7 of which pass
returns 70
"""
def test_70_percent():
    grammarinfo = GrammarStats()
    grammarinfo.check("hello, I'm Ruby!")
    grammarinfo.check("hello, I'm Ruby!")
    grammarinfo.check("hello, I'm Ruby!")
    grammarinfo.check("Hello, I'm Ruby!")
    grammarinfo.check("Hello, I'm Ruby!")
    grammarinfo.check("Hello, I'm Ruby!")
    grammarinfo.check("Hello, I'm Ruby!")
    grammarinfo.check("Hello, I'm Ruby!")
    grammarinfo.check("Hello, I'm Ruby!")
    grammarinfo.check("Hello, I'm Ruby!")
    result = grammarinfo.percentage_good()
    assert result == 70