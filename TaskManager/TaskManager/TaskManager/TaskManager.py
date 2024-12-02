import tkinter as tk
from services.task_manager import TaskManager
from ui.app import TaskManagerApp

if __name__ == "__main__":
    root = tk.Tk()
    task_manager = TaskManager()
    app = TaskManagerApp(root, task_manager)
    root.mainloop()
