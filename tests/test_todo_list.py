from lib.todo_list import *
import pytest

"""
ToDo List instantiates
and stores list of todos
"""
def test_todo_instantiates():
    list = TodoList()
    assert isinstance(list, TodoList)
    assert list.todos == []


"""
Given a non-todo object, 
add throws error
"""

"""
Given an object of type TodoList with no Todos
Incomplete raises error
"""

"""
Given an object of type TodoList with no Todos
Complete raises error
"""

"""
Given an object of type TodoList with no Todos
give_up raises error
"""