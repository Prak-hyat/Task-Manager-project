import pytest
from task_manager import TaskManager
from task import Task

def test_add_task():
    tm = TaskManager()
    t = Task("A", "Test", "Today")

    tm.add(t)

    assert len(tm.list_tasks()) == 1
    assert tm.list_tasks()[0].title() == "A"


def test_mark_complete_success():
    tm = TaskManager()
    t1 = Task("Homework", "Math", "Monday")
    tm.add(t1)

    result = tm.complete("Homework")

    assert result is True
    assert t1.is_done() is True


def test_mark_complete_failure():
    tm = TaskManager()

    result = tm.complete("Missing Task")

    assert result is False


def test_list_pending_and_done():
    tm = TaskManager()

    t1 = Task("Task1", "Desc", "Date")
    t2 = Task("Task2", "Desc2", "Date2")
    tm.add(t1)
    tm.add(t2)

    t1.mark_done()

    done = tm.list_tasks(done=True)
    pending = tm.list_tasks(done=False)

    assert len(done) == 1
    assert len(pending) == 1

    assert done[0].title() == "Task1"
    assert pending[0].title() == "Task2"


def test_clear_completed():
    tm = TaskManager()

    t1 = Task("A", "aaa", "Today")
    t2 = Task("B", "bbb", "Tomorrow")

    tm.add(t1)
    tm.add(t2)

    t1.mark_done()

    tm.clear_completed()

    remaining = tm.list_tasks()

    assert len(remaining) == 1
    assert remaining[0].title() == "B"
