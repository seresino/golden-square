# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.todos.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete = []
        complete = []
        
        if all(todo.complete for todo in self.todos):
            raise Exception("All tasks are complete!")
        else:
            for todo in self.todos:
                if todo.complete == False:
                    incomplete.append(todo.task)
            return incomplete

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete = []
        if all(not todo.complete for todo in self.todos):
            raise Exception("All tasks are incomplete!")
        else:
            for todo in self.todos:
                if todo.complete == True:
                    complete.append(todo.task)
            return complete

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass