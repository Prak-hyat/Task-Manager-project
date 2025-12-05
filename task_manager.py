from task import Task
class TaskManager:
    def __init__(self):
        self._tasks = []

    def add(self, task: Task):
        self._tasks.append(task)

    def complete(self, title):
        for t in self._tasks:
            if t.title() == title:
                t.mark_done()
                return True
        return False

    def clear_completed(self):
        self._tasks = [t for t in self._tasks if not t.is_done()]

    def list_tasks(self, done=None):
        if done is None:
            return list(self._tasks)
        return [t for t in self._tasks if t.is_done() == done]
