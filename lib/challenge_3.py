
"""
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.
"""


def contains_todo(text):
    """
    checks text contains the string '#TODO'


    Parameters: (list all parameters and their types)
        text: string containing a number of words.

    Returns: (state the return value and its type)
        boolean: True / False

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    words = text.split()

    if "#TODO" in words:
        return True
    else:
        return False
    