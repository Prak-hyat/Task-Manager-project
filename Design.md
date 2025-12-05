# Smart Task Manager — Design Document

This document explains the design choices and software architecture used in the Smart Task Manager Python project.

---

## 1. Program Goal
The purpose of the program is to build a functioning task management system that demonstrates object-oriented programming principles.  
It allows users to add tasks, mark them complete, remove completed tasks, and filter tasks through a simple graphical user interface.

---

## 2. OOP Design

### **Encapsulation**
- Task attributes such as title, description, and completion status are stored in protected variables (`_title`, `_details`, `_finished`).
- Getters and methods (like `finish()`, `is_done()`) manage access to task state.

### **Inheritance**
- **Task** is the base class.
- **UrgentTask** adds urgency and priority level.
- **TimedTask** adds a timestamp for when the task is created.

### **Polymorphism**
Every class implements its own `info()` method:
- Task → basic display  
- UrgentTask → adds urgency label  
- TimedTask → adds timestamp  

The TaskManager and GUI treat all tasks the same (polymorphic behavior).

---

## 3. Design Pattern: Strategy
The program uses a **Strategy Pattern** for storage:

### Storage Options:
- **MemoryStore** → simple in-memory list (used for tests)  
- **JSONStore** → stores tasks in a JSON file  

Both implement the same methods:  
`save(tasks)` and `load()`

This allows TaskManager to change its saving mechanism without changing its code.

---

## 4. Architecture Overview (MVC-like)

### **Model**
- `Task`, `UrgentTask`, `TimedTask`
- `TaskManager` manages creation, search, deletion, filtering, and interacts with storage.

### **View**
- Tkinter GUI in `gui_app.py`
- Displays tasks and accepts user input.

### **Controller**
- Event functions in `TaskGUI`
- Connects the GUI actions to the TaskManager logic.

---

## 5. Error Handling
- Prevent adding empty task titles  
- Warn user when completing a task that doesn’t exist  
- Safe loading for missing JSON files  
- Prevent crashes on empty or invalid user input  

---

## 6. Testing
Tests are written using **pytest** (`test_task_system.py`):

Tests include:
- Add and find task  
- Mark as complete  
- Deleting completed tasks  
- JSON storage save/load  
- Polymorphism behavior  

A failing test can be generated if needed for demonstration.

---

## 7. Future Improvements
- Edit existing tasks through the GUI  
- Add task categories (School, Work, Personal)  
- Sort tasks by urgency or due date  
- Add calendar integration  
- Auto-save changes  
- Dark mode GUI  
- Database-backed storage (SQLite)

---

## 8. Summary
This project demonstrates:
- Core OOP concepts  
- A functional GUI  
- A clean modular architecture  
- The Strategy design pattern  
- Unit testing with pytest  

It meets the requirements for a Stage 2 OOP project.
