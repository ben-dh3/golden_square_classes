# As a user
# So that I can keep track of my tasks
# I want a program that I can add todo tasks to and see a list of them.
# return list

# As a user
# So that I can focus on tasks to complete
# I want to mark tasks as complete and have them disappear from the list.

class Todo:
    def __init__(self):
        self.todo_list = []

    def add_task(self,task):
        self.todo_list.append(task)
        return self.todo_list

    def task_complete(self,task):
        self.todo_list.remove(task)
        return self.todo_list