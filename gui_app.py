import tkinter as tk
from tkinter import messagebox
from task import Task
from task_manager import TaskManager

class TaskApp:
    def __init__(self, root):
        self.manager = TaskManager()
        self.root = root

        root.title("Task Manager")
        root.geometry("600x420")
        root.resizable(False, False)

        tk.Label(root, text="Task Title:").pack()
        self.title_entry = tk.Entry(root, width=50)
        self.title_entry.pack()

        tk.Label(root, text="Description:").pack()
        self.desc_entry = tk.Entry(root, width=50)
        self.desc_entry.pack()

        tk.Label(root, text="Due Date:").pack()
        self.due_entry = tk.Entry(root, width=50)
        self.due_entry.pack()

        tk.Button(root, text="Add Task", command=self.add_task).pack(pady=4)
        tk.Button(root, text="Complete Task (by Title)", command=self.complete).pack(pady=4)
        tk.Button(root, text="Remove Completed Tasks", command=self.remove_completed).pack(pady=4)
        tk.Button(root, text="Show All", command=self.display_all).pack(pady=4)
        tk.Button(root, text="Show Pending", command=lambda: self.display(False)).pack(pady=4)
        tk.Button(root, text="Show Completed", command=lambda: self.display(True)).pack(pady=4)

        self.listbox = tk.Listbox(root, width=85, height=10)
        self.listbox.pack(pady=10)

    def add_task(self):
        t = self.title_entry.get().strip()
        d = self.desc_entry.get().strip()
        due = self.due_entry.get().strip()

        if not t or not d or not due:
            messagebox.showwarning("Missing Info", "All fields must be filled.")
            return

        self.manager.add(Task(t, d, due))
        self.refresh()
        messagebox.showinfo("Added", "Task created successfully.")

        self.title_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.due_entry.delete(0, tk.END)

    def complete(self):
        title = self.title_entry.get().strip()

        if not title:
            messagebox.showwarning("Error", "Enter a task title to complete.")
            return

        if self.manager.complete(title):
            messagebox.showinfo("Updated", f"Marked '{title}' as done.")
        else:
            messagebox.showerror("Not Found", "Task not found.")

        self.refresh()

    def remove_completed(self):
        self.manager.clear_completed()
        self.refresh()
        messagebox.showinfo("Removed", "Completed tasks deleted.")

    def display(self, done):
        self.listbox.delete(0, tk.END)
        for t in self.manager.list_tasks(done):
            self.listbox.insert(tk.END, t.info())

    def display_all(self):
        self.refresh()

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for t in self.manager.list_tasks():
            self.listbox.insert(tk.END, t.info())
