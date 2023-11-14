from math import ceil

"""
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.
"""

def count_words(string):
    return len(string.split())

def reading_time(text):
    """Estimates reading time for texts based on reading time of 200words/minute

    Parameters: (list all parameters and their types)
        text: string containing a number of words.

    Returns: (state the return value and its type)
        an integer which represents the time to read the piece of text given in minutes, rounded to the nearest whole minutes

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    if text == "":
        raise Exception("No text!")

    try:
        n = count_words(text)
        print(n)
        return ceil(n/200)
    except:
        return "Wrong data type."
