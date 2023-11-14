from lib.todo_list import *

def test_todo_list():
    todo_list = Todo()
    pass

def test_add_task():
    todo_list = Todo()
    result = todo_list.add_task('shopping')
    assert result == ['shopping']

def test_task_complete():
    todo_list = Todo()
    todo_list.add_task('shopping')
    result = todo_list.task_complete('shopping')
    assert result == []
