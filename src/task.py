class Task:
    def __init__(self, title, details, due):
        self._title = title
        self._details = details
        self._due = due
        self._done = False

    def title(self):
        return self._title

    def mark_done(self):
        self._done = True

    def is_done(self):
        return self._done

    def info(self):
        state = "✓ Completed" if self._done else "✗ Pending"
        return f"{self._title} - {self._details} (Due: {self._due}) [{state}]"
