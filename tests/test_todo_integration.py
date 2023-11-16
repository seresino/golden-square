from lib.todo import *
from lib.todo_list import *
import pytest

"""
Given a todo object,
TodoList's add, adds that object to it's list
"""
# def test_todo_adds():
#     todo = Todo("Eat!")
#     list = TodoList()
#     list.add(todo)
#     assert list.todos == ["Eat!"]

"""
Given an object of type TodoList with incomplete Todos
Incomplete returns incomplete todos
"""
def test_todo_incomplete():
    todo = Todo("Eat!")
    list = TodoList()
    list.add(todo)
    assert list.incomplete() == ["Eat!"]


"""
Given an object of type TodoList with added Todos but all complete
Incomplete returns "All tasks are complete!"
"""
def test_todo_incomplete_error():
    todo = Todo("Eat!")
    todo.mark_complete()
    list = TodoList()
    list.add(todo)
    with pytest.raises(Exception) as e:
        list.incomplete()
    error = str(e.value)
    assert error == "All tasks are complete!"

"""
Given an object of type TodoList with complete Todos
Complete returns complete todos
"""
def complete():
    todo = Todo("Eat!")
    todo.mark_complete()
    list = TodoList()
    list.add(todo)
    assert list.complete() == ["Eat!"]


"""
Given an object of type TodoList with added Todos but all incomplete
Incomplete returns "All tasks are incomplete!"
"""
def test_todo_complete_error():
    todo = Todo("Eat!")
    list = TodoList()
    list.add(todo)
    with pytest.raises(Exception) as e:
        list.complete()
    error = str(e.value)
    assert error == "All tasks are incomplete!"


"""
Given an object of type TodoList with incomplete Todos
give_up makes all as complete
"""


"""
Given an object of type TodoList with all completed Todos
give_up raises error "No need to give up, all todos are complete!"
"""