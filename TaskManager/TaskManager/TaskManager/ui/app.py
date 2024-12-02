import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from services.interfaces import ITaskManager
from models.task import Task

class TaskManagerApp:
    def __init__(self, root, task_manager: ITaskManager):
        self.task_manager = task_manager
        self.root = root
        self.root.title("Task Manager")
        self.setup_ui()

    def setup_ui(self):
        # Eingabefelder und Dropdown-Menü für Priorität
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        self.entry_task = tk.Entry(frame, width=20)
        self.entry_task.pack(side=tk.LEFT, padx=5)
        self.entry_task.insert(0, "Task Name")

        self.entry_user = tk.Entry(frame, width=20)
        self.entry_user.pack(side=tk.LEFT, padx=5)
        self.entry_user.insert(0, "User")

        self.entry_date = DateEntry(frame, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.entry_date.pack(side=tk.LEFT, padx=5)

        self.entry_priority = tk.StringVar(value="medium")
        dropdown_priority = tk.OptionMenu(frame, self.entry_priority, "high", "medium", "low")
        dropdown_priority.pack(side=tk.LEFT, padx=5)

        btn_add = tk.Button(frame, text="Add Task", command=self.add_task)
        btn_add.pack(side=tk.LEFT, padx=5)

        # Task-Liste
        self.listbox_tasks = tk.Listbox(self.root, width=100, height=10)
        self.listbox_tasks.pack(pady=10)

        # Buttons für "Mark Done" und "Delete Task"
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(pady=10)

        btn_done = tk.Button(frame_buttons, text="Mark Done", command=self.mark_task_done)
        btn_done.pack(side=tk.LEFT, padx=5)

        btn_delete = tk.Button(frame_buttons, text="Delete Task", command=self.delete_task)
        btn_delete.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        # Task erstellen und zur Liste hinzufügen
        name = self.entry_task.get()
        user = self.entry_user.get()
        due_date = self.entry_date.get_date()
        priority = self.entry_priority.get()
        if name and user:
            task = Task(name, user, due_date, priority)
            self.task_manager.add_task(task)
            self.refresh_tasks()
        else:
            messagebox.showwarning("Warning", "Task Name, User, and Priority are required!")

    def mark_task_done(self):
        # Task als erledigt markieren
        try:
            selected_index = self.listbox_tasks.curselection()[0]
            self.task_manager.mark_task_done(selected_index)
            self.refresh_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "No Task Selected!")

    def delete_task(self):
        # Task aus der Liste entfernen
        try:
            selected_index = self.listbox_tasks.curselection()[0]
            self.task_manager.delete_task(selected_index)
            self.refresh_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "No Task Selected!")

    def refresh_tasks(self):
        # Aktualisiere die Anzeige der Task-Liste
        self.listbox_tasks.delete(0, tk.END)
        for task in self.task_manager.get_tasks():
            self.listbox_tasks.insert(tk.END, str(task))
