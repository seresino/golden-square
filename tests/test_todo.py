from lib.todo import *
import pytest

"""
Given a task,
ToDo instantiates with self.task = task
and self.complete = false
"""
def test_todo_instantiates():
    todo = Todo("Eat food!")
    assert isinstance(todo, Todo)
    assert todo.task == "Eat food!"
    assert todo.complete == False

"""
Given an empty string task
ToDo does not instantiate and raises "Task is empty!"
"""
def test_todo_instantiate_empty_string():
    with pytest.raises(Exception) as e:
        todo = Todo("")
    error = str(e.value)
    assert error == "Task is empty!"

"""
Given an non-string string task
ToDo does not instantiate and raises "Task must be a string!"
"""
def test_todo_instantiate_non_string():
    with pytest.raises(Exception) as e:
        todo = Todo(24)
    error = str(e.value)
    assert error == "Task must be a string!"

"""
Given an instance of a Todo
mark_complete sets complete property to true
"""
def test_complete():
    todo = Todo("Eat food!")
    todo.mark_complete()
    assert todo.complete == True

"""
Given an instance of a Todo
mark_complete sets complete property to true
"""
def test_complete():
    todo = Todo("Eat food!")
    todo.mark_complete()
    assert todo.complete == True

