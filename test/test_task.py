import pytest
from task import Task

def test_new_task_defaults():
    t = Task("Buy milk", "From grocery store", "Tomorrow")
    assert t.title() == "Buy milk"
    assert t.is_done() is False

def test_mark_task_done():
    t = Task("Clean room", "Organize closet", "Saturday")
    assert not t.is_done()

    t.mark_done()

    assert t.is_done() is True

def test_task_info_format():
    t = Task("Study", "Chapters 1-3", "2025-12-01")
    text = t.info()

    assert "Study" in text
    assert "Chapters 1-3" in text
    assert "2025-12-01" in text
    assert "Pending" in text

    t.mark_done()
    assert "Completed" in t.info()
