from lib.grammar import GrammarStats
import pytest

"""
Given an empty string, 
returns error
"""
def empty_string_error():
    grammarinfo = GrammarStats()
    with pytest.raises(Exception) as e:
        grammarinfo.check("")
    error = str(e.value)
    assert error == "No text!"


"""
Given a text that begins with a capital letter and ends with a sentence-ending punctuation mark,
returns true
"""
def return_true():
    grammarinfo = GrammarStats()
    result = grammarinfo.check("Hello, I'm Ruby.")
    assert result == True


"""
Given a text that begins with a capital letter but ends with a letter,
return false
"""

"""
Given a text that begins with a capital letter but ends with a colon,
return false
"""

"""
Given a text that doesn't begin with a capital letter but does end with a question mark,
return false
"""

"""
Given a text that doesn't begin with a capital letter but does end with an exclamation mark,
return false
"""